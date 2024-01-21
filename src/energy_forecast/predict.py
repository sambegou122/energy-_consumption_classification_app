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

# model = os.getenv("MODEL_DIR")
# training_set = os.getenv("DATA_DIR")
# encoder = os.getenv("ENCODER_DIR")

@click.command()
@click.option('--data_type', default='list', help='Type of data to load.')
@click.option('--predict_set',  required=True, help='Path to training data or list of features')


def predict(data_type, predict_set):
    """Predict the sentiment of the input text."""
    model = pd.read_pickle(os.getenv("MODEL_DIR"))
    encoder = pd.read_pickle(os.getenv("ENCODER_DIR"))
    training_set = os.getenv("DATA_DIR")
    model_manager = ModelManager(model, encoder, training_set)
    dataloader = Dataloader()

    if data_type == "list":

        predict_set = predict_set.split(" ")
        predict_set = [float(i) for i in predict_set]

        assert len(predict_set) == 11 , "The number of features must be 11"

        predict_set = np.array(predict_set).reshape(1, -1)
        prediction = model_manager.predict(predict_set)
        result = " ".join(prediction)
    else:
        predict_set = pd.read_csv(predict_set, delimiter=',')

        predict_set = dataloader.transform(predict_set)

        prediction = model_manager.predict(predict_set)

        result = " ".join(prediction)

    print(f"Classe de conssomation: {result}")
    


if __name__ == '__main__':
    predict()