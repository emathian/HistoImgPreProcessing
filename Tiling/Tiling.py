from __future__ import division
from multiprocessing import Pool
import sys
import os
import argparse
# # necessary to add cwd to path when script run 
# # by slurm (since it executes a copy)
sys.path.append(os.getcwd()) 

import cv2
import numpy as np
from openslide import OpenSlide
from PIL import Image
from resizeimage import resizeimage
import random 

global inputdir
global outputdir


def getGradientMagnitude(im):
    "Get magnitude of gradient for given image"
    ddepth = cv2.CV_32F
    dx = cv2.Sobel(im, ddepth, 1, 0)
    dy = cv2.Sobel(im, ddepth, 0, 1)
    dxabs = cv2.convertScaleAbs(dx)
    dyabs = cv2.convertScaleAbs(dy)
    mag = cv2.addWeighted(dxabs, 0.5, dyabs, 0.5, 0)
    return mag


def random_tiles(imgfilename, inputdir, outputdir):
    print(imgfilename, inputdir, outputdir)
    print(os.path.join(inputdir, imgfilename), "\n \n ")
    if imgfilename.find(".svs") != -1 or imgfilename.find("mrxs") != -1:
        filepath = os.path.join(inputdir, imgfilename) 
        img  = OpenSlide(filepath)
        sample_id = imgfilename.split(" ")[0]
        try:
            os.mkdir(os.path.join(outputdir))
        except:
            print("The Folder already exist")
        try:
            os.mkdir(os.path.join(outputdir, sample_id))
        except:
            print("The Folder for the sample id {} already exist".format(sample_id))
        if imgfilename.find(".svs") != -1 :
            if str(img.properties.values.__self__.get('tiff.ImageDescription')).split("|")[1] == "AppMag = 40":

                # PathoNet resolution 
                sz = 512
                seq = 512
                # Others
                # sz=1024
                # seq=924
            else:
                # Pathonet Resolution
                sz = 256
                seq = 256
                # Others
                # sz=512
                # seq=462
        elif  imgfilename.find("mrxs") != -1:
            if str(img.properties.values.__self__.get("mirax.GENERAL.OBJECTIVE_MAGNIFICATION")) == 20:
                # Pathonet
                sz = 256 
                seq = 256
                # Others
                # sz=512
                # seq=462
            else: 
                # Paathonet
                sz = 512 
                seq = 512
                # Others 
                # sz=1024
                # seq=924
        [w, h] = img.dimensions
        couple_coords_accepted = []
        for x in range(1, w, seq):
            for y in range(1, h, seq):
                # try:
                img1=img.read_region(location=(x,y), level=0, size=(sz,sz))
                img11=img1.convert("RGB")
                img111=img11.resize((256,256),Image.ANTIALIAS)
                pix = np.array(img111)
                grad=getGradientMagnitude(pix)
                unique, counts = np.unique(grad, return_counts=True)
                mean_ch = np.mean(pix, axis=2)
                bright_pixels_count = np.argwhere(mean_ch > 220).shape[0]
                if counts[np.argwhere(unique<=15)].sum() < 256*256*0.6 and bright_pixels_count <  256*256*0.5 :
                    couple_coords_accepted.append((x,y) )
            # except:
            #     print('error Tiles {}, pos {}, {} '.format(sample_id, x, y  ))
        sample_random_accepted_slides = random.sample(couple_coords_accepted, 100)
        for (x,y) in sample_random_accepted_slides:
            img1=img.read_region(location=(x,y), level=0, size=(sz,sz))
            img11=img1.convert("RGB")
            img111=img11.resize((256,256),Image.ANTIALIAS)
            img111.save( os.path.join(outputdir, sample_id, sample_id + "_" +  str(x) + "_" + str(y) + '.jpg'  ) , 'JPEG', optimize=True, quality=94)
            

