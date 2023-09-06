#!/usr/bin python

import numpy
import scipy.optimize
import matplotlib.pyplot as plt


EIJ=[ -0.01,-0.005, 0.005, 0.01]
#EIJ=[ -0.01,-0.0075,-0.005,-0.0025,0.0025, 0.005,0.0075, 0.01]


#Defining the functions to fit
def func(E, C, b): #S=C*E
        return C*E+b

def funcShear(E, C2, b): #S=C12*E22+2*C16*E12
        return E[2]*E[1]+2*C2*E[0]+b


#defining the function to calculate the Green-Lagrange strain tensor
def GreenLagrange(F):
	return (F.transpose().dot(F)-numpy.identity(3))/2


#######################################################################
#deformation applied to E11, response S11, to calculate the constant C11
E11_S11_C11=[]
E11_S22_C12=[]
E11_S33_C13=[]
E11_S23_C14=[]
E11_S13_C15=[]
E11_S12_C16=[]

#reeding the file
fileE11 = open("E11", "r")

i=0
for line in fileE11:
	if i!=0:
		lineSplitted=line.split()
		E11_S11_C11.append(float(lineSplitted[0]))
		E11_S22_C12.append(float(lineSplitted[1]))
		E11_S33_C13.append(float(lineSplitted[2]))
		E11_S23_C14.append(float(lineSplitted[3]))
		E11_S13_C15.append(float(lineSplitted[4]))
		E11_S12_C16.append(float(lineSplitted[5]))
		#print lineSplitted
	i += 1

#print  ""
#print E11_S11_C11
#print E11_S22_C12
#print E11_S33_C13
#print E11_S23_C14
#print E11_S13_C15
#print E11_S12_C16

#print EIJ

#Calculating the real EIJ. this is a matrix. the columns are E11 E22 E33 E23 E13 E12

#print len(EIJ)

EIJmat=numpy.empty([len(EIJ),6])
i=0
for delta in EIJ:
	F11=numpy.array([[1+delta,0,0],[0,1,0],[0,0,1]])
	EIJline=numpy.array([GreenLagrange(F11)[0,0],GreenLagrange(F11)[1,1],GreenLagrange(F11)[2,2],GreenLagrange(F11)[1,2],GreenLagrange(F11)[0,2],GreenLagrange(F11)[0,1]])
	EIJmat[i,:]=EIJline[:]
	i=i+1



#Converting list to array. Needed for the fit
EIJ=numpy.asarray(EIJ)
E11_S11_C11=numpy.asarray(E11_S11_C11)
E11_S22_C12=numpy.asarray(E11_S22_C12)
E11_S33_C13=numpy.asarray(E11_S33_C13)
E11_S23_C14=numpy.asarray(E11_S23_C14)
E11_S13_C15=numpy.asarray(E11_S13_C15)
E11_S12_C16=numpy.asarray(E11_S12_C16)

#print "here"
#print EIJ
#print EIJmat[:,0]
#print E11_S11_C11

#print EIJmat[:,0]
#print E11_S11_C11

C11opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,0], E11_S11_C11)
C12opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,0], E11_S22_C12)
C13opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,0], E11_S33_C13)
C14opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,0], E11_S23_C14)
C15opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,0], E11_S13_C15)
C16opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,0], E11_S12_C16)

print( "----------------------------------------------")
print( "ELASTIC CONSTANTS")
print( "C11=", (C11opt[0]))
print( "C12=", (C12opt[0]))
print( "C13=", (C13opt[0]))
print( "C14=", (C14opt[0]))
print( "C15=", (C15opt[0]))
print( "C16=", (C16opt[0]))
print( " ")




fitC11=func(EIJmat[:,0], C11opt[0], C11opt[1])
fitC12=func(EIJmat[:,0], C12opt[0], C12opt[1])
fitC13=func(EIJmat[:,0], C13opt[0], C13opt[1])
fitC14=func(EIJmat[:,0], C14opt[0], C14opt[1])
fitC15=func(EIJmat[:,0], C15opt[0], C15opt[1])
fitC16=func(EIJmat[:,0], C16opt[0], C16opt[1])



fig, ax1 = plt.subplots()
ax1.plot(EIJmat[:,0], E11_S11_C11, 'o')
ax1.plot(EIJmat[:,0], E11_S22_C12, 'o')
ax1.plot(EIJmat[:,0], E11_S33_C13, 'o')
ax1.plot(EIJmat[:,0], E11_S23_C14, 'o')
ax1.plot(EIJmat[:,0], E11_S13_C15, 'o')
ax1.plot(EIJmat[:,0], E11_S12_C16, 'o')



