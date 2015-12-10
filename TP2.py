import numpy as np
from pylab import *
import os
import re

#matrice = np.mat([[14,10],[12,11],[10,9]])
#matrice = np.mat([[110,38,6,3,1,33,4492,23],[130,63,9,3,1,35,4117,2],[150,57,5,2,1,35,4254,24]])

# Lecture du fichier et création d'une matrice
f = open('brut.txt')
li = []
for ln in f:
    li.append(ln.split())
f.close()
matrice = np.mat(li)
matrice = matrice.astype(np.float_, copy=False)
cr = np.mat(li)
cr = cr.astype(np.int_, copy=False)
d = matrice.shape # d = tableau dont 1er indice = nb lignes matrice et 2eme indice = nb colonnes

#print('MATRICE D\'ORIGINE')
#print(matrice.astype(int))


#INITIALISATION TABLEAU DE MOYENNES
moy = []
for i in range(0, d[1]) :
    moy.append(0)


#CALCUL DE LA SOMME DE CHAQUE COLONNE
for i in range(0, d[1]) :
    for j in range(0, d[0]) :
        moy[i] = moy[i] + matrice[j,i]

#ON DIVISE POUR TROUVER LA MOYENNE DE CHAQUE COLONNE
for i in range(0, d[1]) :
    moy[i] = moy[i] / d[0]

matriceCentree = matrice

#CALCUL MATRICE CENTREE
for i in range(0, d[1]) :
    for j in range(0, d[0]) :
        matriceCentree[j,i] = matriceCentree[j,i] - moy[i]

#INITIALISATION TABLEAU D'ECART TYPE
ecartType = []
for i in range(0, d[1]) :
    ecartType.append(0)

#CALCUL DES ECARTS TYPE
for i in range(0, d[1]) :
    for j in range(0, d[0]) :
        ecartType[i] = ecartType[i] + matriceCentree[j,i]**2

for i in range(0, d[1]) :
    ecartType[i] = ecartType[i] / d[0]
    ecartType[i] = sqrt(ecartType[i])

#CALCUL DE LA MATRICE CENTREE REDUITE
matriceCentreeReduite = matriceCentree
for i in range(0, d[1]) :
    for j in range(0, d[0]) :
        matriceCentreeReduite[j,i] = matriceCentreeReduite[j,i] / ecartType[i]

#print(matriceCentreeReduite.astype(int))
#print(matriceCentreeReduite)

#CALCUL MATRICE DE CORRELATION
matriceCorrelation =  np.zeros((d[1],d[1]))
for i in range(0, d[1]) :
    for j in range(0, d[1]) :
        for z in range(0, d[0]) :
            matriceCorrelation[i,j] = matriceCorrelation[i,j] + (matriceCentreeReduite[z,i]*matriceCentreeReduite[z,j])
        matriceCorrelation[i,j] = matriceCorrelation[i,j] / d[1]

print(matriceCorrelation.astype(int))




