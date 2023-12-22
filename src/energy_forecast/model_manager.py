
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score


class ModelManager():

    def __init__(self, model, text, file, output_file) -> None:
        self.model = model
        self.text = text
        self.file = file
        self.output_file = output_file


    def predict(self)-> str:
        """Predict the sentiment of the input text."""

        if self.text is not None:
            df = [self.text]
        else:
            df = pd.read_csv(self.file)
            assert list(df.columns) == ['review'], f"Expected columns: ['review'], but got {df.columns}"

        predictions = self.model.predict(df)

        if self.text:
            return str(predictions[0])
        else:
            df['prediction'] = predictions
            df.to_csv(self.output_file, index=False)
            print(f"Predictions saved to {self.output_file}")
            return "Predictions saved to {self.output_file}"
    

    def retrain(self, training_set)-> int:
        """Retrain the model."""
        
        df = pd.read_csv(training_set, delimiter=',')
        df.drop(['Unnamed: 0', "film-url"], axis=1, inplace=True)
        assert list(df.columns) == ['review', 'polarity'], f"Expected columns: ['review', 'polarity'], but got {df.columns}"
        print(f"Retraining model with {len(df)} examples")
        print("model training...")
        self.model.fit(df['review'], df['polarity'])
        print("model trained")
        predictions = self.model.predict(df['review'])
        score = accuracy_score(df['polarity'], predictions)
        print(f"Model accuracy: {score}")
        return score