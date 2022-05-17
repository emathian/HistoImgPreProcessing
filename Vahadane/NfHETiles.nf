#!/usr/bin/env nextflow
folderlist = Channel.fromPath("/home/mathiane/LNENWork/Tiles_HE_omics_384_384/*",  type: 'dir')
process TilesHEVahadane{
    conda "/home/mathiane/miniconda3/envs/ImgProcess"
    publishDir "/home/mathiane/LNENWork/Tiles_HE_omics_384_384_Vahadane_2"
    
    input:
    file folder from folderlist
    
    script:
    """
    python /home/mathiane/ImgProcessing/Vahadane/HENormLNEN.py --inputdir /home/mathiane/LNENWork/Tiles_HE_omics_384_384 --sample_ID_folder $folder --outputdir /home/mathiane/LNENWork/Tiles_HE_omics_384_384_Vahadane_2
    """
}