ax1.plot(EIJmat[:,0], fitC11)
ax1.plot(EIJmat[:,0], fitC12)
ax1.plot(EIJmat[:,0], fitC13)
ax1.plot(EIJmat[:,0], fitC14)
ax1.plot(EIJmat[:,0], fitC15)
ax1.plot(EIJmat[:,0], fitC16)


#plt.show()



#######################################################################
#deformation applied to E22, response S11, to calculate the constant C11
E22_S11_C21=[]
E22_S22_C22=[]
E22_S33_C23=[]
E22_S23_C24=[]
E22_S13_C25=[]
E22_S12_C26=[]

#reeding the file
fileE22 = open("E22", "r")

i=0
for line in fileE22:
        if i!=0:
                lineSplitted=line.split()
                E22_S11_C21.append(float(lineSplitted[0]))
                E22_S22_C22.append(float(lineSplitted[1]))
                E22_S33_C23.append(float(lineSplitted[2]))
                E22_S23_C24.append(float(lineSplitted[3]))
                E22_S13_C25.append(float(lineSplitted[4]))
                E22_S12_C26.append(float(lineSplitted[5]))
                #print lineSplitted
        i += 1

#print  ""
#print E22_S11_C21
#print E22_S22_C22
#print E22_S33_C23
#print E22_S23_C24
#print E22_S13_C25
#print E22_S12_C26

#print EIJ


#Calculating the real EIJ. this is a matrix. the columns are E11 E22 E33 E23 E13 E12
EIJmat=numpy.empty([len(EIJ),6])
i=0
for delta in EIJ:
	F22=numpy.array([[1,0,0],[0,1+delta,0],[0,0,1]])
	EIJline=numpy.array([GreenLagrange(F22)[0,0],GreenLagrange(F22)[1,1],GreenLagrange(F22)[2,2],GreenLagrange(F22)[1,2],GreenLagrange(F22)[0,2],GreenLagrange(F22)[0,1]])
	EIJmat[i,:]=EIJline[:]
	i=i+1




#Converting list to array. Needed for the fit
EIJ=numpy.asarray(EIJ)
E22_S11_C21=numpy.asarray(E22_S11_C21)
E22_S22_C22=numpy.asarray(E22_S22_C22)
E22_S33_C23=numpy.asarray(E22_S33_C23)
E22_S23_C24=numpy.asarray(E22_S23_C24)
E22_S13_C25=numpy.asarray(E22_S13_C25)
E22_S12_C26=numpy.asarray(E22_S12_C26)

C21opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,1], E22_S11_C21)
C22opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,1], E22_S22_C22)
C23opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,1], E22_S33_C23)
C24opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,1], E22_S23_C24)
C25opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,1], E22_S13_C25)
C26opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,1], E22_S12_C26)



print( "C21=", (C21opt[0]))
print( "C22=", (C22opt[0]))
print( "C23=", (C23opt[0]))
print( "C24=", (C24opt[0]))
print( "C25=", (C25opt[0]))
print( "C26=", (C26opt[0]))
print( " ")




fitC21=func(EIJmat[:,1], C21opt[0], C21opt[1])
fitC22=func(EIJmat[:,1], C22opt[0], C22opt[1])
fitC23=func(EIJmat[:,1], C23opt[0], C23opt[1])
fitC24=func(EIJmat[:,1], C24opt[0], C24opt[1])
fitC25=func(EIJmat[:,1], C25opt[0], C25opt[1])
fitC26=func(EIJmat[:,1], C26opt[0], C26opt[1])


#fig, ax1 = plt.subplots()
ax1.plot(EIJmat[:,1], E22_S11_C21, 'o')
ax1.plot(EIJmat[:,1], E22_S22_C22, 'o')
ax1.plot(EIJmat[:,1], E22_S33_C23, 'o')
ax1.plot(EIJmat[:,1], E22_S23_C24, 'o')
ax1.plot(EIJmat[:,1], E22_S13_C25, 'o')
ax1.plot(EIJmat[:,1], E22_S12_C26, 'o')



ax1.plot(EIJmat[:,1], fitC21)
ax1.plot(EIJmat[:,1], fitC22)
ax1.plot(EIJmat[:,1], fitC23)
ax1.plot(EIJmat[:,1], fitC24)
ax1.plot(EIJmat[:,1], fitC25)
ax1.plot(EIJmat[:,1], fitC26)


#plt.show()

#######################################################################
#deformation applied to E33, response S11, to calculate the constant C11
E33_S11_C31=[]
E33_S22_C32=[]
E33_S33_C33=[]
E33_S23_C34=[]
E33_S13_C35=[]
E33_S12_C36=[]

