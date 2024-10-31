import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import logging
import io
import boto3
import os
import matplotlib
from sklearn.preprocessing import label_binarize
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import roc_curve, auc
from botocore.exceptions import ClientError
from datetime import datetime
from functools import wraps
from sklearn.metrics import confusion_matrix
matplotlib.use('Agg')

class LoggerHelper:
    def __init__(self, log_level):
        self.logger = self.setup_logger(log_level)
        self.start_time = None
        self.end_time = None
    
    def setup_logger(self, log_level):
        logger = logging.getLogger('OceanAI_logger')
        logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

        if not logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(message)s')
            # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            # logger.debug("added new handler")
        return logger
    
    def check_verbose(self, log_level):
        if log_level == 'DEBUG':
            verbose = 2
        elif log_level == 'INFO':
            verbose = 1
        return verbose
    
    # 데코레이터
    def log_execution_time(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            self.logger.info(f"'{func.__name__}' 시작")
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                duration = end_time - start_time
                self.logger.info(f"'{func.__name__}' 완료")
                self.logger.info(f"시작 시간: {start_time}")
                self.logger.info(f"종료 시간: {end_time}")
                self.logger.info(f"실행 시간: {duration}")
                return result
            except Exception as e:
                self.logger.error(f"'{func.__name__}' 실행 중 오류 발생: {e}")
                raise
        return wrapper
    
    def log_parameters(self, **params):
        param_lines = []
        custom_labels = {
        'dep_var': '종속 변수',
        'indep_var': '독립 변수',
        'model': '모델 파라미터 정보'
        }
        split_info_keys = {'train_size', 'test_size', 'random_state', 
                           'X_train', 'y_train', 'X_test', 'y_test'}
        
        for key, value in params.items():
            if key in split_info_keys:
                if key == 'train_size':
                    param_lines.append(f"학습-테스트 데이터 분할 정보 \ntrain_size={value}")
                elif key == 'test_size':
                    param_lines.append(f"test_size={value}")
                elif key == 'random_state':
                    param_lines.append(f"random_state={value}")
                elif key == 'X_train':
                    param_lines.append(f"학습 데이터 크기\nX_train={value.shape}")
                elif key == 'y_train':
                    param_lines.append(f"y_train={value.shape}")
                elif key == 'X_test':
                    param_lines.append(f"테스트 데이터 크기\nX_test={value.shape}")
                elif key == 'y_test':
                    param_lines.append(f"y_test={value.shape}") 
            else:       
                if isinstance(value, pd.DataFrame):
                    formatted_value = self.format_dataframe(value)
                    label = custom_labels.get(key, '데이터 프레임')
                elif isinstance(value, pd.Series):
                    formatted_value = self.format_series(value)
                    label = custom_labels.get(key, '데이터 시리즈')
                elif isinstance(value, (dict, list)):
                    formatted_value = self.format_json(value)
                    label = custom_labels.get(key, 'JSON Parameter')
                elif hasattr(value, 'get_params'):
                    formatted_value = self.format_model_params(value)
                    label = custom_labels.get(key, '모델 파라미터')
                else:
                    formatted_value = str(value)
                    label = 'General Parameter'

                param_lines.append(f"\n{label} ({key})\n{formatted_value}")
                param_message = "\n\n".join(param_lines)
        param_message = "\n".join(param_lines)
        self.logger.debug(f"데이터 정보를 출력합니다.\n{param_message}")
    
    def format_dataframe(self, df):
        df_info = f"DataFrame Shape: {df.shape} \nColumns: {', '.join(df.columns)}"
        preview = df.head(5).to_string()
        return f"{df_info}\n데이터 미리보기\n{preview}"
    
    def format_series(self, series):
        series_info = f"Series Shape: {len(series)} \nName: {series.name if series.name else '없음'}"
        preview = series.head(5).to_string()
        return f"{series_info}\n데이터 미리보기\n{preview}"
    
    def format_json(self, obj):
        return json.dumps(obj, indent=4)
    
    def format_model_params(self, model):
        if self.logger.isEnabledFor(logging.INFO):
            additional_info = []
            attributes = [
                ('Search Type', model.__class__.__name__),
                ('Estimator', getattr(model, 'estimator', None)),
                ('Cross-Validation Folds', getattr(model, 'cv', None)),
                ('Input Parameters', getattr(model, 'param_grid', None)),
                ('Best Parameters', getattr(model, 'best_params_', None)),
                ('Best Score', getattr(model, 'best_score_', None)),
                ('Classes', getattr(model.best_estimator_, 'classes_', None) if hasattr(model, 'best_estimator_') else None),
                ('Classes Count', getattr(model.best_estimator_, 'class_count_', None) if hasattr(model, 'best_estimator_') else None),
                ('Classes Prior', getattr(model.best_estimator_, 'class_prior_', None) if hasattr(model, 'best_estimator_') else None)
            ]
            for name, value in attributes:
                if value is not None:
                    additional_info.append(f"{name}: {value}")
            return '\n'.join(additional_info)
    
    def log_event(self, event_type, status=None, fold=None, total_folds=None):
        if event_type == 'training':
            if status == 'started':
                self.start_time = datetime.now()
                self.logger.debug(f"모델 학습 시작")
            elif status == 'completed':
                self.end_time = datetime.now()
                self.logger.debug(f"모델 학습 완료")
                if self.start_time and self.end_time:
                    duration = self.end_time - self.start_time
                    self.logger.debug(f"모델 학습 소요 시간: {duration}")
                    
        elif event_type == 'prediction':
            if status == 'started':
                self.logger.debug("모델 예측 시작")
            elif status == 'completed':
                self.logger.debug("모델 예측 완료")
            elif status == 'created':
                self.logger.debug("모델 예측 결과 데이터 생성 완료")
                
        elif event_type == 'scaling':
            if status == 'started':
                self.logger.debug("데이터 스케일링 시작")
            elif status == 'completed':
                self.logger.debug("데이터 스케일링 완료")
                
        elif event_type == 'cross-validation':
            if status == 'started':
                self.logger.debug(f"교차 검증 시작 ({total_folds} folds)")
            elif status == 'completed':
                self.logger.debug("교차 검증 완료")
            elif status == 'fold_started' and fold and total_folds:
                self.logger.debug(f"Fold {fold}/{total_folds} - 교차 검증 시작")
            elif status == 'fold_completed' and fold and total_folds:
                self.logger.debug(f"Fold {fold}/{total_folds} - 교차 검증 완료")


class Private(LoggerHelper):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Private, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, log_level='DEBUG'):
        if not hasattr(self, 'initialized'):
            if not hasattr(self, 'logger'):
                super().__init__(log_level)
        
        self.session = boto3.session.Session()
        self.client = self.session.client('secretsmanager', region_name='ap-northeast-2')
        self.s3 = boto3.client('s3')
        self.bucket_name = None
        self.s3_path = None
        self.base_filename = None

        self.raw_data = None
        self.raw_info = None

    def get_secret(self, db_name):
        secret_name = 'dev/' + db_name + '/data/postgres'
        try:
            get_secret_value_response = self.client.get_secret_value(SecretId=secret_name)
            secret_value = json.loads(get_secret_value_response['SecretString'])
            return secret_value
        except ClientError as e:
            print(f'ClientError: {e}')
            return None
    
    def set_s3_info(self, param_info):
        self.s3_info = param_info['s3_info']
        self.s3_path = self.s3_info['s3_write_path']
        self.base_filename = self.s3_info['filename']
        self.bucket_name = self.s3_info['s3_repository']
    
    def upload_to_s3(self, file_name, bucket_name, s3_path):
        try:
            self.s3.upload_file(file_name, bucket_name, s3_path)
        except Exception as e:
            logging.error(f"Failed to upload {file_name}")
    
    def upload_bytes_to_s3(self, byte_stream, file_name, bucket_name, s3_path):
        try:
            byte_stream.seek(0)
            self.s3.upload_fileobj(byte_stream, bucket_name, s3_path)
        except boto3.exception.S3UploadFailedError as e:
            logging.error(f"Upload failed for file-like object {file_name}. Error: {e}")
        except Exception as e:
            logging.error(f"Failed to upload file-like object {file_name} to S3: {e}")
    
    def upload_file(self,files,var_names=None):
        if not isinstance(files, list):
            files = [files]
            
        if not isinstance(var_names, list):
            var_names = [var_names]
            
        if var_names is None:
            var_names = [None] * len(files)
        elif not isinstance(var_names, list):
            var_names = [var_names]
        elif len(var_names) != len(files):
            raise ValueError("The length of 'var_names' must match the length of 'files'.")
            
        for file_obj, var_name in zip(files, var_names):
            suffix = f"_{var_name}" if var_name else ""
            file_name = f"{self.base_filename}{suffix}"
            
            if isinstance(file_obj, pd.DataFrame):
                file_name += ".csv"
                file_obj = self.add_dtype(file_obj)
                file_obj.to_csv(file_name, index=None, encoding='utf-8')
                self.upload_to_s3(file_name, self.bucket_name, self.s3_path + file_name)
                
            elif isinstance(file_obj, dict):
                file_name += ".json"
                self.save_to_json(file_obj, file_name)
                self.upload_to_s3(file_name, self.bucket_name, self.s3_path + file_name)
                
            elif isinstance(file_obj, plt.Figure):
                file_name += ".png"
                img_bytes = io.BytesIO()
                file_obj.savefig(img_bytes, format='png')
                img_bytes.seek(0)
                self.upload_bytes_to_s3(img_bytes, file_name, self.bucket_name, self.s3_path + file_name)

            if file_name:
                self.cleanup_files([file_name])
    
    def cleanup_files(self, file_names):
        for file_name in file_names:
            if os.path.exists(file_name):
                os.remove(file_name)

    def read_csv(self,file_path):
        raw = pd.read_csv(file_path)
        dtype_dict = {col: dtype for col, dtype in zip(raw.columns, list(raw.iloc[0]))}
        df = raw.iloc[1:]
        df = df.astype(dtype_dict)
        
        first_column_name = df.columns[0]
        df.set_index(first_column_name, inplace=True)
        df = df.dropna(how='any')
        return df, dtype_dict
    
    def read_data(self, INPUT, file_path, json_data, schema_json):
        self.raw_info = schema_json
        self.raw_data, dtype_dict = self.read_csv(file_path)
        X, y = None, None
        
        if schema_json:
            df = self.raw_data.copy()
        else:
            print("데이터 속성 정보가 없어서 프레임 재구성을 할 수 없습니다.")
            df = self.raw_data
        # 컬럼 데이터 타입 검증(allowed_data_types)
        column_valid = self.validate_selected_column(df, dtype_dict, json_data)
        # 스케일링 컬럼 검증
        if column_valid:
            X, y = self.validate_scaling_columns(df, INPUT)
        return X, y
    
    def reshape_for_model(self, INPUT, X_train, y_train, X_test=None, y_test=None):
        feature = X_train.columns
        target = y_train.columns
        
        if X_test is None and y_test is None:
            train_data = pd.concat([X_train, y_train], axis=1)
            X_train_data, y_train_data = self.reshape_frame(train_data, feature, target)
            return X_train_data, y_train_data
        
        else:
            train_data = pd.concat([X_train, y_train], axis=1)
            test_data = pd.concat([X_test, y_test], axis=1)
        
            # reshape -> model에 입력되는 형태로 재가공
            X_train_data, y_train_data = self.reshape_frame(train_data, feature, target)
            X_test_data, y_test_data = self.reshape_frame(test_data, feature, target)
        
            return X_train_data, y_train_data, X_test_data, y_test_data
    
    def validate_scaling_columns(self, df, INPUT):
        # 스키마 딕셔너리
        column_schema = {
            item['name']: {
                'ticker': item.get('ticker', None),
                'property': item.get('property', None),
                'description': item.get('description', None),
            }
            for item in self.raw_info['columns']
        }
        
        ticker_property_map = {} # 피처 컬럼들의 ticker-property 세트
        scaling_columns = []
        excluded_scaling_columns = []
        
        selected_columns = []
        selected_ticker_properties = set() # common properties
        
        features = INPUT['indep_var']
        target_columns = INPUT['dep_var']
        
        # 스키마에서 스케일링 컬럼 조회
        for item in self.raw_info['columns']:
            if 'scaling' in item['description'].lower(): # 스키마 구조가 변경되면 변경이 필요함
                scaling_columns.append(item['name'])
        
        # 피처 컬럼에서 스케일링된 컬럼 제외
        for column in features:
            column_info = column_schema[column]
            ticker = column_info['ticker']
            property_name = column_info['property']
            
            if 'scaling' in column_info['description'].lower():
                excluded_scaling_columns.append(column)
            else:
                selected_columns.append(column) # 스케일링 컬럼 제외한 타겟 컬럼
                if ticker not in ticker_property_map:
                    ticker_property_map[ticker] = set()
                ticker_property_map[ticker].add(property_name)
                
        # 공통 속성 조회 - validation
        if not selected_columns:
            print("선택된 독립변수 중에 공통 속성을 가진 컬럼이 없어 학습을 중단합니다.")
            return None, None
        else:
            if excluded_scaling_columns:
                print(f"이미 스케일링이 적용된 컬럼은 학습 대상에서 제외됩니다: {', '.join(excluded_scaling_columns)}")

            common_properties = set.intersection(*ticker_property_map.values())
            final_selected_columns = []
            
            for column in selected_columns:
                if column in column_schema:
                    column_info = column_schema[column]
                    ticker = column_info['ticker']
                    property_name = column_info['property']
                    
                    if property_name in common_properties:
                        final_selected_columns.append(column) # 공통 속성과 같은 컬럼만 추출
                        # 공통 속성이 있는 티커만 추출 -> y 컬럼에서 조회하기 위함
                        if common_properties.issubset(ticker_property_map[ticker]):
                            selected_ticker_properties.add(ticker)

            selected_columns = final_selected_columns
            
            filtered_target_columns = []
            for target in target_columns:
                if target in column_schema:
                    target_ticker = column_schema[target]['ticker']
                    if target_ticker in selected_ticker_properties:
                        filtered_target_columns.append(target)
                    
            X = df[selected_columns]
            y = df[filtered_target_columns]
        return X, y
    
    def select_scaler(self, scaler_option):
        if scaler_option == 'minmax':
            scaler = MinMaxScaler()
        elif scaler_option == 'standard':
            scaler = StandardScaler()
        else:
            scaler = None  # No scaling
        return scaler
    
    def scale_data(self, scaler, train_set, test_set=None):
        if scaler is None:
            if test_set is None:
                return train_set
            else:
                return train_set, test_set
        else:
            if test_set is None:
                train_scaled = pd.DataFrame(scaler.fit_transform(train_set), index=train_set.index, columns=train_set.columns)
                return train_scaled
            else:
                train_scaled = pd.DataFrame(scaler.fit_transform(train_set), index=train_set.index, columns=train_set.columns)
                test_scaled = pd.DataFrame(scaler.transform(test_set), index=test_set.index, columns=test_set.columns)
                return train_scaled, test_scaled

    def reshape_frame(self, df, indep_vars, dep_vars):
        var_info = self.raw_info
        dep_var_info, indep_var_info = [], []

        for label_col in dep_vars:
            for column in var_info['columns']:
                if column['name'] == label_col:
                    dep_var_info.append(column)
        
        for label_col in indep_vars:
            for column in var_info['columns']:
                if column['name'] == label_col:
                    indep_var_info.append(column)        

        dep_tickers = set(info['ticker'] for info in dep_var_info)
        indep_tickers = set(info['ticker'] for info in indep_var_info)
        
        dep_df = self.build_rows(df, dep_tickers, dep_var_info).squeeze()
        indep_df = self.build_rows(df, indep_tickers, indep_var_info)
        return indep_df, dep_df
    
    def build_rows(self, df, tickers, target_var_info):
        # var_info에서 ticker와 property 정보를 기반으로 재구성
        rows = []
        index_name = df.index.name
        for date in df.index:
            for ticker in tickers:
                row = {'ticker': ticker, index_name: date}
                for info in target_var_info:
                    if info['ticker'] == ticker:
                        col_name = info['name']
                        prop_name = info['property']
                        
                        row[prop_name] = df.at[date, col_name]
                rows.append(row)
                
        result_df = pd.DataFrame(rows).set_index([df.index.name, 'ticker']).sort_index()
        return result_df
    
    def merge_result(self, X_test, df_result):
        original_df = self.raw_data.copy()
        
        df_result = pd.concat([X_test, df_result], axis=1)
        df_result = df_result.reset_index().set_index(original_df.index.name)
        
        column_properties = ['y_true', 'y_pred']
        if 'y_prob' in df_result.columns:
            column_properties.append('y_prob') # 분류 모델일 경우 확률 값 추가
        
        if 'ticker' in df_result.columns: # ticker 컬럼 여부 확인
            unique_tickers = df_result['ticker'].unique()
            for ticker in unique_tickers:
                df_ticker = df_result[df_result['ticker'] == ticker]
                for base_col_name in column_properties:
                    col_name = f'{ticker}_{base_col_name}'
                    original_df.loc[df_ticker.index, col_name] = df_ticker[base_col_name].values
        else:
            for base_col_name in column_properties:
                original_df[base_col_name] = df_result[base_col_name].values

        original_df = original_df.loc[original_df.index.isin(df_result.index)]
        return original_df
    
    def generate_schema_json(self, params, schema_json, func_name=None):
        self.set_s3_info(params)
        dep_var = params['dep_var']
        column_properties = {
            'y_true': {'property': 'true_value', 'data_type': 'int64'},
            'y_pred': {'property': 'predictive_value', 'data_type': 'float64'},
            'y_prob': {'property': 'probability', 'data_type': 'int64'}
        }
        for label_col in dep_var:
            for column in schema_json['columns']:
                if column['name'] == label_col:
                    ticker = column['ticker']
                    ticker_type = column['ticker_type']
                    
                    for prefix, properties in column_properties.items():
                        col_name = f"{ticker}_{prefix}"
                        param = {
                            "name": col_name,
                            "ticker": ticker if ticker else "",
                            "ticker_type": ticker_type,
                            "property": properties['property'],
                            "description": f"{properties['property']}",
                            "data_type": properties['data_type'],
                            "created_by": func_name
                            }
                        schema_json['columns'].append(param)
        
        self.upload_file(schema_json)
        return schema_json

    def add_dtype(self,df):
        if type(df.index) == pd.core.indexes.range.RangeIndex:
            pass
        else:
            df = df.reset_index()
        column_and_type = [(col, df[col].dtype) for col in df.columns]
        df.columns = pd.MultiIndex.from_tuples(column_and_type)
        return df
    
    def parse_json(self,json_string: str) -> dict:
        try:
            data_dict = json.loads(json_string)
            return data_dict
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {}
        
    def read_json(self, file_path):
        if not os.path.exists(file_path):
            print(f"데이터 속성 파일 {file_path}이 존재하지 않습니다.")
        with open(file_path, 'r') as file:
            params = json.load(file)
            print(f"데이터 속성 파일 {file_path}이 로드되었습니다.")
        return params
    
    def generate_report(self, INPUT=None, accuracy=None, report=None, matrix=None, auc_score=None, mse=None, rmse=None, mae=None, r2=None):
        if INPUT['pred_type'] != 'reg':
            # Classification Report Generation
            report_df = pd.DataFrame(report).transpose().reset_index().rename(columns={'index': 'Class'})
            class_labels = report_df['Class'][:len(matrix)].tolist()
            num_classes = matrix.shape[1]
            column_names = [f'Predicted {i}' for i in range(num_classes)]

            matrix_df = pd.DataFrame(matrix, columns=column_names)
            matrix_df['Class'] = class_labels
            matrix_df = matrix_df[['Class'] + column_names]

            combined_df = pd.merge(report_df, matrix_df, on='Class', how='left')

            metrics_df = pd.DataFrame({
                'Class': ['Accuracy', 'AUC Score'],
                'Score': [accuracy, auc_score],
                'precision': [None, None],
                'recall': [None, None],
                'f1-score': [None, None],
                'support': [None, None],
                'Predicted 0': [None, None],
                'Predicted 1': [None, None]
            })

            for col in column_names:
                metrics_df[col] = [None, None]

            final_df = pd.concat([metrics_df, combined_df], ignore_index=True)
            final_df = final_df.set_index('Class')

        else:
            # Regression Report Generation
            final_df = pd.DataFrame({
                'Metric': ['Mean Squared Error (MSE)', 'Root Mean Squared Error (RMSE)', 
                        'Mean Absolute Error (MAE)', 'R2 Score'],
                'Score': [mse, rmse, mae, r2]
            })

        final_df = final_df.fillna(' ')
        self.log_event('evaluation', status='completed')
        self.log_parameters(evaluation_report=final_df)
        return final_df
    
    def save_to_json(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    def confusion_matrix(self,y, y_pred):
        classes = sorted(y.unique())
        matrix = confusion_matrix(y, y_pred, labels=classes)
        df = pd.DataFrame(matrix, columns=[f'Predicted {cls}' for cls in classes], index=[f'Actual {cls}' for cls in classes])
        return df
    
    def roc_curve(self, y, probabilities):
        classes = sorted(list(set(y)))
        n_classes = len(classes)
        plt.figure(figsize=(8, 6))
        
        if n_classes > 2:
            y_bin = label_binarize(y, classes=classes)
        
            for i, class_name in enumerate(classes):
                y_prob = probabilities[:, i]
                fpr, tpr, _ = roc_curve(y_bin[:, i], y_prob) # ROC 곡선 계산
                auc_score = auc(fpr, tpr) # AUC 값 계산
                plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'{class_name} (AUC = {auc_score:.2f})')
                
        else:  # Binary case
            y_prob = probabilities[:, 1]
            fpr, tpr, _ = roc_curve(y, y_prob)
            auc_score = auc(fpr, tpr)
            class_name = classes[1]
            plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'{class_name} (AUC = {auc_score:.2f})')
                
            plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristic (ROC) Curve')
            plt.legend(loc="lower right")
            
        fig = plt.gcf()
        plt.close()  
        return fig, auc_score

    def get_parameters(self, json_data):
        parameters = {
            'model_par': {},
            's3_info':{}
            }
        
        s3_storage = json_data['s3_storage']
        node_information = json_data['node_information']
        parameters['s3_info']['s3_repository'] = s3_storage.get('s3_repository', None)
        parameters['s3_info']['s3_write_path'] = s3_storage.get('s3_write_path', None)
        parameters['s3_info']['filename'] = node_information.get('user_defined_name', None)
        # parameters['s3_info']['filename'] = s3_storage.get('filename', None)
        
        for parameter in json_data['parameters']:
            area = parameter['area']
            options = parameter.get('options')
            parameter_name = parameter['parameter_name']
            selected_value = parameter.get('selected_value')
            
            if options:
                if area == 'hyperparameter':
                    if selected_value == 'values':
                        values_option = next((opt for opt in options if opt['value'] == 'values'), None)
                        if values_option:
                            parameter_value  = [member['selected_value'] for member in values_option['members']]
                            if len(parameter_value) == 1:
                                parameter_value = parameter_value[0]
                    elif selected_value == 'range':
                        range_option = next((opt for opt in options if opt['value'] == 'range'), None)
                        if range_option:
                            range_members = range_option['members']
                            range_values = {member['name']: member['selected_value'] for member in range_members}
                            value_types = {member['name']: member['value_type'] for member in range_members}

                            min_val = range_values['min']
                            max_val = range_values['max']
                            count = range_values['count']
                            dist = range_values['dist']
                            
                            if dist == 'uniform':
                                if value_types['min'] == 'integer' and value_types['max'] == 'integer':
                                    parameter_value = np.linspace(min_val, max_val, count).astype(int).tolist()
                                else:
                                    parameter_value = np.linspace(min_val, max_val, count).tolist()
                            elif dist == 'log_uniform':
                                min_val = float(min_val)
                                max_val = float(max_val)
                                parameter_value = np.logspace(np.log10(min_val), np.log10(max_val), count).tolist()
                            else:
                                parameter_value = None
                        else:
                            parameter_value = None
                    else:
                        if isinstance(selected_value, list) and len(selected_value) == 1:
                            parameter_value = selected_value[0] 
                        else:
                            parameter_value = selected_value
                    parameters['model_par'][parameter_name] = parameter_value
                else:
                    parameters[parameter_name] = selected_value
            else:
                parameters[parameter_name] = selected_value
        return parameters
    
    def validate_data(self,json_data):
        # 스키마 검증
        if isinstance(json_data, str):
            print("데이터 속성 파일이 없습니다.")
        # 데이터 타입 검증
        is_value_valid = self.validate_selected_value(json_data)
        if is_value_valid:
            return True
        else:
            return False
            
    def get_pred_type(self, json_data):
        for item in json_data['parameters']:
            if item.get('parameter_name') == 'pred_type':
                return item.get('selected_value')
        return None
        
    def validate_selected_column(self, df, dtype_dict, json_data):
        pred_type = self.get_pred_type(json_data)
        selected_value = {
            item['parameter_name']: {
                'allowed_data_types': item['allowed_data_types'],
                'n_unique_value': item.get('n_unique_value'),
                'selected_value': item.get('selected_value'),
                'ui_display_name_ko': item.get('ui_display_name_ko')
            }
            for item in json_data['parameters'] if item.get('allowed_data_types')}
        
        dtype_map = {
            'int': 'int64',
            'float': 'float64',
            'string': 'object',
            'datetime': 'datetime64[ns]'
            }
        
        overall_valid = True
        
        for param_name, details in selected_value.items():
            allowed_types = details['allowed_data_types']
            columns_to_check = details['selected_value']
            display_name = details['ui_display_name_ko']
            unique_value_constraints = details.get('n_unique_value', [])
            
            allowed_dtypes = [dtype_map[typ] for typ in allowed_types if typ in dtype_map]
            
            param_valid = True
            
            for col_name in columns_to_check:
                # 컬럼 존재 여부 확인
                if col_name not in dtype_dict:
                    print(f"데이터 프레임에 '{col_name}' 열이 존재하지 않습니다.")
                    param_valid = False
                    continue
                
                # 컬럼의 데이터 타입 확인
                if dtype_dict[col_name] not in allowed_dtypes:
                    print(f"'{display_name}'의 '{col_name}'열의 데이터 유형 '{dtype_dict[col_name]}'이 허용된 유형({allowed_dtypes})과 일치하지 않습니다.")
                    param_valid = False
                
                # pred_type의 unique_value 조건 조회
                if unique_value_constraints:
                    constraint = None
                    for c in unique_value_constraints:
                        if c['pred_type'] == pred_type:
                            constraint = c
                            break 
                        
                    if constraint and pred_type != 'reg':
                        unique_count = df[col_name].nunique()
                        min_val, max_val = constraint['min'], constraint['max']
                        if not (min_val <= unique_count <= max_val):
                            print(f"'{display_name}'열의 '{col_name}'의 고유값 개수 '{unique_count}'가 '{pred_type}'에 대한 허용된 범위(최소값:{min_val}, 최대값:{max_val})를 벗어납니다.")
                            param_valid = False
                            
            if not param_valid:
                overall_valid = False
        return overall_valid

    def validate_selected_value(self, json_data):
        for data in json_data['parameters']:
            value_type = data.get("value_type")
            selected_value = data.get("selected_value")
            ui_display_name = data.get("ui_display_name_ko")
            
            if value_type == "float":
                if not isinstance(selected_value, float):
                    print(f"오류: '{ui_display_name}'의 값이 실수 타입이 아닙니다. 실수형 값을 입력해 주세요.")
                    return False
            elif value_type == "integer":
                if not isinstance(selected_value, int):
                    print(f"오류: '{ui_display_name}'의 값이 정수 타입이 아닙니다. 정수형 값을 입력해 주세요.")
                    return False
            elif value_type == "string":
                if not isinstance(selected_value, str):
                    print(f"오류: '{ui_display_name}'의 값이 문자열 타입이 아닙니다. 문자 형태의 값을 입력해 주세요.")
                    return False
            elif value_type == "float_array":
                if not isinstance(selected_value, list):
                    print(f"오류: '{ui_display_name}'의 값이 리스트 형태가 아닙니다. 리스트 형태로 실수형 값을 입력해 주세요.")
                    return False
                if not all(isinstance(item, float) for item in selected_value):
                    print(f"오류: '{ui_display_name}'의 리스트 내 모든 요소가 실수 타입이 아닙니다. 모든 요소가 실수형인지 확인해 주세요.")
                    return False
            elif value_type == "integer_array":
                if not isinstance(selected_value, list):
                    print(f"오류: '{ui_display_name}'의 값이 리스트 형태가 아닙니다. 리스트 형태로 정수형 값을 입력해 주세요.")
                    return False
                if not all(isinstance(item, int) for item in selected_value):
                    print(f"오류: '{ui_display_name}'의 리스트 내 모든 요소가 정수 타입이 아닙니다. 모든 요소가 정수형인지 확인해 주세요.")
                    return False
            elif value_type == "string_array":
                if not isinstance(selected_value, list):
                    print(f"오류: '{ui_display_name}'의 값이 리스트 형태가 아닙니다. 리스트 형태로 문자열을 입력해 주세요.")
                    return False
                if not all(isinstance(item, str) for item in selected_value):
                    print(f"오류: '{ui_display_name}'의 리스트 내 모든 요소가 문자열 타입이 아닙니다. 모든 요소가 문자열인지 확인해 주세요.")
                    return False
            else:
                print(f"오류: '{ui_display_name}'의 데이터 타입('{value_type}')은 지원되지 않는 타입입니다. 올바른 유형인지 확인해 주세요.")
                return False

            value_range = data.get("value_range")
            if value_range:
                min_value = value_range.get("min")
                max_value = value_range.get("max")
            
                if min_value is None or max_value is None:
                    print(f"오류: '{ui_display_name}'에 최소값 또는 최대값이 누락되었습니다.")
                    return False
        
                if isinstance(selected_value, list):
                    if not all(min_value <= item <= max_value for item in selected_value):
                        print(f"오류: '{ui_display_name}'의 한 개 이상의 요소가 범위 [최소값:{min_value}, 최대값:{max_value}]를 벗어납니다.")
                        return False
                else:
                    if not (min_value <= selected_value <= max_value):
                        print(f"오류: '{ui_display_name}'의 값이({selected_value}) 범위 [최소값:{min_value}, 최대값:{max_value}]을 벗어납니다.")
                        return False
        return True