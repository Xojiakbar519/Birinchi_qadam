# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:05:44 2026

@author: HP
"""
# 6-dars
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
son=int(input("Son kiriting: "))
kvadrati=son**2
kubi=son**3
print(f"kiritilgan son({son}) kvadrati : {kvadrati}, kubi esa {kubi}")
# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
yoshi=int(input("yoshingizni kiriting: "))
from datetime import datetime
year = datetime.now().year
t_yil=year-yoshi
print('tug\'ilgan yilingiz: ', t_yil)
# foydadan ikkilanishni so'rab bo'lib o'g'illarning yig'indi, ayirmasi, ko'paytmasi va'linmasini kiritadigan dastur dastur
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}x{b}=", a*b)
print(f"{a}/{b}=", a/b)