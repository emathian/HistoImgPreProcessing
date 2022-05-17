#!/bin/bash
#SBATCH --job-name=HVVahanneHELNEN
#SBATCH --output=VahanneHELNEN.out
#SBATCH --partition=high_p
#SBATCH --account=gcs
#SBATCH --mem-per-cpu=38GB

nextflow run NfFullHE.nf
