#!/usr/bin/env nextflow
folderlist = Channel.fromPath("/data/lungNENomics/files/Internal_Data/Images/LunGNeNOmicsImagesBatch123/*{.svs, .mrxs}")
process Tiling{
    conda "/home/mathiane/miniconda3/envs/ImgProcess"
    publishDir "/home/mathiane/LNENWork/Tiles_HE_LCNEC_384_384"
    
    input:
    file folder from folderlist
    
    script:
    """
    python /home/mathiane/ImgProcessing/Tiling/Tiling.py --inputdir /data/lungNENomics/files/Internal_Data/Images/LunGNeNOmicsImagesBatch123  --FileSample "$folder" --outputdir /home/mathiane/LNENWork/Tiles_HE_omics_384_384  --OnlyOneSlide True
    """
}
