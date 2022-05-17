#!/usr/bin/env nextflow
imagelist = Channel.fromPath("/home/mathiane/ln_LNEN_work_mathian/FullSlidesToJpegHighQualityNormalLung/*.jpg")
process VahadaneNorm{
    conda "/home/mathiane/miniconda3/envs/ImgProcess"
    publishDir "/home/mathiane/ln_LNEN_work_mathian/FullSlidesToJpegHENormHighQuality"
    
    input:
    file img from imagelist
    
    script:
    """
    python /home/mathiane/ImgProcessing/Vahadane/HE_NormFullTiles.py --inputfile $img --outputdir /home/mathiane/ln_LNEN_work_mathian/FullSlidesToJpegHENormHighQualityNormalLung/
    """
}
