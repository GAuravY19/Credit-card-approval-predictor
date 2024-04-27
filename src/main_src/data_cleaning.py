import pandas as pd
import numpy as np

import sys

from src.exceptions import CustomException
from src.logger import logging
from src.utils import calculate_yrs, save_data

class DataClean:
    """
        This class encapsulates all the essential methods for data cleaning.
    """

    def __init__(self, df:pd.DataFrame):
        logging.info("DataCleaning class initialized.")
        self.data = df



    def step_1_Drop_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This Method will remove all the non-essential columns from the dataset.

        The columns are:-
        1. 'ID'
        2. 'FLAG_MOBIL'
        3. 'FLAG_WORK_PHONE'
        4. 'FLAG_PHONE'
        5. 'FLAG_EMAIL'
        6. 'MONTHS_BALANCE'

        Args:
            df (pd.DataFrame): The dataset containing these columns

        Returns:
            pd.DataFrame: Dataset after removing the columns.
        """
        logging.info("step_1_Drop_column method started.")

        try:

            cols_to_drop = ['ID', 'FLAG_MOBIL', 'FLAG_WORK_PHONE', 'FLAG_PHONE', 'FLAG_EMAIL', 'MONTHS_BALANCE']

            df1 = df.drop(cols_to_drop, axis = 'columns')

            logging.info("step_1_Drop_column method Completed.")

            return df1

        except Exception as e:
            logging.info("step_1_Drop_column method failed.")
            raise CustomException(e, sys)



    def step_2_cnt_children(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will remove the outliers from the CNT_CHILDREN columns.

        Args:
            df (pd.DataFrame): The dataset containing the columns

        Returns:
            pd.DataFrame: Dataset after removing the outliers.
        """
        logging.info("step_2_cnt_children method started.")

        try:
            df1 = df[df['CNT_CHILDREN'] != 14]
            df2 = df1[df1['CNT_CHILDREN'] != 19]

            logging.info("step_2_cnt_children method completed.")

            return df2

        except Exception as e:
            logging.info("step_2_cnt_children method failed.")
            raise CustomException(e, sys)



    def step_3_amt_income_total(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will remove the outliers from the AMT_INCOME_TOTAL columns.

        Args:
            df (pd.DataFrame): The dataset containing the columns

        Returns:
            pd.DataFrame: Dataset after removing the outliers.
        """
        logging.info("step_3_amt_income_total method Started.")

        try:

            threshold = 1000000

            df1 = df[df['AMT_INCOME_TOTAL'] <= threshold]

            logging.info("step_3_amt_income_total method completed.")

            return df1

        except Exception as e:
            logging.info("step_3_amt_income_total method failed.")
            raise CustomException(e, sys)



    def step_4_days_birth(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will calculate the age in Years instead of days.

        Args:
            df (pd.DataFrame): The dataset containing the columns

        Returns:
            pd.DataFrame: Dataset Containing age in years in new column.
        """
        logging.info("step_4_days_birth method Started.")

        try:
            days = df['DAYS_BIRTH'].to_list()

            age = []

            for day in days:
                age.append(calculate_yrs(days = day))

            df['AGE'] = age

            df1 = df.drop(['DAYS_BIRTH'], axis = 'columns')

            logging.info("step_4_days_birth method completed.")

            return df1

        except Exception as e:
            logging.info("step_4_days_birth method failed.")
            raise CustomException(e, sys)



    def step_5_days_emp(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will calculate the employment time in Years instead of days.

        Args:
            df (pd.DataFrame): The dataset containing the columns

        Returns:
            pd.DataFrame: Dataset containing the employment time in Years instead of days.
        """
        logging.info("step_5_days_emp method Started.")

        try:

            emp_days = df['DAYS_EMPLOYED'].to_list()

            yrs = []

            for day in emp_days:
                yrs.append(calculate_yrs(days=day))

            df['YR_EMPLOYEED'] = yrs

            threshold = 50

            df1 = df[df['YR_EMPLOYEED'] <= threshold]

            df2 = df1.drop(['DAYS_EMPLOYED'], axis = 'columns')

            logging.info("step_5_days_emp method Completed.")

            return df2

        except Exception as e:
            logging.info("step_5_days_emp method failed.")
            raise CustomException(e, sys)



    def step_6_occupation_type(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will form groups of different types of occupation.

        The groups will be as follow:

            1. Administrative and Management:
                * Managers
                * Secretaries
                * HR staff

            2. Customer Service and Hospitality:
                * Sales staff
                * Waiters/barmen staff
                * Realty agents

            3. Finance and Accounting:
                * Accountants

            4. Technical and IT:
                * High skill tech staff
                * IT staff

            5. Healthcare:
                * Medicine staff
                * Support and Services:
                * Security staff
                * Core staff
                * Cleaning staff
                * Private service staff
                * Cooking staff

            6. Transportation and Logistics:
                * Drivers

            7. Labor and Maintenance:
                * Laborers
                * Low-skill Laborers

        Args:
            df (pd.DataFrame): The dataset containing this column.

        Returns:
            pd.DataFrame: Dataset with refreshed occupation type datavalues.
        """
        logging.info("step_6_occupation_type method Started.")

        try:
            occu_list = df['OCCUPATION_TYPE'].to_list()

            new_occu_list = []

            for i in occu_list:
                if i in ['Managers', 'Secretaries', 'HR staff']:
                    new_occu_list.append('Administrative and Management')

                elif i in ['Sales staff', 'Waiters/barmen staff', 'Realty agents']:
                    new_occu_list.append('Customer Service and Hospitality')

                elif i in ['Accountants']:
                    new_occu_list.append('Finance and Accounting')

                elif i in ['High skill tech staff', 'IT staff']:
                    new_occu_list.append('Technical and IT')

                elif i in ['Medicine staff']:
                    new_occu_list.append('Healthcare')

                elif i in ['Security staff', 'Core staff', 'Cleaning staff', 'Private service staff', 'Cooking staff']:
                    new_occu_list.append('Support and Services')

                elif i in ['Drivers']:
                    new_occu_list.append('Transportation and Logistics')

                elif i in ['Laborers', 'Low-skill Laborers']:
                    new_occu_list.append('Labor and Maintenance')

                else:
                    new_occu_list.append(i)

            df['NEW_OCC_COL'] = new_occu_list

            df.dropna(inplace=True)

            df1 = df.drop(['OCCUPATION_TYPE'], axis = 'columns')

            logging.info("step_5_days_emp method Completed.")

            return df1

        except Exception as e:
            logging.info("step_5_days_emp method failed.")
            raise CustomException(e, sys)



    def step_7_save_model(self, df:pd.DataFrame):
        """
        This method will save cleaned data to csv file.

        Args:
            df (pd.DataFrame): The dataset which is ready to be saved.
        """

        logging.info("Saving of Model started.")

        save_data(name='Clean_data.csv',
                  path = 'D:/Credit-card-approval-predictor/data/clean_data',
                  df=df)

        logging.info("Saving of Model Completed.")


