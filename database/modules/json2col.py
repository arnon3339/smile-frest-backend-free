from importlib.resources import path
import json
import pandas as pd
import string
import random

def gen_quiz():
    data = []
    qas = pd.read_excel(r'./database/quiz_yipf.xlsx')
    for index, value in qas.iterrows():
        data.append({"no": index, 
            "question": value["Question"], "options": [
            value["Choice1"], value["Choice2"], value["Choice3"], value["Choice4"]
        ],
            "correct":int(value["Correct"]) - 1
        })
        # print(value)
    return data


def gen_paths():
    chs = string.ascii_letters + string.digits
    paths = []
    for i in range(2000):
        path = ''.join(random.choice(chs) for i in range(20))
        if not path.lower() in [paths[i].lower() for i in range(len(paths))]:
            paths.append(path)
    return paths

def gen_coll():
    paths = gen_paths()
    quizs = gen_quiz()
    data = [{"no": i, "path": paths[i], 
             "quizs": [quizs[j] for j in random.sample(range(len(quizs)), 3)]}
            for i in range(len(paths))]    
    with open("./database/json_data.json", 'w') as f:
        json.dump(data, f)
    return data