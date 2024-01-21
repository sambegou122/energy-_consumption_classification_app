from fastapi import FastAPI
from pydantic import BaseModel
from energy_forecast.model_manager import ModelManager
import pandas as pd
import os
from dotenv import load_dotenv
import logging
import uvicorn
import pickle
import numpy as np



load_dotenv(override=True)
print(os.getenv("MODEL_DIR"))
with open(os.getenv("MODEL_DIR"), 'rb') as f:
    model = pickle.load(f)

with open(os.getenv("ENCODER_DIR"), 'rb') as f:
    encoder = pickle.load(f)
training_set = os.getenv("DATA_DIR")

model_manager = ModelManager(model, encoder, training_set)


app=FastAPI(title="Energie Classification", version="1")

class PredictInput(BaseModel):
    annee_construction: int
    surface_thermique_lot: int
    code_insee_commune_actualise: int
    batiment_public: int
    copropriete: int
    location: int
    neuf: int
    vente: int
    batiment_collectif: int
    logement: int
    maison_individuelle: int



@app.get("/")
async def root():
    return "This Energie Classification API Go to /docs for documentation"

@app.post("/predict")
async def predict(input:PredictInput):
    """
    Predict class of energy consumption

    **return**: prediction

    """
    try:
       
        # Your prediction code here
       columns = ['annee_construction', 'code_insee_commune_actualise',
       'surface_thermique_lot',
       'tr001_modele_dpe_type_libelle_Bâtiment public',
       'tr001_modele_dpe_type_libelle_Copropriété',
       'tr001_modele_dpe_type_libelle_Location',
       'tr001_modele_dpe_type_libelle_Neuf',
       'tr001_modele_dpe_type_libelle_Vente',
       "tr002_type_batiment_description_Bâtiment collectif à usage principal d'habitation",
       'tr002_type_batiment_description_Logement',
       'tr002_type_batiment_description_Maison Individuelle'
       ]
       
       data = input.model_dump()

       df = pd.DataFrame(data, index=[0])
       df.columns = columns

       logging.info(df)

       predictions = model_manager.predict(df)
       
       return {"Classe consomation energie": ' '.join(predictions)}
    
    except Exception as e:

        logging.error(e)

        raise e
    


if __name__=="__main__":

    uvicorn.run(app, host="localhost", port=8000)
