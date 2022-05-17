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

directory_target   = '/home/mathiane/ln_LNEN_work_mathian/FullSlidesToJpegHighQuality'
TARGET_PATH_HE = directory_target + '/TNE0287.jpg'#+ '/TNE0535/'+'TNE0535_8741_106629.jpg'
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
parser.add_argument('--inputfile', type=str,    help="Input directory where the images are stored")
parser.add_argument('--outputdir', type=str,    help='output directory where the files will be stored')
args = parser.parse_args()
outputdir = args.outputdir
inputfile = args.inputfile

sample_id = inputfile.split('/')[-1].split('.')[0]#.split(' ')[0].split('_')[0]
f = inputfile.split('/')[-1]#
if f not in os.listdir(outputdir):
    print(sample_id)
    SOURCE_PATH = os.path.join(inputfile)        
    source_image = utils.read_image(SOURCE_PATH)


    print("f  ", f)

    Ws, Hs = vhdHE.stain_separate(source_image)
    res = vhdHE.SPCN(source_image, Ws, Hs)# 
    res =  Image.fromarray(res)#:                                                     []
    res.save( os.path.join(outputdir,  f ) , 'JPEG', optimize=True, quality=94) 

















