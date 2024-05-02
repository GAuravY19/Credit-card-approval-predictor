import os
import pickle

import numpy as np
import torch
import torch.nn as nn

from src.main_src.base_model import ModelV2

AGE_PATH = "D:/Credit-card-approval-predictor/artifacts/age_scaler.pkl"
REALTY_PATH = r'D:\Credit-card-approval-predictor\artifacts\realty.pkl'
CNT_CHILD_PATH = r'D:\Credit-card-approval-predictor\artifacts\child_scaler.pkl'
INCOME_PATH = r'D:\Credit-card-approval-predictor\artifacts\annual_amt_scaler.pkl'
INCOME_TYPE_ENCODER_PATH = r'D:\Credit-card-approval-predictor\artifacts\income_type_encoder.pkl'
INCOME_TYPE_SCALER_PATH = r'D:\Credit-card-approval-predictor\artifacts\income_type_scaler.pkl'
EDUCATION_ENCODER_PATH = r'D:\Credit-card-approval-predictor\artifacts\education_order_encoder.pkl'
EDUCATION_SCALER_PATH = r'D:\Credit-card-approval-predictor\artifacts\education_scaler.pkl'
MEMBER_PATH = r'D:\Credit-card-approval-predictor\artifacts\fam_mem_scaler.pkl'
OVERDUES_ENCODER_PATH = r'D:\Credit-card-approval-predictor\artifacts\status_encoder.pkl'
OVERDUES_SCALER_PATH = r'D:\Credit-card-approval-predictor\artifacts\status_scaler.pkl'
EMPLOYMENT_PATH = r'D:\Credit-card-approval-predictor\artifacts\employ_scaler.pkl'
OCCUPATION_ENCODER_PATH = r'D:\Credit-card-approval-predictor\artifacts\occu_type_encoder.pkl'
OCCUPATION_SCALER_PATH = r'D:\Credit-card-approval-predictor\artifacts\occu_type_scaler.pkl'
HOUSE_PATH = r'D:\Credit-card-approval-predictor\artifacts\housing_encoder.pkl'
PCA_PATH = r'D:\Credit-card-approval-predictor\artifacts\pca.pkl'
MODEL_PATH = r'D:\Credit-card-approval-predictor\artifacts\model\pytorchneural.pth'
# loading artifacts required for making predictions
def OpenPklFiles(path:str):
    with open(path, 'rb') as f:
        name = pickle.load(f)

    return name


try:
    AGE_PKL = OpenPklFiles(AGE_PATH)
    REALTY_PKL = OpenPklFiles(REALTY_PATH)
    CNT_CHILD_PKL = OpenPklFiles(CNT_CHILD_PATH)
    INCOME_PKL = OpenPklFiles(INCOME_PATH)
    INCOME_TYPE_ENCODER_PKL = OpenPklFiles(INCOME_TYPE_ENCODER_PATH)
    INCOME_TYPE_SCALER_PKL = OpenPklFiles(INCOME_TYPE_SCALER_PATH)
    EDUCATION_ENCODER_PKL = OpenPklFiles(EDUCATION_ENCODER_PATH)
    EDUCATION_SCALER_PKL = OpenPklFiles(EDUCATION_SCALER_PATH)
    MEMBER_PKL = OpenPklFiles(MEMBER_PATH)
    OVERDUES_ENCODER_PKL = OpenPklFiles(OVERDUES_ENCODER_PATH)
    OVERDUES_SCALER_PKL = OpenPklFiles(OVERDUES_SCALER_PATH)
    EMPLOYMENT_PKL = OpenPklFiles(EMPLOYMENT_PATH)
    OCCUPATION_ENCODER_PKL = OpenPklFiles(OCCUPATION_ENCODER_PATH)
    OCCUPATION_SCALER_PKL = OpenPklFiles(OCCUPATION_SCALER_PATH)
    PCA_PKL = OpenPklFiles(PCA_PATH)

except:
    print("The file does not ran successfully.")


def MakePredictions(AGE:int, REALTY:str, CNT_CHILD:int, INCOME:int, INCOME_TYPE:str, EDUCATION:str, MEMBER:int, OVERDUES:str,
                    EMPLOYMENT:int, OCCUPATION:str, HOUSE:str):

    scaled_age = AGE_PKL.transform([[AGE]])
    scaled_realty = REALTY_PKL.transform([[REALTY]])
    scaled_child = CNT_CHILD_PKL.transform([[CNT_CHILD]])
    scaled_income = INCOME_PKL.transform([[INCOME]])

    scaled_income_type_encoded = INCOME_TYPE_ENCODER_PKL.transform([[INCOME_TYPE]])
    scaled_income_type = INCOME_TYPE_SCALER_PKL.transform(scaled_income_type_encoded)

    scaled_education_encoded = EDUCATION_ENCODER_PKL.transform([[EDUCATION]])
    scaled_education = EDUCATION_SCALER_PKL.transform(scaled_education_encoded)

    scaled_member = MEMBER_PKL.transform([[MEMBER]])

    scaled_overdues_encoded = OVERDUES_ENCODER_PKL.transform([[OVERDUES]])
    scaled_overdues = OVERDUES_SCALER_PKL.transform(scaled_overdues_encoded)

    scaled_employment = EMPLOYMENT_PKL.transform([[EMPLOYMENT]])

    scaled_occupation_encoded = OCCUPATION_ENCODER_PKL.transform([[OCCUPATION]])
    scaled_occupation = OCCUPATION_SCALER_PKL.transform(scaled_occupation_encoded)

    House = ['House / apartment', 'Rented apartment', 'Municipal apartment',
             'With parents', 'Co-op apartment', 'Office apartment']

    house_idx = House.index(HOUSE)

    x = np.zeros(16)

    x[0] = scaled_realty
    x[1] = scaled_child
    x[2] = scaled_income
    x[3] = scaled_income
    x[4] = scaled_education
    x[5] = scaled_member
    x[6] = scaled_overdues
    x[7] = scaled_age
    x[8] = scaled_employment
    x[9] = scaled_occupation
    x[house_idx + 10] = 1
    x = PCA_PKL.transform([x])

    model = ModelV2()
    model.load_state_dict(torch.load(MODEL_PATH))
    # print("Model load ho gaya")


    tensor_x = torch.from_numpy(x).type(dtype=torch.float32)

    model.eval()
    with torch.inference_mode():
        output = model(tensor_x).squeeze()

        output = torch.round(torch.sigmoid(output))

    return output.item()













if __name__ == "__main__":
    MakePredictions(45, 'Yes', 4, 84000, 'Working', 'Incomplete higher', 3, 'C', 4, 'Healthcare', 'Office apartment')



