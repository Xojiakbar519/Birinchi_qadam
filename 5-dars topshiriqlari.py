# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:05:41 2026

@author: HP
"""
# 5- dars
#o'zgaruvchilarni yarating: kocha="Bog'bon" mahalla="Sog'bon" tuman="Bodomzor"  viloyat="Samarqand"
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, ko'rinishda konsolga chiqaring: Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+" tumani, "+viloyat+" viloyati")
# Yuqoridagi o'zgaruvchilarning ( kocha, mahalla, tuman, viloyat) foydalanuvchilarni so'rang. Va avvalgi mashqni takrorlang.
kocha=str(input("ko'cha: "))
mahalla=str(input("mahalla: "))
tuman=str(input("tuman: "))
viloyat=str(input("viloyat: "))
print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+" tumani, "+viloyat+" viloyati")
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print(kocha+" ko'chasi,\n"+mahalla+" mahallasi,\n"+tuman+" tumani,\n"+viloyat+" viloyati")
# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi, manzildeb nomlangan o'zgaruvchiga yuklang
manzil=f"{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# manzilga biz yuqorida o'rgangan title(), upper(), lower(), capitalize()metodlarini qo'llab ko'ring.
print(manzil.capitalize())
print(manzil.title())
print(manzil.lower())
print(manzil.upper())