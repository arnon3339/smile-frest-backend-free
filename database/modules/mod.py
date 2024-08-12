from ntpath import join
from sys import modules
from xml.dom.minidom import Document
import motor.motor_asyncio
import json
# from modules.exel2db import write_json
from modules.exel2db import get_data_from_xlsx
import random
import string
import asyncio
from modules.json2col import gen_coll, gen_quiz
import pprint
import bson.json_util as json_util
import string
import random
import dotenv

config = dotenv.dotenv_values("../.env")
client = motor.motor_asyncio.\
    AsyncIOMotorClient(f"mongodb+srv://{config["DBUSER"]}:{config["DBPW"]}@{config["DBSTRING"]}?retryWrites=true&w=majority&appName={config["DBCLUSTER"]}")
database = client.get_default_database()
collection_question = database.question
collection_questions = database.questions
collection_users = database.users

async def insert_question_to_db(xlsx_f):
    data = get_data_from_xlsx(xlsx_f)
    await collection_question.insert_many(data)

async def clear_question_to_db():
    await collection_question.delete_many({})

async def clear_questions_to_db():
    await collection_questions.delete_many({})

async def clear_users_to_db():
    await collection_users.delete_many({})

# new_db = client

# def create_qadb():
#     write_json(mod=True)
#     with open('./database/QA.json', 'r') as f:
#         document = json.load(f)
#     collection_quiz.insert_many(document)
    
async def get_collections(database):
    colls = await database.list_collections()
    async for c in colls:
        print(c)
