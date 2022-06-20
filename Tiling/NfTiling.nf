#!/usr/bin/env nextflow
folderlist = Channel.fromPath("/home/mathiane/LNEN_files_imgs/HES_Massimo_LCNEC/*{.svs, .mrxs}")
process Tiling{
    conda "/home/mathiane/miniconda3/envs/ImgProcess"
    publishDir "/home/mathiane/LNENWork/Tiles_HE_all_samples_384_384_2"
    
    input:
    file folder from folderlist
    
    script:
    """
    python /home/mathiane/ImgProcessing/Tiling/Tiling.py --inputdir /home/mathiane/LNEN_files_imgs/HES_Massimo_LCNEC  --FileSample "$folder" --outputdir /home/mathiane/LNENWork/Tiles_HE_massimo_LCNEC_384_384  --OnlyOneSlide True
    """
}
