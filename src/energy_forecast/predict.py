import click
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from energy_forecast.Dataloader import Dataloader
from energy_forecast.model_manager import ModelManager
from dotenv import load_dotenv
import click
import os
load_dotenv()

model = os.getenv("MODEL_DIR")
training_set = os.getenv("DATA_DIR")
encoder = os.getenv("ENCODER_DIR")

@click.command()
@click.option('--predict_set', default='data.csv', help='Path to training data.')


def predict(predict_set):
    """Predict the sentiment of the input text."""
    model = pd.read_pickle(model)
    encoder = pd.read_pickle(encoder)
    model_manager = ModelManager(model, encoder, none)
    prediction = model_manager.predict(predict_set)
    
    return prediction


if __name__ == '__main__':
    predict()