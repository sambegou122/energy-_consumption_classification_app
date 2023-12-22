from fastapi import FastAPI
from dotenv import load_dotenv
import pandas as pd

app = FastAPI()
load_dotenv()

@app.get("/predict")
def predict():
    return "Hello world"

@app.get("/retrain")
def retrain():
    return "Hello world"