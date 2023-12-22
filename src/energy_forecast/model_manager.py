
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from energy_forecast.Dataloader import Dataloader

class ModelManager():

    def __init__(self, model, data) -> None:
        self.model = model
        self.data = data

    def predict(self)-> str:
        """Predict the sentiment of the input text."""
        prediction = self.model.predict(self.data)
        return prediction
    

    def retrain(self, training_set)-> int:
        """Retrain the model."""
        
        df = pd.read_csv(training_set, delimiter=',')
        
        assert list(df.columns) == ['review', 'polarity'], f"Expected columns: ['review', 'polarity'], but got {df.columns}"
        df = Dataloader().transform(df)
        print("model training...")
        self.model.fit(df)
        print("model trained")
        columns_to_drop = ['review', 'polarity']
        x = df.drop(columns_to_drop, axis=1)
        predictions = self.model.predict(x)
        score = accuracy_score(df['polarity'], predictions)
        print(f"Model accuracy: {score}")
        return score