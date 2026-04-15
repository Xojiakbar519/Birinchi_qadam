# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:17:42 2026

@author: HP
"""
# dars 25 
import random

# print('Assalomu alaykum')
# sonlar_toplami=list(range(0,1000))
# while True:
#     tasodif=random.choice(sonlar_toplami)
#     print(f'Men bir son oyladim topingchi ? uzunligi={len(str(tasodif))}  ')
#     while True:
#         kirit=int(input(': '))
#         if kirit==tasodif:
#             print('Tabriklayman topdiz ')
#             break
#         else:
#             if kirit>tasodif:
#                 print('kichikroq son')
#             else:
#                 print('kattaroq son')
#             print('harakat qilib ko\'ring')
        
#     break



# print('0 dan 100 gacha son oylang ')
# royhat=[]
# a=0
# b=100
# while True:
#     tasodif=random.randint(a, b)
#     if len(royhat)>90:
#         print('ERROR. Hamma son aytildi !!! ')
#         break
#     elif tasodif in royhat:
#         continue
#     elif tasodif < 10 :
#         continue
#     else:
#         print(f'{a} va {b} lar orasidan:')
#         royhat.append(tasodif)
#         print(' siz o\'ylagan son : ' , tasodif )
#         soroq=input(' to\'g\'rimi ? ha/yoq')
#         if soroq=='ha':
#             print(' son topildi ! ')
#             break
#         savol=(input('ayta olasizmi son kattaroqmi yoki kichikroq? katta / kichik')).lower()
#         if savol=='katta':
#             a=tasodif
#         elif savol=='kichik':
#             b=tasodif
#         if a+1==b:
#             print(' Hatolik orada son qolmadi tanlashga !')
#             break



a = 0
b = 1_000_000_000 # 0 dan 10

while True:
    tasodif = (a + b) // 2
    print(f"{a} va {b} orasidan taxmin: {tasodif}")

    soroq = input("to‘g‘rimi? (h/y): ").lower()

    if soroq == 'h':
        print('Son topildi!')
        break

    savol = input("kattaroqmi yoki kichikroq? (kat/kich): ").lower()

    if savol == 'kat':
        a = tasodif + 1
    elif savol == 'kich':
        b = tasodif - 1

    if a > b:
        print("Xatolik! Noto‘g‘ri javob berildi.")
        break
            