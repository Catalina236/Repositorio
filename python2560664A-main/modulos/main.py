#import modulo

import random
import sys

for p in sys.path:
    print(p)

print(random.randint(1,10))
import sys
from sys import path
#path.append('..\\MiPracticaPythonA\\modulos')

path.append('C:\\Users\\usuario\\Dropbox\\sena2022\\Trimestre4-06octubre-17diciembre\\MiPracticaPythonA\\modulos')

import module
#from modulo1 import suml,prodl
Lista=[]
for i in range(5):
    Lista.append(random.randint(1,100))
print(module.suml(Lista))
