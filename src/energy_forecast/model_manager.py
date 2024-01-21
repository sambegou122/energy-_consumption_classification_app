
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
        return prediction.tolist()
    

    def retrain(self, training_set)-> int:
        """Retrain the model."""

        print("loading training data...")
        try : 
            df = pd.read_csv(training_set, delimiter=',')

            y = self.encoder.transform(df['classe_consommation_energie'])
            
            print("transforming training data...")
            x = df.drop(['classe_consommation_energie'], axis=1)
            x = Dataloader().transform(x)
            index= x.index
            y= y[index]

            print("model training...")
            print(x.shape)

            self.model.fit(x, y)

            print("model trained")
        
            score = self.model.score(x, y)
        
          

        except Exception as e:

            print(f"Error : {e}")
            score = 0

        return score