# import modules
import motor.motor_asyncio
import qrcode
from PIL import Image, ImageDraw
import asyncio
import json
import os, shutil, sys
from os import path
import dotenv
import motor
import random
from motor import motor_asyncio

random.seed(12345)

config = dotenv.dotenv_values("./.env")
 
# taking image which user wants
# in the QR code center
Logo_link = './orig_logo.JPG'
 
logo = Image.open(Logo_link)
 
# taking base width
basewidth = 200
 
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), resample=Image.Resampling.LANCZOS)

def create_circular_mask(image_size, radius):
    mask = Image.new("L", image_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    return mask

async def get_data(client: motor.motor_asyncio.AsyncIOMotorClient, q_ids):
    database = client.get_default_database()
    collection_questions = database.questions
    rnd_question = random.sample(q_ids, 3)
    new_questions = await collection_questions.insert_one({
        "active": True,
        "questions": rnd_question,
        "rndchoices": [random.sample(range(4), 4) for i in range(3)]
    })
    if new_questions.acknowledged:
        return new_questions.inserted_id
    return False
    
def clear_images():
    folder = './images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

async def get_qids(client):
    database = client.get_default_database()
    collection_question = database.question
    cursor = collection_question.find({}, '_id')
    data = []
    async for q_id in cursor:
        data.append(str(q_id['_id']))
    return data
 
async def gen_qrcode(num):
    client = motor_asyncio.\
        AsyncIOMotorClient(f"mongodb+srv://{config["DBUSER"]}:{config["DBPW"]}@{config["DBSTRING"]}?retryWrites=true&w=majority&appName={config["DBCLUSTER"]}")
    q_ids = await get_qids(client)
    clear_images()
    for i in range(int(num)):
        data = await get_data(client, q_ids)
        if not data:
            continue
        QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        # adding URL or text to QRcode
        qr_path = config["NEXTAUTH_URL"] + f"/?q={data}"
        QRcode.add_data(qr_path)
        
        # generating QR code
        QRcode.make()
        # qr.add_data(data)
        QRcode.make(fit=True)
        
        # taking color name from user
        QRcolor = 'Black'
        
        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="white").convert('RGB')
        
        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
            (QRimg.size[1] - logo.size[1]) // 2)

        mask = create_circular_mask(logo.size, logo.size[0]// 2)

        QRimg.paste(logo, pos, mask)

        # save the QR code generated
        QRimg.save(f'./images/{data}.png')
    client.close()

if __name__ == "__main__":
    try:
        asyncio.run(gen_qrcode(sys.argv[1]))
    except:
        asyncio.run(gen_qrcode(1000))