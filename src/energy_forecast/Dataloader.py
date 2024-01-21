import os
import requests
import pandas as pd
from dotenv import load_dotenv
import io
import time
from tqdm import tqdm

import re



class Dataloader:

    def __init__(self, size=10000):
        load_dotenv()
        self.base_url = os.getenv("URL")
        self.dir = os.getenv("DATA_DIR")
        self.size = size


    def download_csv(self):
        url = self.base_url
        data = pd.DataFrame()
        T = 0
        print("Downloading data progess ...")
        progess = tqdm(total=self.size)
        
        while T < self.size:
            try:
                
                response = requests.get(url)

                if response.status_code == 200:
                    content = response.content
                    energy = pd.read_csv(io.StringIO(content.decode('utf-8')), delimiter=',')
                    data = pd.concat([data, energy])
                    T = data.shape[0]
                    next = response.links['next']['url']
                    if next is not None:
                        url = next
                    else:
                        break
                else:
                    print("Erreur lors de la récupération des données")
                    break
                progess.update(T)
            except Exception as e:
                print(f"Erreur : {e}")
                time.sleep(5)
                continue

        filename = self.dir
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    
    def set_data_path(self, path):
        self.dir = path


    def load_csv(self):

        filename = self.dir
        return pd.read_csv(filename, delimiter=",")
    
    def transform(self, df):

        assert isinstance(df, pd.DataFrame), "df must be a pandas dataframe"
    

        columns_keep = ["annee_construction", "code_insee_commune_actualise", "surface_thermique_lot",
                "tr001_modele_dpe_type_libelle", "tr002_type_batiment_description"]
        
        assert all([i in df.columns for i in columns_keep]), "df must have the following columns: annee_construction, code_insee_commune_actualise, surface_thermique_lot, tr001_modele_dpe_type_libelle, tr002_type_batiment_description"


        df = df[columns_keep]

        
        df["code_insee_commune_actualise"] = (
            df["code_insee_commune_actualise"].\
                apply(lambda x: float(re.sub('[^0-9]', '', str(x))) if re.sub('[^0-9]', '', str(x)) else 0)
        )

        df = df.drop_duplicates()

        df.fillna(0, inplace=True)

        df = df.reindex(sorted(df.columns), axis=1)

        df = pd.get_dummies(df)

        return df



if __name__ == "__main__":
    # dl = Dataloader(size=100000)
    # dl.download_csv()
    dl = Dataloader()
    df = dl.load_csv()
    print(df.head())
    print(df.shape)
   