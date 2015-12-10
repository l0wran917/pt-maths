import numpy as np
from pylab import *
import os
import re

###############################################################

print("")
print("===============================================================================")
print("Projet - Maths Modélisation S3           |")
print("Jonathan Robillard - François Rousselet  |")
print("------------------------------------------")
print("")

###############################################################

# Lecture du fichier et création d'une matrice
f = open('brut.txt')
li = []
for ln in f:
    li.append(ln.split())
f.close()
m = np.mat(li)
m = m.astype(np.int_, copy=False)
cr = np.mat(li)
cr = cr.astype(np.int_, copy=False)
print('MATRICE D\'ORIGINE')
print(m)

# Centrage de chaque valeur
sum = 0

# On calcule la somme et la moyenne
for i in range(0, len(m)) :
	sum = sum + m[i,0]
print(sum)

moyenne = sum/len(m[:,1])
moyenne2 = (sum**2)/len(m[:,1])
print(moyenne)

#Centrage

	
for i in range(0, len(m[:,1])) :
	cr[i,0] = (m[i,0] - moyenne)
    
print(cr)
    
sumCR = 0
for i in range(0, len(m)) :
	sumCR = sumCR + cr[i,0]**2
print(sumCR)

for i in range(0, len(m[:,1])) :
	cr[i,0] = cr[i,0] / math.sqrt(1/len(m[:,1]) * sumCR)

print("")
print("MATRICE CENTREE REDUITE")
print(cr)

print("")
print("===============================================================================")
print("")