#reeding the file
fileE33 = open("E33", "r")

i=0
for line in fileE33:
        if i!=0:
                lineSplitted=line.split()
                E33_S11_C31.append(float(lineSplitted[0]))
                E33_S22_C32.append(float(lineSplitted[1]))
                E33_S33_C33.append(float(lineSplitted[2]))
                E33_S23_C34.append(float(lineSplitted[3]))
                E33_S13_C35.append(float(lineSplitted[4]))
                E33_S12_C36.append(float(lineSplitted[5]))
                #print lineSplitted
        i += 1

#print  ""
#print E33_S11_C31
#print E33_S22_C32
#print E33_S33_C33
#print E33_S23_C34
#print E33_S13_C35
#print E33_S12_C36

#print EIJ

#Calculating the real EIJ. this is a matrix. the columns are E11 E22 E33 E23 E13 E12
EIJmat=numpy.empty([len(EIJ),6])
i=0
for delta in EIJ:
	F33=numpy.array([[1,0,0],[0,1,0],[0,0,1+delta]])
	EIJline=numpy.array([GreenLagrange(F33)[0,0],GreenLagrange(F33)[1,1],GreenLagrange(F33)[2,2],GreenLagrange(F33)[1,2],GreenLagrange(F33)[0,2],GreenLagrange(F33)[0,1]])
	EIJmat[i,:]=EIJline[:]
	i=i+1


#Converting list to array. Needed for the fit
EIJ=numpy.asarray(EIJ)
E33_S11_C31=numpy.asarray(E33_S11_C31)
E33_S22_C32=numpy.asarray(E33_S22_C32)
E33_S33_C33=numpy.asarray(E33_S33_C33)
E33_S23_C34=numpy.asarray(E33_S23_C34)
E33_S13_C35=numpy.asarray(E33_S13_C35)
E33_S12_C36=numpy.asarray(E33_S12_C36)

C31opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,2], E33_S11_C31)
C32opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,2], E33_S22_C32)
C33opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,2], E33_S33_C33)
C34opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,2], E33_S23_C34)
C35opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,2], E33_S13_C35)
C36opt,pcov=scipy.optimize.curve_fit(func, EIJmat[:,2], E33_S12_C36)



print( "C31=", (C31opt[0]))
print( "C32=", (C32opt[0]))
print( "C33=", (C33opt[0]))
print( "C34=", (C34opt[0]))
print( "C35=", (C35opt[0]))
print( "C36=", (C36opt[0]))
print( " ")




fitC31=func(EIJmat[:,2], C31opt[0], C31opt[1])
fitC32=func(EIJmat[:,2], C32opt[0], C32opt[1])
fitC33=func(EIJmat[:,2], C33opt[0], C33opt[1])
fitC34=func(EIJmat[:,2], C34opt[0], C34opt[1])
fitC35=func(EIJmat[:,2], C35opt[0], C35opt[1])
fitC36=func(EIJmat[:,2], C36opt[0], C36opt[1])


#fig, ax1 = plt.subplots()
ax1.plot(EIJmat[:,2], E33_S11_C31, 'o')
ax1.plot(EIJmat[:,2], E33_S22_C32, 'o')
ax1.plot(EIJmat[:,2], E33_S33_C33, 'o')
ax1.plot(EIJmat[:,2], E33_S23_C34, 'o')
ax1.plot(EIJmat[:,2], E33_S13_C35, 'o')
ax1.plot(EIJmat[:,2], E33_S12_C36, 'o')



ax1.plot(EIJmat[:,2], fitC31)
ax1.plot(EIJmat[:,2], fitC32)
ax1.plot(EIJmat[:,2], fitC33)
ax1.plot(EIJmat[:,2], fitC34)
ax1.plot(EIJmat[:,2], fitC35)
ax1.plot(EIJmat[:,2], fitC36)


#plt.show()

#######################################################################
#deformation applied to E23, response S11, to calculate the constant C11
E23_S11_C41=[]
E23_S22_C42=[]
E23_S33_C43=[]
E23_S23_C44=[]
E23_S13_C45=[]
E23_S12_C46=[]

#reeding the file
fileE23 = open("E23", "r")

i=0
for line in fileE23:
        if i!=0:
                lineSplitted=line.split()
                E23_S11_C41.append(float(lineSplitted[0]))
                E23_S22_C42.append(float(lineSplitted[1]))
                E23_S33_C43.append(float(lineSplitted[2]))
                E23_S23_C44.append(float(lineSplitted[3]))
                E23_S13_C45.append(float(lineSplitted[4]))
                E23_S12_C46.append(float(lineSplitted[5]))
                #print lineSplitted
        i += 1

