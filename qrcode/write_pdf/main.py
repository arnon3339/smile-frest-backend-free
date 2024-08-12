import PIL
from PIL import Image
import os
import math
from os import path
from PyPDF2 import PdfMerger
import numpy as np


w, h = 595, 842
# logo = r'../logo2.png'
# # img_logo_re = Image.open(logo).resize((28, 28), Image.Resampling.BILINEAR)

input_path = r'./input' 
output_path = r'./output'
imgs = os.listdir(input_path)
for i in range(math.ceil(len(imgs)/12)):
    a4im = Image.new('RGB', (w, h)
                    ,   # A4 at 72dpi
                    (255, 255, 255))  # White
    for j in range(i*12, (i*12 + 12)):
        if 12*i + j == len(imgs):
            break
        im = Image.open(path.join(input_path, imgs[i*12 + j]))
        img_re = im.resize((180, 180), Image.Resampling.BILINEAR)
        a4im.paste(img_re, (int((198/2)*[0.1, 2.1, 4.1][(j%12)%3]), 
                         int((205/2)*[0.2, 2.2, 4.2, 6.2][int((j%12)/3)])))  # Not centered, top-left corner
        # a4im.paste(img_logo_re, (int((198/2)*(np.array([0.86, 2.86, 4.86]))[(j%12)%3]), 
        #                  int((205/2)*(np.array([0.94, 2.94, 4.94, 6.94]))[int((j%12)/3)])))
    a4im.save(path.join(output_path, f'pdf{i}.pdf'),'PDF', quality=500)
    

pdfs = [path.join(output_path, i) for i in os.listdir(output_path)]
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("./result.pdf")
merger.close()