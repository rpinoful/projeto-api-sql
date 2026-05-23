import requests
from pprint import pprint
import json 
import os
import glob
import pandas as pd

# api request with the content save in memory
try:
    url = 'https://dummyjson.com/products'
    response= requests.get(url)
    data = response.json()
    
except Exception as e:
    print(f" Error {e}")

os.makedirs("data", exist_ok=True)
products :dict= data['products']
size_process :int = 10

for i in range(0,len(products),size_process):
    chunk = products[i:i + size_process] # productos de 10 en 10 
    nome_arquivo = f"data/products_{i//size_process+1}.json"

    with open(nome_arquivo, 'w',encoding='utf-8') as f:
        json.dump(chunk,f,indent=4,ensure_ascii=False)



def reading_jsonfiles_append(folder: str) -> pd.DataFrame:
    files = glob.glob(os.path.join(folder,"products*.json"))
    for file in files:
        print(file)





if __name__ == "__main__":
    folder = "data"
    df_append = reading_jsonfiles_append(folder)

