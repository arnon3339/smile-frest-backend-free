import pandas as pd
from os import path
import json
import random

def get_data():
    data = []
    qas = pd.read_excel(r'./database/QA.xlsx')
    for index, value in qas.iterrows():
        data.append({"no": value["No"], 
            "question": value["Question"], "options": [
            value["Choice1"], value["Choice2"], value["Choice3"], value["Choice4"]
        ],
            "correct":int(value["Correct"]) - 1
        })
        # print(value)
    return data

def get_data_from_xlsx(xlsx_f):
    data = []
    qas = pd.read_excel(path.join("./", xlsx_f))
    for index, value in qas.iterrows():
        data.append({ 
            "question": value["Question"], "choices": [
            value["Choice1"], value["Choice2"], value["Choice3"], value["Choice4"]
        ],
            "correct":int(value["Correct"]) - 1
        })
        # print(value)
    return data

def write_xls():
    documents = []
    pd.read_json("./database/scoredf.json").to_excel("./database/outputdf.xlsx")
    pd.read_json("./database/scoref.json").to_excel("./database/outputf.xlsx")
    
# write_xls()