#print  ""
#print E23_S11_C41
#print E23_S22_C42
#print E23_S33_C43
#print E23_S23_C44
#print E23_S13_C45
#print E23_S12_C46

#print EIJ



#print EIJ
EIJ=numpy.asarray(EIJ)
#print EIJ

#Calculating the real EIJ. this is a matrix. the columns are E11 E22 E33 E23 E13 E12

EIJmat=numpy.empty([len(EIJ),6])
i=0
for delta in EIJ:
	F23=numpy.array([[1,0,0],[0,1,delta],[0,0,1]])
	EIJline=numpy.array([GreenLagrange(F23)[0,0],GreenLagrange(F23)[1,1],GreenLagrange(F23)[2,2],GreenLagrange(F23)[1,2],GreenLagrange(F23)[0,2],GreenLagrange(F23)[0,1]])
	EIJmat[i,:]=EIJline[:]
	i=i+1


#Converting list to array. Needed for the fit

E23_S11_C41=numpy.asarray(E23_S11_C41)
E23_S22_C42=numpy.asarray(E23_S22_C42)
E23_S33_C43=numpy.asarray(E23_S33_C43)
E23_S23_C44=numpy.asarray(E23_S23_C44)
E23_S13_C45=numpy.asarray(E23_S13_C45)
E23_S12_C46=numpy.asarray(E23_S12_C46)


#print "here"

#print EIJmat[:,3]
#print EIJmat[:,2]
#print C13opt[0]*numpy.ones(len(EIJ))



#print "here"


C41opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,3],EIJmat[:,2]],[C13opt[0]*numpy.ones(len(EIJ))], axis=0), E23_S11_C41)
C42opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,3],EIJmat[:,2]],[C23opt[0]*numpy.ones(len(EIJ))], axis=0), E23_S22_C42)
C43opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,3],EIJmat[:,2]],[C33opt[0]*numpy.ones(len(EIJ))], axis=0), E23_S33_C43)
C44opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,3],EIJmat[:,2]],[C34opt[0]*numpy.ones(len(EIJ))], axis=0), E23_S23_C44)
C45opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,3],EIJmat[:,2]],[C35opt[0]*numpy.ones(len(EIJ))], axis=0), E23_S13_C45)
C46opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,3],EIJmat[:,2]],[C36opt[0]*numpy.ones(len(EIJ))], axis=0), E23_S12_C46)

#print "here"

#print C41opt

#print "here"


print( "C41=", (C41opt[0]))
print( "C42=", (C42opt[0]))
print( "C43=", (C43opt[0]))
print( "C44=", (C44opt[0]))
print( "C45=", (C45opt[0]))
print( "C46=", (C46opt[0]))
print( " ")





fitC41=funcShear(numpy.append([EIJmat[:,3],EIJmat[:,2]],[C13opt[0]*numpy.ones(len(EIJ))], axis=0), C41opt[0], C41opt[1])
fitC42=funcShear(numpy.append([EIJmat[:,3],EIJmat[:,2]],[C23opt[0]*numpy.ones(len(EIJ))], axis=0), C42opt[0], C42opt[1])
fitC43=funcShear(numpy.append([EIJmat[:,3],EIJmat[:,2]],[C33opt[0]*numpy.ones(len(EIJ))], axis=0), C43opt[0], C43opt[1])
fitC44=funcShear(numpy.append([EIJmat[:,3],EIJmat[:,2]],[C34opt[0]*numpy.ones(len(EIJ))], axis=0), C44opt[0], C44opt[1])
fitC45=funcShear(numpy.append([EIJmat[:,3],EIJmat[:,2]],[C35opt[0]*numpy.ones(len(EIJ))], axis=0), C45opt[0], C45opt[1])
fitC46=funcShear(numpy.append([EIJmat[:,3],EIJmat[:,2]],[C36opt[0]*numpy.ones(len(EIJ))], axis=0), C46opt[0], C46opt[1])

#fig, ax1 = plt.subplots()
ax1.plot(EIJmat[:,3], E23_S11_C41, 'o')
ax1.plot(EIJmat[:,3], E23_S22_C42, 'o')
ax1.plot(EIJmat[:,3], E23_S33_C43, 'o')
ax1.plot(EIJmat[:,3], E23_S23_C44, 'o')
ax1.plot(EIJmat[:,3], E23_S13_C45, 'o')
ax1.plot(EIJmat[:,3], E23_S12_C46, 'o')



