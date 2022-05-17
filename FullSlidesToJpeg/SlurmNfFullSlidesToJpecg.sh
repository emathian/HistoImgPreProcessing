#!/bin/bash
#SBATCH --job-name=NfFullSlides
#SBATCH --output=NfFullSlides.out
#SBATCH --partition=high_p
#SBATCH --account=gcs
##SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=10GB
nextflow run NfFullSlidesToJpeg.nf
