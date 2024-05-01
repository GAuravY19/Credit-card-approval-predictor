import pandas as pd

import pickle
import sys
import os

from .exceptions import CustomException
from .logger import logging


def calculate_yrs(days:int) -> int:
    years = (days / 365.25)

    years = abs(int(years))

    return years


def save_data(name:str, path:str, df:pd.DataFrame) -> None:
    try:
        df.to_csv(os.path.join(path, name),
                    index=False)

    except Exception as e:
        logging.info("Error occured in saving the model.")
        raise CustomException(e, sys)


def save_models(name:str, path:str, model) -> None:
    try:
        with open(os.path.join(path,name), 'wb') as f:
            pickle.dump(model, f)

    except Exception as e:
        raise CustomException(e, sys)

def load_models(path:str, name:str):
    try:
        with open(path, 'rb') as f:
            loaded_model = pickle.load(f)

        logging.info(f"Loading of {name} model completed.")

        return loaded_model

    except:
        logging.info(f"Loading of {name} model failed.")



