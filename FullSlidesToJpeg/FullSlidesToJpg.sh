#!/bin/bash
#SBATCH --job-name=1_806_2159
#SBATCH --output=FullJpg1_806_2159.out
#SBATCH --error=FullJpg1_806_2159.error
#SBATCH --partition=high_p
#SBATCH --account=gcs
##SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=10GB
eval "$(conda shell.bash hook)"
conda activate ImgProcess
python FullSlidesToJpeg.py --inputdir /data/gcs/lungNENomics/files/Internal_Data/Images/LungNENomics_2020 --outputdir /home/mathiane/ln_LNEN_work_mathian/FullSlidesToJpegHighQuality

  
