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



directory_target   = '/home/mathiane/LNENWork/Tiles_HE_all_samples_384_384_2'
TARGET_PATH_HE = directory_target  + '/TNE1344-HPS/accept/'+'/TNE1344-HPS_86401_41857.jpg'
# TARGET_PATH_HES = directory_target + '/TNE0952/'+'TNE0952_15733_17481.jpg'
target_imageHE = utils.read_image(TARGET_PATH_HE)
# target_imageHES = utils.read_image(TARGET_PATH_HES)

# vhdHES = vahadane(STAIN_NUM=3, LAMBDA1=0.01, LAMBDA2=0.01, fast_mode=0, getH_mode=0, ITER=50)
# vhdHES.fast_mode=0;
# vhdHES.getH_mode=0;
# WtHES, HtHES = vhdHES.stain_separate(target_imageHES)
# vhdHES.setWt(WtHES); 
# vhdHES.setHt(HtHES); 

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
# if sample_ID_folder not in os.listdir('/home/mathiane/LNENWork/Tiles_HE_omics_384_384_Vahadane'):
try:
 os.mkdir(os.path.join(outputdir, sample_ID_folder))
except:
    print('folder ' , sample_ID_folder, ' already created')
acc_reject_foder = os.listdir(os.path.join(inputdir,sample_ID_folder))
for folder in acc_reject_foder:
    files = os.listdir(os.path.join(inputdir,sample_ID_folder,folder))
    if folder == 'Tumor' or folder == 'Normal' :
        try:
            os.mkdir(os.path.join(outputdir, sample_ID_folder, folder))
        except:
            print('folder ' , folder, ' already created')
        for f in files:
            if f.find('jpg') != -1 :
                # try:
                print(f)
                SOURCE_PATH = os.path.join(inputdir,sample_ID_folder,folder,  f)
                print('SOURCE_PATH  ', SOURCE_PATH)
                source_image = utils.read_image(SOURCE_PATH)
                Ws, Hs = vhdHE.stain_separate(source_image)
                res = vhdHE.SPCN(source_image, Ws, Hs)# 
                res =  Image.fromarray(res)#:                                                     []
                res.save( os.path.join(outputdir, sample_ID_folder, folder, f ) , 'JPEG', optimize=True, quality=94) 
                # except:
                #     print(f'{f} process failed!')
































