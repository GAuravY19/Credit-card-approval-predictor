import pandas as pd

from src.main_src.feature_engineering import FeatureEngineering

from src.logger import logging

class RunFeaturePipeline:
    def __init__(self):
        self.df = pd.read_csv(r'D:\Credit-card-approval-predictor\data\clean_data\Clean_data.csv')
        logging.info("Dataset loaded")

        logging.info("Performing Feature engineering.")

        self.feature = FeatureEngineering(self.df)

    def RunMethods(self):
        df1 = self.feature.step_01_drop_columns(self.df)
        df2 = self.feature.step_02_realty_col(df1)
        df3 = self.feature.step_03_income_column(df2)
        df4 = self.feature.step_04_cnt_child_column(df3)
        df5 = self.feature.step_06_income_type_column(df4)
        df6 = self.feature.step_07_education_column(df5)
        df7 = self.feature.step_08_Housing_type_column(df6)
        df8 = self.feature.step_09_Fam_Member_column(df7)
        df9 = self.feature.step_10_status_column(df8)
        df10 = self.feature.step_11_target_column(df9)
        df11 = self.feature.step_12_Age_column(df10)
        df12 = self.feature.step_13_Employ_column(df11)
        df13 = self.feature.step_14_Occ_column(df12)
        self.feature.step_15_save_model(df13)

        # print(df12.head())
        logging.info("Feature engineering completed.")

