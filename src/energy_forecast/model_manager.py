
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from energy_forecast.Dataloader import Dataloader
from sklearn.pipeline import Pipeline
import pickle
import xgboost as xgb

class ModelManager():

    def __init__(self, model, encoder, data) -> None:
        self.model = model
        self.encoder = encoder
        self.data = data

    def predict(self, x)-> list:
        """Predict the sentiment of the input text."""
        prediction = self.model.predict(x)
        prediction = self.encoder.inverse_transform(prediction)
        return prediction
    

    def retrain(self, training_set)-> int:
        """Retrain the model."""

        print("loading training data...")
        df = pd.read_csv(training_set, delimiter=',')
        
        print("transforming training data...")
        df = Dataloader().transform(df)

        print("model training...")
        
        y = self.encoder.transform(df['classe_consommation_energie'])
        x = pd.get_dummies(df.drop(['classe_consommation_energie'], axis=1))

        self.model.fit(x,y) 

        print("model trained")
      
        score = self.model.score(x, y)
      
        print(f"Model score: {score}")

        return score