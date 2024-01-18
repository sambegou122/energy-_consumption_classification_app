from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
from energy_forecast.Dataloader import Dataloader
from energy_forecast.model_manager import ModelManager
import click
load_dotenv()
model = os.getenv("MODEL_DIR")
training_set = os.getenv("DATA_DIR")
encoder = os.getenv("ENCODER_DIR")



def retrain(training_set, model, encoder):
    """Retrain the model."""

    model = pd.read_pickle(model)
    encoder = pd.read_pickle(encoder)
    model_manager = ModelManager(model, encoder, training_set)
    score = model_manager.retrain(training_set)

    print(f"Model score: {score}")






if __name__ == '__main__':

    retrain()


