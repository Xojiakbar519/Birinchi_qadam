# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:32:25 2026

@author: HP
"""
#  22 - dars
1
def kopaytma(*sonlar):
    a=1
    for i in sonlar:
        a=a*i
    print(a)
    
2
def malumotnoma(ism,familya,**malumot):
    malumot['Talaba ismi']=ism
    malumot['Talaba familyasi']=familya
    for qiymat , k in  malumot.items():
        print( qiymat, ':', k, end='   ')
        
    