ax1.plot(EIJmat[:,3], fitC41)
ax1.plot(EIJmat[:,3], fitC42)
ax1.plot(EIJmat[:,3], fitC43)
ax1.plot(EIJmat[:,3], fitC44)
ax1.plot(EIJmat[:,3], fitC45)
ax1.plot(EIJmat[:,3], fitC46)


#plt.show()

#######################################################################
#deformation applied to E13, response S11, to calculate the constant C11
E13_S11_C51=[]
E13_S22_C52=[]
E13_S33_C53=[]
E13_S23_C54=[]
E13_S13_C55=[]
E13_S12_C56=[]

#reeding the file
fileE13 = open("E13", "r")

i=0
for line in fileE13:
        if i!=0:
                lineSplitted=line.split()
                E13_S11_C51.append(float(lineSplitted[0]))
                E13_S22_C52.append(float(lineSplitted[1]))
                E13_S33_C53.append(float(lineSplitted[2]))
                E13_S23_C54.append(float(lineSplitted[3]))
                E13_S13_C55.append(float(lineSplitted[4]))
                E13_S12_C56.append(float(lineSplitted[5]))
                #print lineSplitted
        i += 1

#print  ""
#print E13_S11_C51
#print E13_S22_C52
#print E13_S33_C53
#print E13_S23_C54
#print E13_S13_C55
#print E13_S12_C56

#print EIJ
#Calculating the real EIJ. this is a matrix. the columns are E11 E22 E33 E23 E13 E12

EIJmat=numpy.empty([len(EIJ),6])
i=0
for delta in EIJ:
	F13=numpy.array([[1,0,delta],[0,1,0],[0,0,1]])
	EIJline=numpy.array([GreenLagrange(F13)[0,0],GreenLagrange(F13)[1,1],GreenLagrange(F13)[2,2],GreenLagrange(F13)[1,2],GreenLagrange(F13)[0,2],GreenLagrange(F13)[0,1]])
	EIJmat[i,:]=EIJline[:]
	i=i+1





#Converting list to array. Needed for the fit
EIJ=numpy.asarray(EIJ)
E13_S11_C51=numpy.asarray(E13_S11_C51)
E13_S22_C52=numpy.asarray(E13_S22_C52)
E13_S33_C53=numpy.asarray(E13_S33_C53)
E13_S23_C54=numpy.asarray(E13_S23_C54)
E13_S13_C55=numpy.asarray(E13_S13_C55)
E13_S12_C56=numpy.asarray(E13_S12_C56)




C51opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,4],EIJmat[:,2]],[C13opt[0]*numpy.ones(len(EIJ))], axis=0), E13_S11_C51)
C52opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,4],EIJmat[:,2]],[C23opt[0]*numpy.ones(len(EIJ))], axis=0), E13_S22_C52)
C53opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,4],EIJmat[:,2]],[C33opt[0]*numpy.ones(len(EIJ))], axis=0), E13_S33_C53)
C54opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,4],EIJmat[:,2]],[C34opt[0]*numpy.ones(len(EIJ))], axis=0), E13_S23_C54)
C55opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,4],EIJmat[:,2]],[C35opt[0]*numpy.ones(len(EIJ))], axis=0), E13_S13_C55)
C56opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,4],EIJmat[:,2]],[C36opt[0]*numpy.ones(len(EIJ))], axis=0), E13_S12_C56)



print( "C51=", (C51opt[0]))
print( "C52=", (C52opt[0]))
print( "C53=", (C53opt[0]))
print( "C54=", (C54opt[0]))
print( "C55=", (C55opt[0]))
print( "C56=", (C56opt[0]))
print( " ")




fitC51=funcShear(numpy.append([EIJmat[:,4],EIJmat[:,2]],[C13opt[0]*numpy.ones(len(EIJ))], axis=0), C51opt[0], C51opt[1])
fitC52=funcShear(numpy.append([EIJmat[:,4],EIJmat[:,2]],[C23opt[0]*numpy.ones(len(EIJ))], axis=0), C52opt[0], C52opt[1])
fitC53=funcShear(numpy.append([EIJmat[:,4],EIJmat[:,2]],[C33opt[0]*numpy.ones(len(EIJ))], axis=0), C53opt[0], C53opt[1])
fitC54=funcShear(numpy.append([EIJmat[:,4],EIJmat[:,2]],[C34opt[0]*numpy.ones(len(EIJ))], axis=0), C54opt[0], C54opt[1])
fitC55=funcShear(numpy.append([EIJmat[:,4],EIJmat[:,2]],[C35opt[0]*numpy.ones(len(EIJ))], axis=0), C55opt[0], C55opt[1])
fitC56=funcShear(numpy.append([EIJmat[:,4],EIJmat[:,2]],[C36opt[0]*numpy.ones(len(EIJ))], axis=0), C56opt[0], C56opt[1])

