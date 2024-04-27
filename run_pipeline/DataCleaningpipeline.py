import pandas as pd
import numpy as np

from src.main_src.data_cleaning import DataClean

import sys

from src.exceptions import CustomException
from src.logger import logging

df = pd.read_csv(r'D:\Credit-card-approval-predictor\data\Raw_data\NewData.csv')
logging.info("Dataset loaded")

logging.info("Performing data cleaning.")

clean = DataClean(df)
df1 = clean.step_1_Drop_column(df)
df2 = clean.step_2_cnt_children(df1)
df3 = clean.step_3_amt_income_total(df2)
df4 = clean.step_4_days_birth(df3)
df5 = clean.step_5_days_emp(df4)
df6 = clean.step_6_occupation_type(df5)
clean.step_7_save_model(df6)

logging.info("Datacleaning Completed.")

