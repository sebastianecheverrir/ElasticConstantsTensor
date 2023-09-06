#!/bin/bash


##################################################


initial11=1
initial12=0
initial13=0
initial21=0
initial22=1
initial23=0
initial31=0
initial32=0
initial33=1




scalingVector=(-0.01 -0.005 0.005 0.01)
componentVector=(11 22 33 23 13 12)


InTEMPLATEFileName=FeBCCTEMPLATE.in
InFileName=FeBCC.in

qsubFileName=runfileAbinitAzure.sh


##################################################
function matrix_multiply {

result11=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r11*m11+r12*m21+r13*m31}'`
result12=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r11*m12+r12*m22+r13*m32}'`
result13=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r11*m13+r12*m23+r13*m33}'`
result21=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r21*m11+r22*m21+r23*m31}'`
result22=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r21*m12+r22*m22+r23*m32}'`
result23=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r21*m13+r22*m23+r23*m33}'`
result31=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r31*m11+r32*m21+r33*m31}'`
result32=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r31*m12+r32*m22+r33*m32}'`
result33=`awk -v r11=$1 -v r12=$2 -v r13=$3 -v r21=$4 -v r22=$5 -v r23=$6 -v r31=$7 -v r32=$8 -v r33=$9  -v m11=${10} -v m12=${11} -v m13=${12} -v m21=${13} -v m22=${14} -v m23=${15} -v m31=${16} -v m32=${17} -v m33=${18} 'BEGIN{print r31*m13+r32*m23+r33*m33}'`

echo $result11
echo $result12
echo $result13
echo $result21
echo $result22
echo $result23
echo $result31
echo $result32
echo $result33


}

#matrix_multiply $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33 $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33


##################################################