#fig, ax1 = plt.subplots()
ax1.plot(EIJmat[:,4], E13_S11_C51, 'o')
ax1.plot(EIJmat[:,4], E13_S22_C52, 'o')
ax1.plot(EIJmat[:,4], E13_S33_C53, 'o')
ax1.plot(EIJmat[:,4], E13_S23_C54, 'o')
ax1.plot(EIJmat[:,4], E13_S13_C55, 'o')
ax1.plot(EIJmat[:,4], E13_S12_C56, 'o')





ax1.plot(EIJmat[:,4], fitC51)
ax1.plot(EIJmat[:,4], fitC52)
ax1.plot(EIJmat[:,4], fitC53)
ax1.plot(EIJmat[:,4], fitC54)
ax1.plot(EIJmat[:,4], fitC55)
ax1.plot(EIJmat[:,4], fitC56)


#plt.show()

#######################################################################
#deformation applied to E12, response S11, to calculate the constant C11
E12_S11_C61=[]
E12_S22_C62=[]
E12_S33_C63=[]
E12_S23_C64=[]
E12_S13_C65=[]
E12_S12_C66=[]

#reeding the file
fileE12 = open("E12", "r")

i=0
for line in fileE12:
        if i!=0:
                lineSplitted=line.split()
                E12_S11_C61.append(float(lineSplitted[0]))
                E12_S22_C62.append(float(lineSplitted[1]))
                E12_S33_C63.append(float(lineSplitted[2]))
                E12_S23_C64.append(float(lineSplitted[3]))
                E12_S13_C65.append(float(lineSplitted[4]))
                E12_S12_C66.append(float(lineSplitted[5]))
                #print lineSplitted
        i += 1

#print  ""
#pdcrint E12_S11_C61
#print E12_S22_C62
#print E12_S33_C63
#print E12_S23_C64
#print E12_S13_C65
#print E12_S12_C66

#print EIJ

#Calculating the real EIJ. this is a matrix. the columns are E11 E22 E33 E23 E13 E12

EIJmat=numpy.empty([len(EIJ),6])
i=0
for delta in EIJ:
	F12=numpy.array([[1,delta,0],[0,1,0],[0,0,1]])
	EIJline=numpy.array([GreenLagrange(F12)[0,0],GreenLagrange(F12)[1,1],GreenLagrange(F12)[2,2],GreenLagrange(F12)[1,2],GreenLagrange(F12)[0,2],GreenLagrange(F12)[0,1]])
	EIJmat[i,:]=EIJline[:]
	i=i+1




#Converting list to array. Needed for the fit
EIJ=numpy.asarray(EIJ)
E12_S11_C61=numpy.asarray(E12_S11_C61)
E12_S22_C62=numpy.asarray(E12_S22_C62)
E12_S33_C63=numpy.asarray(E12_S33_C63)
E12_S23_C64=numpy.asarray(E12_S23_C64)
E12_S13_C65=numpy.asarray(E12_S13_C65)
E12_S12_C66=numpy.asarray(E12_S12_C66)

C61opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,5],EIJmat[:,1]],[C12opt[0]*numpy.ones(len(EIJ))], axis=0), E12_S11_C61)
C62opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,5],EIJmat[:,1]],[C22opt[0]*numpy.ones(len(EIJ))], axis=0), E12_S22_C62)
C63opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,5],EIJmat[:,1]],[C23opt[0]*numpy.ones(len(EIJ))], axis=0), E12_S33_C63)
C64opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,5],EIJmat[:,1]],[C24opt[0]*numpy.ones(len(EIJ))], axis=0), E12_S23_C64)
C65opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,5],EIJmat[:,1]],[C25opt[0]*numpy.ones(len(EIJ))], axis=0), E12_S13_C65)
C66opt,pcov=scipy.optimize.curve_fit(funcShear, numpy.append([EIJmat[:,5],EIJmat[:,1]],[C26opt[0]*numpy.ones(len(EIJ))], axis=0), E12_S12_C66)




print( "C61=", (C61opt[0]))
print( "C62=", (C62opt[0]))
print( "C63=", (C63opt[0]))
print( "C64=", (C64opt[0]))
print( "C65=", (C65opt[0]))
print( "C66=", (C66opt[0]))
print( " ")




