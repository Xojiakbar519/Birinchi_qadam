# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 09:54:30 2026

@author: HP
"""
# 9-dars

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
royhat=['salima', 'karim', 'malika', 'Sevara', 'Muslima']
for i in royhat:
        print(f'{i.capitalize()} Dunyo go\'zallari festivaliga borasizmi')
# uoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print(f'kod {len(royhat)} marta takrorlandi')

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toq_sonlar=[]
for i in range(11,100,2):
    toq_sonlar.append(i)
for i in toq_sonlar:
    print(f'{i} toq son kubi {i**3}')
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
sevimli_kinolar=[]
for i in range(5):
    sevimli_kinolar.append(f'{i+1}-kino:{input(f'Siz yoqtirgan {i+1}-kino: ')}')
for royhat in sevimli_kinolar:
    print('Siz yoqtirgan ', royhat)
    
        

