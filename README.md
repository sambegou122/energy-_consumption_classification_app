# BG PROJETC

## Description

This project is the simple implementation of an app that can predict the energy consumption of a building based on the open data of energie consumptionpof the gouvernement of france.

This project is composed of tree parts:

- The first part is the data processing part, it is the part where we downlead the data from the API, clean the data and we prepare it for the training of the model.

- The second part is the API part, it is the part where we create the API that will be used to make the prediction.

- The part is the web app part, it web application that will be used to make the prediction.

The data used in this project is the data of the energy consumption of the gouvernement of france. The data is available on the API of the gouvernement of france at this link: https://data.ademe.fr/data-fair/api/v1/datasets/dpe-france/lines?format=csv

## Project structure

```
.
├── src
│   ├── data
│   ├── models
│   │── DataLoader.py
│   │── model_manager.py
│   │── predict.py
│   │── train.py
│   ├── WebApp
│   │   ├── app.py
│   ├── FrontEnd
│   │   ├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
├── notebooks
```

## Installation
Use the requirements.txt file to install the dependencies.

```bash 
pip install -r requirements.txt
```

## Notebooks
The notebooks folder contains the notebooks that we used to explore the data and to train the model.

## Data
The data folder contains the data that we used to train the model

## Models
The models folder contains the models that we used to make the prediction and the classe encoder that we used to encode the categorical features.

## WebApp
The WebApp folder contains the web API that we used to make the prediction.

## FrontEnd
The FrontEnd folder contains the web application that we used to make the prediction.

## Usage
To use the API you need to run the app.py file in the WebApp folder.

```bash
python app.py
```

To use the web application you need to run the app.py file in the FrontEnd folder. But before you need to run the app.py file in the WebApp folder like we said before.

```bash
streamlit run app.py
```

## Author
- [Ibrahima sambegou Diallo]
