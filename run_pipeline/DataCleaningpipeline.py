import pandas as pd

from src.main_src.data_cleaning import DataClean

from src.logger import logging

class DatacleanPipeline:
    def __init__(self):

        self.df = pd.read_csv(r'D:\Credit-card-approval-predictor\data\Raw_data\NewData.csv')
        logging.info("Dataset loaded")

        logging.info("Performing data cleaning.")
        self.clean = DataClean(self.df)

    def RunningMethods(self):
        df1 = self.clean.step_1_Drop_column(self.df)
        df2 = self.clean.step_2_cnt_children(df1)
        df3 = self.clean.step_3_amt_income_total(df2)
        df4 = self.clean.step_4_days_birth(df3)
        df5 = self.clean.step_5_days_emp(df4)
        df6 = self.clean.step_6_occupation_type(df5)
        self.clean.step_7_save_model(df6)

        logging.info("Datacleaning Completed.")

