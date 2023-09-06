#!/bin/bash


#After the stresses are calculated using the script ElasticConstants.sh, this script 
#	reads the output from abinit

#6 files are generated, one for each component of the stress-strain tensor
#	E11 E22 E33 E23 E13 E12

#Each of these files contains 6 colums with the resulting stresses in GPa
#	s11 s22 s33 s23 s13 s12
#	and 4 lines. Each line corresponds to the resulting stress for a different value of
#		deformation: 	-0.01 
#				-0.005
#				 0.005
#				 0.01


componentVector=(11 22 33 23 13 12)
scalingVector=(-0.01 -0.005 0.005 0.01)

OutFileName=FeBCC.out



for component in  ${componentVector[@]:0}
do

	echo "# s11 s22 s33 s23 s13 s12" > E${component}

	for scaling in  ${scalingVector[@]:0}
	do
		cd "component${component}scale${scaling}"
		pwd

		grep -A3 stress $OutFileName | tail -3 | head -1 | awk '{print $4}' >tmp11
		grep -A3 stress $OutFileName | tail -3 | head -1 | awk '{print $7}' >tmp23

		grep -A3 stress $OutFileName | tail -2 | head -1 | awk '{print $4}' >tmp22
		grep -A3 stress $OutFileName | tail -2 | head -1 | awk '{print $7}' >tmp13

		grep -A3 stress $OutFileName | tail -1 | head -1 | awk '{print $4}' >tmp33
		grep -A3 stress $OutFileName | tail -1 | head -1 | awk '{print $7}' >tmp12

		paste  tmp11 tmp22 tmp33 tmp23 tmp13  tmp12 > tmp_11_22_33_23_13_12

		cat tmp_11_22_33_23_13_12 >> ../E${component}
                cat tmp_11_22_33_23_13_12 

		rm  tmp11 tmp22 tmp33 tmp23 tmp13  tmp12 tmp_11_22_33_23_13_12

		cd ..

	done

	echo component${component}
done

