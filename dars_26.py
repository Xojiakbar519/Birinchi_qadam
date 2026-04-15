# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:57:50 2026

@author: HP
"""
# dars _ 26 
from uzwords import words as baza
import random 

soz=random.choice(baza)
olcham=len(soz)
harfiy=[]
salom=[]
for s in soz:
    harfiy.append(s)
    salom.append('_')
while True:
    print( salom )
    kiriting=input('bitta harf kiriting: ')
    for i in range(olcham):
        if harfiy[i]==kiriting:
            salom[i]=kiriting
    if salom==harfiy:
        break
        
print(soz)
