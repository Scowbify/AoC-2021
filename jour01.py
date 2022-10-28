"""--------------------------------
Importations de fonctions externes :
--------------------------------"""

import numpy

"""--------------------------------
Parametres globaux :
--------------------------------"""

source = numpy.loadtxt('/Users/marchais/Desktop/AdventOfCode/jour01-1.txt',int)

"""--------------------------------
Definitions locales de fonctions  :
--------------------------------"""


"""--------------------------------
Corps principal du programme(Main):
--------------------------------"""

n = len(source)

compt = 0

for i in range (1,n):
    if source[i]>source[i-1]:
        compt += 1
        
print(compt)


compt = 0

for i in range (3,n):
    if source[i]>source[i-3]:
        compt += 1
        
print(compt)