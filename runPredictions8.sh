#!/bin/bash
# Author: M.Jacobs

# Slurm directives
#SBATCH --job-name=PredictElectrophilicity
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1

cd $SLURM_SUBMIT_DIR

module purge

module load SciPy-bundle/2023.07-gfbf-2023a

python dirty_calc/predict8.py
