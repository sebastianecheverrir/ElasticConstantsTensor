#!/bin/bash
#SBATCH --job-name=Abinit # Job name
#SBATCH --error=debug_%j.err
#SBATCH --output=debug_%j.out
#SBATCH --partition=hpc
#SBATCH --ntasks-per-core=1
#SBATCH --nodes=1
#SBATCH --ntasks=4



. /shared/apps/spack/0.16.0/spack/share/spack/setup-env.sh

module purge
module load gcc-9.2.0
module load mpi/openmpi-4.1.1
module load abinit-8.10.3-gcc-9.2.0-zux5drf

export OMP_NUM_THREADS=1


mpirun  abinit < FeBCC.files  > log

