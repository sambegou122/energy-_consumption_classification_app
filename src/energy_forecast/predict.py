import click
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from energy_forecast.Dataloader import Dataloader
from energy_forecast.model_manager import ModelManager

@click.option("--training_set", default="data/training_set.csv", help="Path to the training set")
@click.option("--model", default="model/model.pkl", help="Path to the model")
@click.option("--data", default="data/data.csv", help="Path to the data")