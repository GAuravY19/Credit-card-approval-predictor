import pandas as pd
import numpy as np

import sys

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_models
from src.utils import save_data

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder

class FeatureEngineering:
    """
        This class contains all the methods for feature engineering of data.
    """

    def __init__(self, data:pd.DataFrame):
        logging.info('Class FeatureEngineering initialized')

        self.data = data
        self.path = 'D:/Credit-card-approval-predictor/artifacts'


    def step_01_drop_columns(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method removes the non-necessary columns.
        The columns are:
        1. CODE_GENDER
        2. FLAG_OWN_CAR
        3. NAME_FAMILY_STATUS

        Args:
            df (pd.DataFrame): The dataset containing the required columns.

        Returns:
            pd.DataFrame: Dataset after removing the columns.
        """
        logging.info("Inside step_01_drop_columns method")

        try:
            logging.info("Dropping of cols started.")

            col_to_drop = ['CODE_GENDER', 'FLAG_OWN_CAR', 'NAME_FAMILY_STATUS']

            df = df.drop(col_to_drop, axis='columns')

            logging.info("Dropping of cols completed.")

            return df

        except Exception as e:
            logging.info("Dropping of cols failed.")
            raise CustomException(e, sys)


    def step_02_realty_col(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method applied ONEHOTENCODING on FLAG_OWN_REALTY column.

        Args:
            df (pd.DataFrame): Dataset containing the column.

        Returns:
            pd.DataFrame: Dataset after encoding the FLAG_OWN_REALTY col.
        """
        logging.info('Inside step_02_realty_col method')

        try:
            logging.info("Encoding of realty col started.")

            realty_encoder = OneHotEncoder(drop = 'first',
                                           sparse_output=False,
                                           handle_unknown='ignore')

            realty_encoder.fit(df[['FLAG_OWN_REALTY']])

            df['FLAG_OWN_REALTY'] = realty_encoder.transform(df[['FLAG_OWN_REALTY']])

            save_models(name = 'realty.pkl',
                        path=self.path,
                        model=realty_encoder)

            logging.info("Encoding of realty col failed.")

            return df

        except Exception as e:
            logging.info("Encoding of realty col failed.")
            raise CustomException(e, sys)


    def step_03_income_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply MinMaxScaler on AMT_INCOME_TOTAL col.

        Args:
            df (pd.DataFrame): Dataset containing the AMT_INCOME_TOTAL col

        Returns:
            pd.DataFrame: Dataset containing the scaled values of AMT_INCOME_TOTAL col
        """
        logging.info('Inside step_03_income_column method')

        try:
            logging.info("Scaling of income col started.")

            annual_amt_scaler = MinMaxScaler()

            annual_amt_scaler.fit(df[['AMT_INCOME_TOTAL']])

            df['AMT_INCOME_TOTAL'] = annual_amt_scaler.transform(df[['AMT_INCOME_TOTAL']])

            save_models(name = 'annual_amt_scaler.pkl',
                        path=self.path,
                        model=annual_amt_scaler)

            logging.info("Scaling of income col completed.")

            return df

        except Exception as e:
            logging.info("Scaling of income col failed.")
            raise CustomException(e, sys)


    def step_04_cnt_child_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply MinMaxScaler on CNT_CHILDREN col.

        Args:
            df (pd.DataFrame): Dataset containing the CNT_CHILDREN col.

        Returns:
            pd.DataFrame: Dataset containing the scaled values of CNT_CHILDREN col.
        """
        logging.info('Inside step_04_cnt_child_column method')

        try:
            logging.info("Scaling of cnt chilren col started.")

            child_scaler = MinMaxScaler()

            child_scaler.fit(df[['CNT_CHILDREN']])

            df['CNT_CHILDREN'] = child_scaler.transform(df[['CNT_CHILDREN']])

            save_models(name = 'child_scaler.pkl',
                        path=self.path,
                        model=child_scaler)

            logging.info("Scaling of cnt chilren col Completed.")

            return df

        except Exception as e:
            logging.info("Scaling of cnt chilren col failed.")
            raise CustomException(e, sys)


    def step_06_income_type_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply OrdinalEncoder and MinMaxScaler on NAME_INCOME_TYPE col.

        Args:
            df (pd.DataFrame): Dataset containing the NAME_INCOME_TYPE col.

        Returns:
            pd.DataFrame: Dataset containing the scaled values of NAME_INCOME_TYPE col.
        """
        logging.info("Inside step_06_income_type_column method")

        try:
            logging.info("Encoding and scaling of income type col started.")

            category_order = [['Working', 'Commercial associate', 'State servant', 'Student',
                                'Pensioner']]

            income_type_encoder = OrdinalEncoder(categories = category_order)

            income_type_encoder.fit(df[['NAME_INCOME_TYPE']])

            df['NAME_INCOME_TYPE'] = income_type_encoder.transform(df[['NAME_INCOME_TYPE']])

            save_models(name = 'income_type_encoder.pkl',
                        path=self.path,
                        model=income_type_encoder)

            income_type_scaler = MinMaxScaler()

            income_type_scaler.fit(df[['NAME_INCOME_TYPE']])

            income_type_scaler.transform(df[['NAME_INCOME_TYPE']])

            save_models(name = 'income_type_scaler.pkl',
                        path=self.path,
                        model=income_type_scaler)

            logging.info("Encoding and scaling of income type col Completed.")

            return df

        except Exception as e:
            logging.info("Encoding and scaling of income type col failed.")
            raise CustomException(e, sys)


    def step_07_education_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply OrdinalEncoder and MinMaxScaler on NAME_EDUCATION_TYPE col.

        Args:
            df (pd.DataFrame): Dataset containing NAME_EDUCATION_TYPE col.

        Returns:
            pd.DataFrame: Dataset containing the scaled values of NAME_EDUCATION_TYPE col.
        """
        logging.info('Inside step_07_education_column method.')

        try:
            logging.info("Encoding and scaling of education col started.")

            education_order = [['Lower secondary', 'Secondary / secondary special', 'Incomplete higher', 'Higher education', 'Academic degree']]

            education_order_encoder = OrdinalEncoder(categories = education_order)

            education_order_encoder.fit(df[['NAME_EDUCATION_TYPE']])

            df['NAME_EDUCATION_TYPE'] = education_order_encoder.transform(df[['NAME_EDUCATION_TYPE']])

            save_models(name = 'education_order_encoder.pkl',
                        path=self.path,
                        model=education_order_encoder)

            education_scaler = MinMaxScaler()

            education_scaler.fit(df[['NAME_EDUCATION_TYPE']])

            df['NAME_EDUCATION_TYPE'] = education_scaler.transform(df[['NAME_EDUCATION_TYPE']])

            save_models(name = 'education_scaler.pkl',
                        path=self.path,
                        model=education_scaler)

            logging.info("Encoding and scaling of education col Completed.")

            return df

        except Exception as e:
            logging.info("Encoding and scaling of education col failed.")
            raise CustomException(e, sys)


    def step_08_Housing_type_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """_summary_

        Args:
            df (pd.DataFrame): _description_

        Raises:
            CustomException: _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info('Inside step_08_Housing_type_column method.')

        try:
            logging.info("Encoding of housing type col started.")

            housing_encoder = OneHotEncoder(drop = 'first',
                               sparse_output=False,
                               handle_unknown='ignore')

            housing_encoder.fit(df[['NAME_HOUSING_TYPE']])

            housing_encoder.transform(df[['NAME_HOUSING_TYPE']])

            feature_names = housing_encoder.get_feature_names_out()

            feature_names = [name.split("_")[-1] for name in feature_names]

            Rental_apar_df = pd.DataFrame(housing_encoder.transform(df[['NAME_HOUSING_TYPE']]), columns = feature_names)

            df2 = pd.concat([df,Rental_apar_df], axis = 'columns')

            df3 = df2.drop(['NAME_HOUSING_TYPE'], axis = 'columns')

            save_models(name = 'housing_encoder.pkl',
                        path=self.path,
                        model=housing_encoder)

            logging.info("Encoding of housing type col completed.")

            return df3

        except Exception as e:
            logging.info("Encoding of housing type col failed.")
            raise CustomException(e, sys)


    def step_09_Fam_Member_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply MinMaxScaler on CNT_FAM_MEMBERS cols.

        Args:
            df (pd.DataFrame): Dataset containing CNT_FAM_MEMBERS col.

        Returns:
            pd.DataFrame: Dataset containing scaled values of CNT_FAM_MEMBERS col.
        """
        logging.info("Inside step_09_Fam_Member_column method.")

        try:
            logging.info("Scaling of fam member col failed.")

            fam_mem_scaler = MinMaxScaler()

            fam_mem_scaler.fit(df[['CNT_FAM_MEMBERS']])

            df['CNT_FAM_MEMBERS'] = fam_mem_scaler.transform(df[['CNT_FAM_MEMBERS']])

            save_models(name = 'fam_mem_scaler.pkl',
                        path=self.path,
                        model=fam_mem_scaler)

            logging.info("Scaling of fam member col failed.")

            return df

        except Exception as e:
            logging.info("Scaling of fam member col failed.")
            raise CustomException(e, sys)


    def step_10_status_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply OrdinalEncoder and MinMaxScaler on STATUS col.

        Args:
            df (pd.DataFrame): Dataset containing the STATUS col.

        Returns:
            pd.DataFrame: Dataset containing the scaled values of STATUS col.
        """
        logging.info('Inside step_10_status_column col.')

        try:
            logging.info("Encoding and scaling of status col started.")

            status = df['STATUS'].to_list()

            new_status = []

            for i in status:
                if  i == '0' or i == '1':
                    new_status.append('<60')

                elif i == '2' or i == '3' or  i == '4':
                    new_status.append('60-150')

                elif i == '5':
                    new_status.append('B')

                else:
                    new_status.append(i)

            df['STATUS'] = new_status

            category_order = [['X', 'C', '<60', '60-150', 'B']]

            status_encoder = OrdinalEncoder(categories = category_order)

            status_encoder.fit(df[['STATUS']])

            df[['STATUS']] = status_encoder.transform(df[['STATUS']])

            save_models(name = 'status_encoder.pkl',
                        path=self.path,
                        model=status_encoder)

            status_scaler = MinMaxScaler()

            status_scaler.fit(df[['STATUS']])

            df['STATUS'] = status_scaler.transform(df[['STATUS']])

            save_models(name = 'status_scaler.pkl',
                        path=self.path,
                        model=status_scaler)

            logging.info("Encoding and scaling of status col Completed.")

            return df

        except Exception as e:
            logging.info("Encoding and scaling of status col failed.")
            raise CustomException(e, sys)


    def step_11_target_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply OneHotEncoder on TARGET col.

        Args:
            df (pd.DataFrame): Dataset containing the TARGET col.

        Returns:
            pd.DataFrame: Dataset containing the encoded values of TARGET col.
        """
        logging.info('Inside step_11_target_column method.')

        try:
            logging.info("Encoding of target col started.")

            target_encoder = OneHotEncoder(drop = 'first',
                               sparse_output=False,
                               handle_unknown='ignore')

            target_encoder.fit(df[['TARGET']])

            df['TARGET'] = target_encoder.transform(df[['TARGET']])

            save_models(name = 'target_encoder.pkl',
                        path=self.path,
                        model=target_encoder)

            logging.info("Encoding of target col failed.")

            return df

        except Exception as e:
            logging.info("Encoding of target col failed.")
            raise CustomException(e, sys)


    def step_12_Age_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply MinMaxScaler on AGE col.

        Args:
            df (pd.DataFrame): Dataset containing the AGE col.

        Returns:
            pd.DataFrame: Dataset with scaled values of AGE col.
        """
        logging.info('Inside step_12_Age_column method')

        try:
            logging.info("scaling of age col failed.")

            age_scaler = MinMaxScaler()

            age_scaler.fit(df[['AGE']])

            df['AGE'] = age_scaler.transform(df[['AGE']])

            save_models(name = 'age_scaler.pkl',
                        path=self.path,
                        model=age_scaler)

            logging.info("scaling of age col failed.")

            return df

        except Exception as e:
            logging.info("scaling of age col failed.")
            raise CustomException(e, sys)


    def step_13_Employ_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply MinMaxScaler on YR_EMPLOYEED col.

        Args:
            df (pd.DataFrame): Dataset containing the YR_EMPLOYEED col.

        Returns:
            pd.DataFrame: Dataset with scaled values of YR_EMPLOYEED col.
        """
        logging.info("Inside step_13_Employ_column method")

        try:
            logging.info("scaling of employeed col started.")

            employ_scaler = MinMaxScaler()

            employ_scaler.fit(df[['YR_EMPLOYEED']])

            df['YR_EMPLOYEED'] = employ_scaler.transform(df[['YR_EMPLOYEED']])

            save_models(name = 'employ_scaler.pkl',
                        path=self.path,
                        model=employ_scaler)

            logging.info("scaling of employeed col completed.")

            return df

        except Exception as e:
            logging.info("scaling of employeed col failed.")
            raise CustomException(e, sys)


    def step_14_Occ_column(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        This method will apply OrdinalEncoder and MinMaxScaler on NEW_OCC_COL col.

        Args:
            df (pd.DataFrame): Dataset containing the NEW_OCC_COL col.

        Returns:
            pd.DataFrame: Dataset containing the scaled values of NEW_OCC_COL col.
        """
        logging.info("Inside step_14_Occ_column method.")

        try:
            logging.info("Encoding and scaling of occupation col started.")

            category_order = [['Finance and Accounting', 'Technical and IT', 'Healthcare', 'Administrative and Management', 'Customer Service and Hospitality', 'Transportation and Logistics', 'Support and Services', 'Labor and Maintenance']]

            occu_type_encoder = OrdinalEncoder(categories = category_order)

            occu_type_encoder.fit(df[['NEW_OCC_COL']])

            df['NEW_OCC_COL'] = occu_type_encoder.transform(df[['NEW_OCC_COL']])

            save_models(name = 'occu_type_encoder.pkl',
                        path=self.path,
                        model=occu_type_encoder)

            occu_type_scaler = MinMaxScaler()

            occu_type_scaler.fit(df[['NEW_OCC_COL']])

            df['NEW_OCC_COL'] = occu_type_scaler.transform(df[['NEW_OCC_COL']])

            save_models(name = 'occu_type_scaler.pkl',
                        path=self.path,
                        model=occu_type_scaler)

            logging.info("Encoding and scaling of occupation col Completed.")

            return df

        except Exception as e:
            logging.info("Encoding and scaling of occupation col failed.")
            raise CustomException(e, sys)


