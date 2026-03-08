# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:17:14 2026

@author: HP
"""
# 10-dars 
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['tayotta', 'mazda', 'yundai', 'gm', 'kia']
for i in cars:
   if i == 'gm': 
       i=i.upper()
   else: 
       i=i.title()
   print(i)       
cars = ['tayotta', 'mazda', 'yundai', 'gm', 'kia']
for avto in cars:
   if avto != 'gm':
       avto=avto.title()
   else:
       avto= avto.upper()
   print (avto) 
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
foydalanuvchi_ismi= input('Assalomu alaykum \nIsmingiz nima ? \n->>>>: ')
if foydalanuvchi_ismi.lower() == 'admin':
   print('Hush kelibsiz Admin ! \nFoydalanuchilar ismini ko\'rasizmi ?') 
else :
   print (f'Hush kelibsiz {foydalanuvchi_ismi.upper()} ')
# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son_1=int(input('1-son: '))
son_2=int(input('2-son: '))
if son_1>son_2:
    print(f'{son_1}>{son_2}')
if son_1<son_2:
    print(f'{son_1}<{son_2}')
if son_1==son_2:
    print(f'{son_1}={son_2}')
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
m='manfiy' 
son_1=float(input('1-sonni kiriting -> '))   
if son_1 > 0 : 
    print('musbat')
elif son_1==0 :
   print ('EROR')
else : print(m) 