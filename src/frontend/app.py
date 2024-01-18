import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
PREDICT_URL = "http://localhost:8000/predict"


st.header("Energie Classification")
# Text area for the user to enter their text

annee_construction = st.number_input("annee_construction", min_value=0, max_value=100000, value=0)
surface_thermique_lot = st.number_input("surface_thermique_lot", min_value=0, max_value=100000, value=0)
code_insee_commune_actualise = st.number_input("code_insee_commune_actualise", min_value=0, max_value=100000, value=0)

type_dpe = st.selectbox("type_dpe", ["batiment_public", "copropriete", "location", "neuf", "vente"])
type_batiment = st.selectbox("type_batiment", ["batiment_collectif", "logement", "maison_individuelle"])

data_type_dpe = {"batiment_public": 0, "copropriete": 0, "location": 0, "neuf": 0, "vente": 0}
data_type_batiment = {"batiment_collectif": 0, "logement": 0, "maison_individuelle": 0}
data_type_dpe[type_dpe] = 1
data_type_batiment[type_batiment] = 1

data = {
    "annee_construction": annee_construction,
    "surface_thermique_lot": surface_thermique_lot,
    "code_insee_commune_actualise": code_insee_commune_actualise,
    **data_type_dpe,
    **data_type_batiment
}

if st.button("Predict"):

    response = requests.post(PREDICT_URL, json=data)
    if response.status_code == 200:
        result = response.json()["Classe consomation energie"]

        st.success(f"Classe consomation energie: {result}")

    else:

        st.error("Error: Unable to process request")