for component in  ${componentVector[@]:0}
do
for scaling in  ${scalingVector[@]:0}
do


	mkdir "component${component}scale${scaling}"
	cp tmp/* component${component}scale${scaling}

	initial="initial$component"
#	echo ${initial}
#	echo ${!initial}

	final=`awk -v Initial=${!initial} -v Scaling=$scaling 'BEGIN{OFMT = "%.11g"; print Initial+Initial*Scaling}'`
#	echo $final



	if [ $component -eq 11 ]
	then
		rot11=`awk -v Scaling=$scaling 'BEGIN{OFMT = "%.11g"; print 1+1*Scaling}'`
		rot12=0
		rot13=0
		rot21=0
		rot22=1
		rot23=0
		rot31=0
		rot32=0
		rot33=1

		final11=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -1`
                final12=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -2 | tail -1`
                final13=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -3 | tail -1`
                final21=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -4 | tail -1`
                final22=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -5 | tail -1`
                final23=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -6 | tail -1`
                final31=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -7 | tail -1`
                final32=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -8 | tail -1`
                final33=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -9 | tail -1`

	#	matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  

	#	echo $final11 $final12 $final13 $final21 $final22 $final23 $final31 $final32 $final33


		cat tmp/$InTEMPLATEFileName | sed "s/rprim/rprim $final11 $final12 $final13 $final21 $final22 $final23 $final31 $final32 $final33  /g" > component${component}scale${scaling}/$InFileName
#	echo "11"
	fi
        if [ $component -eq 22 ]
        then
                rot11=1
                rot12=0
                rot13=0
                rot21=0
                rot22=`awk -v Scaling=$scaling 'BEGIN{OFMT = "%.11g"; print 1+1*Scaling}'`
                rot23=0
                rot31=0
                rot32=0
                rot33=1

                final11=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -1`  
                final12=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -2 | tail -1`
                final13=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -3 | tail -1`
                final21=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -4 | tail -1`
                final22=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -5 | tail -1`
                final23=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -6 | tail -1`
                final31=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -7 | tail -1`
                final32=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -8 | tail -1`
                final33=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -9 | tail -1`

                cat tmp/$InTEMPLATEFileName | sed "s/rprim/rprim $final11 $final12 $final13 $final21 $final22 $final23 $final31 $final32 $final33  /g" > component${component}scale${scaling}/$InFileName

	fi

        if [ $component -eq 33 ]
        then
                rot11=1
                rot12=0
                rot13=0
                rot21=0
                rot22=1
                rot23=0
                rot31=0
                rot32=0
                rot33=`awk -v Scaling=$scaling 'BEGIN{OFMT = "%.11g"; print 1+1*Scaling}'`

                final11=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -1`  
                final12=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -2 | tail -1`
                final13=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -3 | tail -1`
                final21=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -4 | tail -1`
                final22=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -5 | tail -1`
                final23=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -6 | tail -1`
                final31=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -7 | tail -1`
                final32=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -8 | tail -1`
                final33=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -9 | tail -1`

                cat tmp/$InTEMPLATEFileName | sed "s/rprim/rprim $final11 $final12 $final13 $final21 $final22 $final23 $final31 $final32 $final33  /g" > component${component}scale${scaling}/$InFileName

        fi

        if [ $component -eq 23 ]
        then
                rot11=1
                rot12=0
                rot13=0
                rot21=0
                rot22=1
                rot23=`awk -v Scaling=$scaling 'BEGIN{OFMT = "%.11g"; print 0+1*Scaling}'`
                rot31=0
                rot32=0
                rot33=1

                final11=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -1`  
                final12=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -2 | tail -1`
                final13=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -3 | tail -1`
                final21=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -4 | tail -1`
                final22=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -5 | tail -1`
                final23=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -6 | tail -1`
                final31=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -7 | tail -1`
                final32=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -8 | tail -1`
                final33=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -9 | tail -1`

                cat tmp/$InTEMPLATEFileName | sed "s/rprim/rprim $final11 $final12 $final13 $final21 $final22 $final23 $final31 $final32 $final33  /g" > component${component}scale${scaling}/$InFileName

        fi

        if [ $component -eq 13 ]
        then
                rot11=1
                rot12=0
                rot13=`awk -v Scaling=$scaling 'BEGIN{OFMT = "%.11g"; print 0+1*Scaling}'`
                rot21=0
                rot22=1
                rot23=0
                rot31=0
                rot32=0
                rot33=1

                final11=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -1`  
                final12=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -2 | tail -1`
                final13=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -3 | tail -1`
                final21=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -4 | tail -1`
                final22=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -5 | tail -1`
                final23=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -6 | tail -1`
                final31=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -7 | tail -1`
                final32=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -8 | tail -1`
                final33=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -9 | tail -1`

                cat tmp/$InTEMPLATEFileName | sed "s/rprim/rprim $final11 $final12 $final13 $final21 $final22 $final23 $final31 $final32 $final33  /g" > component${component}scale${scaling}/$InFileName

        fi

        if [ $component -eq 12 ]
        then
                rot11=1
                rot12=`awk -v Scaling=$scaling 'BEGIN{OFMT = "%.11g"; print 0+1*Scaling}'`
                rot13=0
                rot21=0
                rot22=1
                rot23=0
                rot31=0
                rot32=0
                rot33=1

                final11=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -1`  
                final12=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -2 | tail -1`
                final13=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -3 | tail -1`
                final21=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -4 | tail -1`
                final22=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -5 | tail -1`
                final23=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -6 | tail -1`
                final31=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -7 | tail -1`
                final32=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -8 | tail -1`
                final33=`matrix_multiply $initial11 $initial12 $initial13 $initial21 $initial22 $initial23 $initial31 $initial32 $initial33  $rot11 $rot12 $rot13 $rot21 $rot22 $rot23 $rot31 $rot32 $rot33  | head -9 | tail -1`

                cat tmp/$InTEMPLATEFileName | sed "s/rprim/rprim $final11 $final12 $final13 $final21 $final22 $final23 $final31 $final32 $final33  /g" > component${component}scale${scaling}/$InFileName

        fi



	cd component${component}scale${scaling}
	rm $InTEMPLATEFileName
        sbatch $qsubFileName
        cd ..


done
done

