#!/bin/bash
#SBATCH --job-name=TilingKi67
#SBATCH --output=TilesKi67_2.out
#SBATCH --error=TilesKi67_2.error
#SBATCH --partition=high_p
#SBATCH --account=gcs
nextflow run -resume NfTiling.nf