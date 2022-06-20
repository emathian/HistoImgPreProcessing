#!/bin/bash
#SBATCH --job-name=VahanneHELNEN
#SBATCH --output=TilesVahanneHELNEN.out
#SBATCH --partition=low_p
#SBATCH --account=gcs
#SBATCH --mem-per-cpu=35GB

nextflow run NfHETiles.nf
conda activate ImgProcess
#python /home/mathiane/ImgProcessing/Vahadane/HENormLNEN.py --inputdir /home/mathiane/LNENWork/Tiles_HE_omics_384_384 --sample_ID_folder TNE0305-HPS --outputdir /home/mathiane/LNENWork/Tiles_HE_omics_384_384_Vahadane
