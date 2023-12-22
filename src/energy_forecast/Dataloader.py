import os
import requests
import pandas as pd
from dotenv import load_dotenv
import io
load_dotenv()


class Dataloader:

    def __init__(self, shape=10000):
        self.base_url = os.getenv("URL")
        self.dir = os.getenv("DATA_DIR")
        self.shape = shape


    def download_csv(self):
        url = self.base_url
        data = pd.DataFrame()
        T = 0
        print("Downloading data...")
        while T < self.shape:
    
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

        filename = self.dir
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")


    def load_csv(self):
        filename = self.dir
        return pd.read_csv(filename, delimiter=",")


if __name__ == "__main__":
    dl = Dataloader()
    df = dl.load_csv()
    print(df.head())
    print(df.shape)
   