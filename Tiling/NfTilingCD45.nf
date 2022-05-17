#!/usr/bin/env nextflow
folderlist = Channel.fromPath("/home/mathiane/LNENWork/CLB_1203_NewImgs/CLB/CD45/*{.svs, .mrxs}")
process Tiling{
    conda "/home/mathiane/miniconda3/envs/ImgProcess"
    publishDir "/home/mathiane/LNENWork/CD45_Tiling_256_256"
    
    input:
    file folder from folderlist
    
    script:
    """
    python /home/mathiane/ImgProcessing/Tiling/Tiling.py --inputdir /home/mathiane/LNENWork/CLB_1203_NewImgs/CLB/CD45 --FileSample "$folder" --outputdir /home/mathiane/LNENWork/CD45_Tiling_256_256  --OnlyOneSlide True
    """
}
