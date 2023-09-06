# Elastic Constants Tensor

Scripts to calculate the elastic tensor of a periodic structure using Abinit.

---

The process is as follows:

1. Run the bash script `ElasticConstants.sh`. This script generates 24 folders, each one containing the initial structure with a different deformation appplied to it.

2. Go to each folder and run the Abinit calculations

3. Once the Abinit calculations are completed, run the bash script `ElasticConstantsREAD.sh`.
This script reads the output from the Abinit simulations and writes the files E11, E22, E33, E23, E13 and E12, containiing the relevant information needed for the calculation of the elastic constants tensor

4. Finally, run the python script `ElasticConstantsCalculatorEigenNye3.py`.
This script will output the elastic constants tensor and some other additional information.


---

If you use this software, please cite 

S. Echeverri Restrepo, Density functional theory characterisation of cementite (Fe<sub>3</sub>C) with substitutional molybdenum (Mo) atoms, Phys. B Condens. Matter. 631 (2022) 413669. [https://doi.org/10.1016/j.physb.2022.413669](https://doi.org/10.1016/j.physb.2022.413669)
