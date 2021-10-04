import numpy as np
import sys
from Log_writer import logger
import json

class Validator:
    def __init__(self):
        self.log_writer = logger.App_Logger()
        self.schema_path = "Required_Data_Schema/schema.json"

    def values_from_schema(self):

        try:
            schema = open(self.schema_path, 'r')
            schema_dic = json.load(schema)
            schema.close()
            col_length = schema_dic["col_length"]
            col_names = schema_dic["col_names"]
            dtypes=schema_dic["dtypes"]
            self.log_writer.log("Extracted column length and column names from schema")
            return col_length, col_names ,dtypes

        except Exception as e:
            self.log_writer.log("Error occured in extracting values from schema")
            return print(e)

    def validate(self, data):
        try :
            col_length, col_names, dtypes = self.values_from_schema()

            # validating column length
            if data.shape[1] == col_length:
                self.log_writer.log("Column Length Validated")
            else:
                self.log_writer.log(f"Column Lengths are greater or less than 29")
                sys.exit()

            # validate column names
            if set(list(data.columns)) == set(col_names):
                self.log_writer.log("Column Names Validated")
            else :
                self.log_writer.log("Column names are not as required by the format")
                sys.exit()

            # validate data types
            for col, dtype in zip(data.columns, dtypes):
                a = 0
                if data[col].dtypes == np.dtype(dtype):
                    continue
                else:
                    a += 1
                    if a > 0:
                        self.log_writer.log(f"The data type of values in column {col} is not same as {dtype}")
                        self.log_writer.log("There is an error in the data type of input data")
                    sys.exit()

        except Exception as e:
            self.log_writer.log("Error occured in data validation")
            return print(e)



