#!/bin/bash
#SBATCH --job-name=VAhanneHELNEN
#SBATCH --output=VahanneHELNEN.out
#SBATCH --partition=high_p
#SBATCH --account=gcs
##SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=2GB
eval "$(conda shell.bash hook)"
conda activate ImgProcess
python HE_NormLNEN.py --inputdir ~/ln_LNEN_work_mathian/FullSlidesToJpeg/ --outputdir ~/ln_LNEN_work_mathian/FullSlidesToJpegHENorm/
  
