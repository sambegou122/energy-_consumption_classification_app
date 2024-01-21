from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
from energy_forecast.Dataloader import Dataloader
from energy_forecast.model_manager import ModelManager
import click
from xgboost import XGBClassifier
load_dotenv()



def retrain():
    """Retrain the model."""
    training_set = os.getenv("DATA_DIR")
    model = XGBClassifier()
    encoder = pd.read_pickle(os.getenv("ENCODER_DIR"))
    model_manager = ModelManager(model, encoder, training_set)
    score = model_manager.retrain(training_set)

    print(f"Model score: {score}")






if __name__ == '__main__':

    retrain()


