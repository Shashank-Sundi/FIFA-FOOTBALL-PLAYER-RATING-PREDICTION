from Log_writer.logger import App_Logger
import pandas as pd

class data_loader:
    def __init__(self):
        self.log_writer=App_Logger()
        #self.database="database.sqlite"

    def load_data(self):
        data=pd.read_csv("Cleaned_database_data.csv")
        self.log_writer.log("Original Data Loaded Successfully")
        return data
        # we can also load directly from database , but then we would have to clean it again

