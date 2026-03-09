# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:14:31 2026

@author: HP
"""
# 18-dars
# foydadan buyurtma qabul qilish dastur yozing. Ular nomini birma-bir qabul qilib, yangi ro' mahsulotlar joylang.
# e-bozor uchun mahsulotlar va hujjat narhlari lug'atini shakllantiruvchi dastur yozing. samaralidan lug'atga bir nechta mahsulot (mahsulot va uning narhi) mahsulotlarini so'rang.
# Yuqoridagi ikki dasturni jamlaymiz. samarali buyurtmasi ro'yxatidagi har qanday e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxatini olishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
baza={'anor':10000}
print('foydalanuvchimisiz yoki ishchi')
a=str(input('>>: '))
if a=='ishchi':
    print('Buyurtma qabul qilish dasturi ishga tushdi')
    while True:
        nom=str(input('Mahsulot nomini kiriting: '))
        narx=float(input('Mahsulot narxi qancha: '))
        baza[nom]=narx
        soroq=str(input('Yana mahsulot bormi? (ha/yoq)'))
        if soroq=='yoq':
            break
elif a=='foydalanuvchi':
    while True:
        foydalanuvchi=input('nima sotib olmoqchisiz ? : ')
        if foydalanuvchi in baza:
               print(f'Siz soragan {foydalanuvchi} narxi: {baza[foydalanuvchi]}')
        else:
               print('mavjudmas')
        soroq=str(input('Yana mahsulot olasizmi? (ha/yoq)'))
        if soroq=='yoq': 
            break