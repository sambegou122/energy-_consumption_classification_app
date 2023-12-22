import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


class Dataloader:
    def __init__(self):
        self.url = os.getenv("URL")
        self.dir = os.getenv("DATA_DIR")

    def download_csv(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            filename = self.dir
            with open(filename, "wb") as file:
                file.write(response.content)
            print("CSV file downloaded and saved successfully.")
        else:
            print("Failed to download CSV file.")

    def load_csv(self):
        filename = self.dir
        return pd.read_csv(filename, delimiter=";")


if __name__ == "__main__":
    dl = Dataloader()
    dl.download_csv()
    df = dl.load_csv()
    print(df.head())