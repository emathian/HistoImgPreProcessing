import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import spams
import cv2
from PIL import Image
import utils
from vahadane import vahadane
from sklearn.manifold import TSNE
import os
import pandas as pd
import argparse

global inputdir
global outputdir


# df_LNEN = pd.read_csv('/home/mathiane/ImgProcessing/Data/Slides_LNEN_CIRC.csv')

directory_target   = '/home/mathiane/LNENWork/KI67_Tiling_256_256_40x/TNE1925.svs/accept'
TARGET_PATH_HE = directory_target  + '/TNE1925.svs_26113_9217.jpg'
# TARGET_PATH_HES = directory_target + '/TNE0952/'+'TNE0952_15733_17481.jpg'
target_imageHE = utils.read_image(TARGET_PATH_HE)


vhdHE = vahadane(STAIN_NUM=2, LAMBDA1=0.01, LAMBDA2=0.01, fast_mode=0, getH_mode=0, ITER=50)
vhdHE.fast_mode=0;
vhdHE.getH_mode=0;
WtHE, HtHE = vhdHE.stain_separate(target_imageHE)
vhdHE.setWt(WtHE); 
vhdHE.setHt(HtHE); 

print('\n Sources \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
## Separate the stain for all images in /Data
parser = argparse.ArgumentParser(description='Test set carcinoids for scanners.')
parser.add_argument('--inputdir', type=str,    help="Input directory where the images are stored")
parser.add_argument('--outputdir', type=str,    help='output directory where the files will be stored')
parser.add_argument('--sample_ID_folder', type=str,    help='output directory where the files will be stored')
args = parser.parse_args()
outputdir = args.outputdir
inputdir = args.inputdir
sample_ID_folder = args.sample_ID_folder
list_images = os.listdir(inputdir)
Images = []
try:
     os.mkdir(os.path.join(outputdir))
except:
        print('outputdir ' , outputdir, ' already created')


try:
     os.mkdir(os.path.join(outputdir, sample_ID_folder))
except:
        print('folder ' , sample_ID_folder, ' already created')

files = os.listdir(os.path.join(inputdir,sample_ID_folder))
print('os.listdir(os.path.join(inputdir,sample_ID_folder))', len(os.listdir(os.path.join(inputdir,sample_ID_folder))))
c = 0
for f in files:
    if f.find('jpg') != -1 :
        c+= 1
        print(c)
        try:
            SOURCE_PATH = os.path.join(inputdir,sample_ID_folder,  f)
            source_image = utils.read_image(SOURCE_PATH)
            Ws, Hs = vhdHE.stain_separate(source_image)
            res = vhdHE.SPCN(source_image, Ws, Hs)# 
            res =  Image.fromarray(res)#:                                                     []
            res.save( os.path.join(outputdir, sample_ID_folder,  f ) , 'JPEG', optimize=True, quality=94) 
        except:
            print('error')







































