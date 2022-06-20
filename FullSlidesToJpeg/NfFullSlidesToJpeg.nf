#!/usr/bin/env nextflow
imagelist = Channel.fromPath("/home/mathiane/LNEN_files_imgs/LunGNeNOmicsImagesBatch123/*{svs,mrxs}")
process FullSlidesToJpeg{
    publishDir '/home/mathiane/LNENWork/LCNECFullImgJPG'
    conda "/home/mathiane/miniconda3/envs/ImgProcess"
    input:
    file img from imagelist
    script:
    """
    python /home/mathiane/ImgProcessing/FullSlidesToJpeg/FullSlidesToJpegNf.py --inputdir /home/mathiane/LNEN_files_imgs/LunGNeNOmicsImagesBatch123  --inputfile $img --outputdir /home/mathiane/LNENWork/FullSlidesToJpegHENormHighQuality
    """
}
