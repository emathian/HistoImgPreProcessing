#!/usr/bin/env nextflow
imagelist = Channel.fromPath("/data/lungNENomics/files/Internal_Data/Images/LCNEC/*{svs,mrxs}")
process FullSlidesToJpeg{
    publishDir '/home/mathiane/LNENWork/LCNECFullImgJPG'
    conda "/home/mathiane/miniconda3/envs/ImgProcess"
    input:
    file img from imagelist
    script:
    """
    python /home/mathiane/ImgProcessing/FullSlidesToJpeg/FullSlidesToJpegNf.py --inputdir /data/lungNENomics/files/Internal_Data/Images/LCNEC  --inputfile $img --outputdir /home/mathiane/LNENWork/CNECFullImgJPG/LCNECFullImgJPG
    """
}
