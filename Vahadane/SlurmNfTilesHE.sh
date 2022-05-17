#!/bin/bash
#SBATCH --job-name=VahanneHELNEN
#SBATCH --output=TilesVahanneHELNEN.out
#SBATCH --partition=low_p
#SBATCH --account=gcs
#SBATCH --mem-per-cpu=35GB
nextflow run NfHETiles.nf