fitC61=funcShear(numpy.append([EIJmat[:,5],EIJmat[:,1]],[C12opt[0]*numpy.ones(len(EIJ))], axis=0), C61opt[0], C61opt[1])
fitC62=funcShear(numpy.append([EIJmat[:,5],EIJmat[:,1]],[C22opt[0]*numpy.ones(len(EIJ))], axis=0), C62opt[0], C62opt[1])
fitC63=funcShear(numpy.append([EIJmat[:,5],EIJmat[:,1]],[C23opt[0]*numpy.ones(len(EIJ))], axis=0), C63opt[0], C63opt[1])
fitC64=funcShear(numpy.append([EIJmat[:,5],EIJmat[:,1]],[C24opt[0]*numpy.ones(len(EIJ))], axis=0), C64opt[0], C64opt[1])
fitC65=funcShear(numpy.append([EIJmat[:,5],EIJmat[:,1]],[C25opt[0]*numpy.ones(len(EIJ))], axis=0), C65opt[0], C65opt[1])
fitC66=funcShear(numpy.append([EIJmat[:,5],EIJmat[:,1]],[C26opt[0]*numpy.ones(len(EIJ))], axis=0), C66opt[0], C66opt[1])

#fig, ax1 = plt.subplots()
ax1.plot(EIJmat[:,5], E12_S11_C61, 'o')
ax1.plot(EIJmat[:,5], E12_S22_C62, 'o')
ax1.plot(EIJmat[:,5], E12_S33_C63, 'o')
ax1.plot(EIJmat[:,5], E12_S23_C64, 'o')
ax1.plot(EIJmat[:,5], E12_S13_C65, 'o')
ax1.plot(EIJmat[:,5], E12_S12_C66, 'o')





ax1.plot(EIJmat[:,5], fitC61)
ax1.plot(EIJmat[:,5], fitC62)
ax1.plot(EIJmat[:,5], fitC63)
ax1.plot(EIJmat[:,5], fitC64)
ax1.plot(EIJmat[:,5], fitC65)
ax1.plot(EIJmat[:,5], fitC66)



plt.show()


#####################################################################
#Converting Voigt to tensor notation

#writing voigt matrix

C_Voigt=numpy.array([	[C11opt[0],C12opt[0],C13opt[0],C14opt[0],C15opt[0],C16opt[0]],
			[C21opt[0],C22opt[0],C23opt[0],C24opt[0],C25opt[0],C26opt[0]],
			[C31opt[0],C32opt[0],C33opt[0],C34opt[0],C35opt[0],C36opt[0]],
			[C41opt[0],C42opt[0],C43opt[0],C44opt[0],C45opt[0],C46opt[0]],
			[C51opt[0],C52opt[0],C53opt[0],C54opt[0],C55opt[0],C56opt[0]],
			[C61opt[0],C62opt[0],C63opt[0],C64opt[0],C65opt[0],C66opt[0]]])


print( "----------------------------------------------")
print( "Voigt Matrix")
print( C_Voigt)

C_tensor=numpy.empty(81).reshape(3,3,3,3)


#print C_tensor


#C_tensor[0][0][0][0]=1



