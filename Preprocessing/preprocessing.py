from Log_writer.logger import App_Logger
from data_loader import data_loader
from sklearn.impute import KNNImputer
import json


class Preprocessor:
    def __init__(self):
        self.log_writer=App_Logger()
        self.loader_obj=data_loader()
        self.original_data=self.loader_obj.load_data()
        self.schema_path = "Required_Data_Schema/schema.json"

    def null_value_imputer(self,data):

        try:
            schema = open(self.schema_path, 'r')
            schema_dic = json.load(schema)
            schema.close()
            bad_cols= schema_dic["removed_correlated_columns"]

            # Imputing Categorical Columns , by random sample imputation
            object_index = self.original_data.dtypes[self.original_data.dtypes == 'object'].index
            for col in object_index:
                if col in bad_cols:
                    continue
                if col=="preferred_foot":
                    continue
                if data[col].isnull().sum() > 0:
                    rand_sample = self.original_data[col].dropna().sample(1)
                    data[col].iloc[0] = rand_sample

            self.log_writer.log("Categorical columns imputed successfully")

            # Imputing Numerical Columns , by nearest neighbour imputation
            numerical_index = self.original_data.dtypes[self.original_data.dtypes != 'object'].index
            imputer = KNNImputer(n_neighbors=10, weights='distance')
            for col in numerical_index:
                if col in bad_cols:
                    continue
                if data[col].isnull().sum() > 0:
                    imputer.fit(self.original_data[[col]])
                    data[[col]] = imputer.transform(data[[col]])

            self.log_writer.log("Numerical Columns imputed successfully")

            self.log_writer.log("Null Value Imputation Completed Successfully")

            return data
        except Exception as e:
            self.log_writer.log("Error Occured while imputing null values")
            return print(e)

    def encode(self,data):
        try:
            # Frequency Encoding of attacking and defensive work rate

            attacking_rate_map = self.original_data.attacking_work_rate.value_counts().to_dict()
            defensive_rate_map = self.original_data.defensive_work_rate.value_counts().to_dict()

            # data.preferred_foot = pd.get_dummies(data.preferred_foot, drop_first=True)  # right=1 , left=0
            data.attacking_work_rate = data.attacking_work_rate.map(attacking_rate_map)
            data.defensive_work_rate = data.defensive_work_rate.map(defensive_rate_map)
            self.log_writer.log("Categorical Data Encoded Successfully")

            return data

        except Exception as e:
            self.log_writer.log("Error occured while Encoding ")
            return print(e)

    def preprocess(self,data):

        data=self.null_value_imputer(data)
        data=self.encode(data)
        return data
