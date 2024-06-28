#!/bin/bash
# Author: M.Jacobs

# Slurm directives
#SBATCH --job-name=PredictElectrophilicity
#SBATCH --time=00:05:00
#SBATCH --ntasks=1

cd $SLURM_SUBMIT_DIR

module purge

module load OpenBabel/3.1.1-gompi-2023a

python code/predict.py