for i in range(0, 3):
        for j in range(0, 3):
                for k in range(0, 3):
                        for l in range(0, 3):
                                if i==0 and j==0:
                                        if k==0 and l==0:
                                                C_tensor[i][j][k][l]=C_Voigt[0][0]
                                        if k==1 and l==1:
                                                C_tensor[i][j][k][l]=C_Voigt[0][1]
                                        if k==2 and l==2:
                                                C_tensor[i][j][k][l]=C_Voigt[0][2]
                                        if (k==1 and l==2) or (k==2 and l==1):
                                                C_tensor[i][j][k][l]=C_Voigt[0][3]
                                        if (k==0 and l==2) or (k==2 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[0][4]
                                        if (k==0 and l==1) or (k==1 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[0][5]


                                if i==1 and j==1:
                                        if k==0 and l==0:
                                                C_tensor[i][j][k][l]=C_Voigt[1][0]
                                        if k==1 and l==1:
                                                C_tensor[i][j][k][l]=C_Voigt[1][1]
                                        if k==2 and l==2:
                                                C_tensor[i][j][k][l]=C_Voigt[1][2]
                                        if (k==1 and l==2) or (k==2 and l==1):
                                                C_tensor[i][j][k][l]=C_Voigt[1][3]
                                        if (k==0 and l==2) or (k==2 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[1][4]
                                        if (k==0 and l==1) or (k==1 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[1][5]


                                if i==2 and j==2:
                                        if k==0 and l==0:
                                                C_tensor[i][j][k][l]=C_Voigt[2][0]
                                        if k==1 and l==1:
                                                C_tensor[i][j][k][l]=C_Voigt[2][1]
                                        if k==2 and l==2:
                                                C_tensor[i][j][k][l]=C_Voigt[2][2]
                                        if (k==1 and l==2) or (k==2 and l==1):
                                                C_tensor[i][j][k][l]=C_Voigt[2][3]
                                        if (k==0 and l==2) or (k==2 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[2][4]
                                        if (k==0 and l==1) or (k==1 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[2][5]


                                if (i==1 and j==2) or (i==2 and j==1):
                                        if k==0 and l==0:
                                                C_tensor[i][j][k][l]=C_Voigt[3][0]
                                        if k==1 and l==1:
                                                C_tensor[i][j][k][l]=C_Voigt[3][1]
                                        if k==2 and l==2:
                                                C_tensor[i][j][k][l]=C_Voigt[3][2]
                                        if (k==1 and l==2) or (k==2 and l==1):
                                                C_tensor[i][j][k][l]=C_Voigt[3][3]
                                        if (k==0 and l==2) or (k==2 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[3][4]
                                        if (k==0 and l==1) or (k==1 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[3][5]


                                if (i==0 and j==2) or (i==2 and j==0):
                                        if k==0 and l==0:
                                                C_tensor[i][j][k][l]=C_Voigt[4][0]
                                        if k==1 and l==1:
                                                C_tensor[i][j][k][l]=C_Voigt[4][1]
                                        if k==2 and l==2:
                                                C_tensor[i][j][k][l]=C_Voigt[4][2]
                                        if (k==1 and l==2) or (k==2 and l==1):
                                                C_tensor[i][j][k][l]=C_Voigt[4][3]
                                        if (k==0 and l==2) or (k==2 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[4][4]
                                        if (k==0 and l==1) or (k==1 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[4][5]


                                if (i==0 and j==1) or (i==1 and j==0):
                                        if k==0 and l==0:
                                                C_tensor[i][j][k][l]=C_Voigt[5][0]
                                        if k==1 and l==1:
                                                C_tensor[i][j][k][l]=C_Voigt[5][1]
                                        if k==2 and l==2:
                                                C_tensor[i][j][k][l]=C_Voigt[5][2]
                                        if (k==1 and l==2) or (k==2 and l==1):
                                                C_tensor[i][j][k][l]=C_Voigt[5][3]
                                        if (k==0 and l==2) or (k==2 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[5][4]
                                        if (k==0 and l==1) or (k==1 and l==0):
                                                C_tensor[i][j][k][l]=C_Voigt[5][5]




#print C_tensor


#####################################################################
#Calculating the eigenvalues of C_Voigt
val, vect =  numpy.linalg.eig(C_Voigt)
print( "----------------------------------------------")
print( "Eigenvalues of C")
print( val)


#####################################################################
#Bulk modulus Voigt
B_0 = (1.0/9.0) * (C_Voigt[0,0]+C_Voigt[0,1]+C_Voigt[0,2]+\
		   C_Voigt[1,0]+C_Voigt[1,1]+C_Voigt[1,2]+\
	           C_Voigt[2,0]+C_Voigt[2,1]+C_Voigt[2,2])


print( "----------------------------------------------")
print( "Bulk Modulus Voigt")
print( B_0)


####################################################################
#Bulk modulus Nye
S_Voigt=numpy.linalg.inv(C_Voigt)

B_0 = 1/(S_Voigt[0,0]+S_Voigt[0,1]+S_Voigt[0,2]+\
       S_Voigt[1,0]+S_Voigt[1,1]+S_Voigt[1,2]+\
       S_Voigt[2,0]+S_Voigt[2,1]+S_Voigt[2,2])

print( "----------------------------------------------")
print( "Bulk Modulus Nye")
print( B_0)


####################################################################


#####################################################################
#Shear modulus Voigt

G_0 = (1.0/15.0) * (C_Voigt[0,0]+C_Voigt[1,1]+C_Voigt[2,2]-\
                    C_Voigt[0,1]-C_Voigt[1,2]-C_Voigt[0,2])+\
      (1.0/5.0) *  (C_Voigt[3,3]+C_Voigt[4,4]+C_Voigt[5,5])


print( "----------------------------------------------"  )
print( "Shear Modulus Voigt")
print( G_0)

#####################################################################
#poisson ratio

v=(3*B_0-2*G_0)/(2*(3*B_0+G_0))


print( "----------------------------------------------")
print( "Poisson ratio")
print( v)