def full_pictures_to_tiles(imgfilename, inputdir, outputdir):
    # For TCGA SLIDES
    print(imgfilename, inputdir, outputdir)
    print(os.path.join(inputdir, imgfilename), "\n \n ")
    sample_id = imgfilename.split("_")[0]
    sample_id = sample_id.split(".")[0]
    print('sample_id  ', sample_id)
    # if os.path.join(outputdir, sample_id)
    try:
        os.mkdir(os.path.join(outputdir))
    except:
        print("The Folder already exist")
    try:
        os.mkdir(os.path.join(outputdir, sample_id))
    except:
        print("The Folder for the sample id {} already exist".format(sample_id))
    try:
        os.mkdir(os.path.join(outputdir, sample_id, 'accept'))
    except:
        print('Accept folder already created')  
    try:
        os.mkdir(os.path.join(outputdir, sample_id, 'reject'))
    except:
        print('Reject  folder already created')  

    if imgfilename.find(".svs") != -1 or imgfilename.find("mrxs") != -1:
        filepath = os.path.join(inputdir, imgfilename) 
        print('filepath ', filepath)
        img  = OpenSlide(filepath)
        if imgfilename.find(".svs") != -1 :
            if str(img.properties.values.__self__.get('tiff.ImageDescription')).split("|")[1] == "AppMag = 40":
                sz = 384
                seq = 384
                # Others
                # sz=1024
                # seq=924
            else:
                # Pathonet Resolution
                sz = 192
                seq = 192
                # Others
                # sz=512
                # seq=462
        elif  imgfilename.find("mrxs") != -1:
            if str(img.properties.values.__self__.get("mirax.GENERAL.OBJECTIVE_MAGNIFICATION")) == 20:
                # Pathonet
                sz = 192 
                seq = 192
                # Others
                # sz=512
                # seq=462
            else: 
                # Paathonet
                sz = 384 
                seq = 384
                # Others 
                # sz=1024
                # seq=924
    [w, h] = img.dimensions
    for x in range(1, w, seq):
        for y in range(1, h, seq):
            try:
                img  = OpenSlide(filepath)
                img1=img.read_region(location=(x,y), level=0, size=(sz,sz))
                img11=img1.convert("RGB")
                img111=img11.resize((384,384),Image.ANTIALIAS)
                pix = np.array(img111)
                grad=getGradientMagnitude(pix)
                unique, counts = np.unique(grad, return_counts=True)
                mean_ch = np.mean(pix, axis=2)
                bright_pixels_count = np.argwhere(mean_ch > 220).shape[0]
                if counts[np.argwhere(unique<=15)].sum() < 384*384*0.7 and bright_pixels_count <  384*384*0.7:
                    # print( os.path.join(outputdir, sample_id, sample_id + "_" +  str(x) + "_" + str(y) + '.jpg'  ))
                    img111.save( os.path.join(outputdir, sample_id,'accept', sample_id + "_" +  str(x) + "_" + str(y) + '.jpg'  ) , 'JPEG', optimize=True, quality=94)
                else:
                    img111.save( os.path.join(outputdir, sample_id,'reject', sample_id + "_" +  str(x) + "_" + str(y) + '.jpg'  ) , 'JPEG', optimize=True, quality=94) 
        
            except:
                with open('errorReadingSlides_0_77.txt', 'a') as f:
                    f.write('\n{}\t{}\t{}'.format(sample_id,x,y))
                #print('error Tiles {}, pos {}, {} '.format(sample_id, x, y  ))
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test set carcinoids for scanners.')
    parser.add_argument('--inputdir', type=str,    help="Input directory where the images are stored")
    parser.add_argument('--outputdir', type=str,    help='output directory where the files will be stored')
    parser.add_argument('--OnlyOneSlide', type=bool,    help='If only one Tiled Has to be processed')
    parser.add_argument('--FileSample', type=str,    help='For one sample')
    file1 = open('/home/mathiane/ImgProcessing/Tiling/images_with_omics_for_tiling.txt', 'r')
    Lines = file1.readlines()
    fname2Tiles = []
    for ele in Lines:
        fname2Tiles.append(ele[:-1])
    args = parser.parse_args()
    outputdir = args.outputdir
    inputdir = args.inputdir
    OnlyOneSlide = args.OnlyOneSlide
    FileSample = args.FileSample
    try:
        os.mkdir(outpudir)
    except:
        print('Output dir created')
    if OnlyOneSlide == False:
        nb_l = []
        images_l = []
        all_f = os.listdir(inputdir) # To change main folder
        all_o = os.listdir(outputdir)
        for f in all_f:
            if f.find(".svs") != -1 or f.find(".mrxs") != -1:
                sample = f.split('.')[0]
                print('Sample ', sample, '\n')
                num = int(f.split('.')[0].split(' ')[-1])
                print('Num ', num)
                if f not in all_o:
                    images_l.append(f)
                #full_pictures_to_tiles(f, inputdir, outputdir) 
                print('\n\n')
        if len(images_l) > 0:
            array_of_args = [(i, inputdir, outputdir) for i in images_l]
            with Pool(len(images_l)) as p:
                p.starmap(full_pictures_to_tiles, array_of_args)
    else:
        c =0 
        if FileSample not in os.listdir(outputdir) and (FileSample.find('svs') !=-1 or FileSample.find('mrxs') !=-1 ):
            full_pictures_to_tiles(FileSample, inputdir, outputdir)
                 
        # for FileSample in  os.listdir(inputdir):
        #     if FileSample not in os.listdir(outputdir) and (FileSample.find('svs') !=-1 or FileSample.find('mrxs') !=-1 ):
        #         if len( FileSample.split('_')) >= 2:
        #             if FileSample.split('_')[1].find('20') == -1: 
        #                 #full_pictures_to_tiles(FileSample, inputdir, outputdir)
        #                 t = 0
        #         elif FileSample.find('_') == -1:
        #             print(FileSample)
        #             c += 1
        print(c)
        # if FileSample.find('TNE0180-HPS') != -1 or  FileSample.find('TNE0181-HPS') != -1 or \
        # FileSample.find('TNE0305-HPS') != -1 or FileSample.find('TNE0360') != -1 or FileSample.find('TNE0404-HPS') != -1 :
        # FileSample_c = FileSample.split('.')[0]
        # print('FileSample  ', FileSample)
        # full_pictures_to_tiles(FileSample, inputdir, outputdir)
