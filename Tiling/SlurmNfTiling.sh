#!/bin/bash
#SBATCH --job-name=TilingKi67
#SBATCH --output=TilesKi67_2.out
#SBATCH --error=TilesKi67_2.error
#SBATCH --partition=high_p
#SBATCH --account=gcs
nextflow run -resume NfTiling.nf
eval "$(conda shell.bash hook)"
conda activate ImgProcess
#python /home/mathiane/ImgProcessing/Tiling/Tiling.py --inputdir /data/lungNENomics/files/Internal_Data/Images/LunGNeNOmicsImagesBatch123  --FileSample TNE0360-HPS_magx40.svs --outputdir /home/mathiane/LNENWork/Tiles_HE_omics_384_384  --OnlyOneSlide True