# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:45:17 2026

@author: HP
"""
# 24-dars

natija = lambda a,b : a+b
print( natija(2,3))

kub = lambda a : a**3
print(kub(3))

kattasi = lambda a, b : max(a,b)
print(kattasi(5,4))

sonlari = [1,2,3,4,5]
kvadrati =list(map(lambda x:x*x,sonlari))
print(kvadrati)

sonlar = [2,4,6,8]
kopaytma = list(map(lambda x: x*2, sonlar))
print(kopaytma)

ismlar = ['ali','vali','hasan']
katta_hrfda = list(map(lambda x: x.title(), ismlar))
print(katta_hrfda)

sonlar = [1,2,3,4,5,6,7,8]
juftlari =list(filter( lambda x: x%2==0, sonlar))
print(sonlar, '\n juftlari: ',juftlari)
toqlari =list(filter( lambda x: x%2!=0, sonlar))
print('toqlari:',toqlari)

mevalar = ['olma','anor','banan','shaftoli']
a_harf = list(filter( lambda x: x.startswith('a'), mevalar))
print(a_harf)

sonlar = [1,2,3,4,5,6]   
kvadrati= list(map(lambda x: x**2, list(filter(lambda x: x%2==0, sonlar))))
print(kvadrati)

sonlar = [3,5,7,9]
buyurtma = list(map( lambda x:(x**2)+10, sonlar ))
print(buyurtma)

list(filter(lambda x: x>10, map(lambda x: x*2, [3,6,8,1])))
# bu kod 3,6,8,1 bularni 2 ga kopaytirib 10 dan katta ekanini tekshiradi

from math import sqrt
sonlar = [10,15,20,25,30]
aniq=list(filter(lambda x: x%3==0 , sonlar)) 
listi=[]
for i in aniq:
    a=sqrt(i)
    listi.append(a)
print(listi)

from math import sqrt

sonlar = [10,15,20,25,30]

natija = [sqrt(x) for x in sonlar if x%3==0]
print(natija)


talabalar = [
    {'ism': 'Ali', 'yosh': 20, 'ball': 85},
    {'ism': 'Vali', 'yosh': 17, 'ball': 72},
    {'ism': 'Hasan', 'yosh': 22, 'ball': 90},
    {'ism': 'Husan', 'yosh': 19, 'ball': 65},
    {'ism': 'Olim', 'yosh': 21, 'ball': 88},
]
1
katta=list(filter( lambda y: y['yosh']>18, talabalar)) 
yuqori= list(filter(lambda b: b['ball']>80, katta ))
tartib= sorted(yuqori , key=lambda x: x['ball'], reverse=True)  
natija=list(map(lambda x:  {   'ism':x['ism'] , 'ball':x['ball'] }, tartib))
print(natija)
2
tayyor= list(map( lambda x: {'ism':x['ism'], 'ball':x['ball'], 'Status': 'Exselent' if x['ball']>=90 else 'Good' if x['ball']>=80 else 'Avarage'},   
                               sorted( filter( lambda x: x['yosh']>18 , 
                                      filter( lambda x: x['ball']>80, talabalar)), key=lambda x: x['ball'] , reverse=True))) 
print(tayyor)
