import requests
from pprint import pprint
import json 
import os
import glob
import pandas as pd




def reading_jsonfiles_append(products:dict,folder: str) -> pd.DataFrame:

    # processing files 
    for i in range(0,len(products),size_process):
        chunk = products[i:i + size_process] # productos de 10 en 10 
        nome_arquivo = f"data/products_{i//size_process+1}.json" # creating json files from information before readed
        # writing json file information
        with open(nome_arquivo, 'w',encoding='utf-8') as f:
            json.dump(chunk,f,indent=4,ensure_ascii=False)

    
    files = glob.glob(os.path.join(folder,"products*.json")) # list with all json files from a specific path
    dataframes = [pd.read_json(file) for file in files]
    df_concat = pd.concat(dataframes,ignore_index=True)
    
    return df_concat











if __name__ == "__main__":
    try:
        url = 'https://dummyjson.com/products'
        response= requests.get(url)
        data = response.json()
        
    except Exception as e:
        print(f" Error {e}")

    # creating data folder if doesnt exist
    os.makedirs("data", exist_ok=True)
    # taking only products from json response
    products :dict= data['products']
    # process size 
    size_process :int = 10


    folder = "data"
    df_append = reading_jsonfiles_append(products,folder)
    print(df_append.columns)


