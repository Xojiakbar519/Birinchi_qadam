# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:34:23 2026

@author: HP
"""
# 8-dars
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar=['Uzbekistan', 'Qirg\'iziston','Tojikiston','Turkmaniston', 'Qozog\'iston' ]

# sorted()yordam ro'yxatni tartiblangan holda  chiqaring
tartiblangan=sorted(davlatlar)
# sorted()yordam ro'xtani teskari konsolga chiqaring
teskari=sorted(davlatlar, reverse=True)
# 120dan 1200gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar=[]
for i in range(120,1200,2):
    sonlar.append(i)
print(sonlar)
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar))
# Ro'yxatdagi eng katta va eng kichik son o'zining ayirmani hisoblang va konsolga chiqaring
print(max(sonlar)-min(sonlar))
# Ro'yxatdagi maqola sonini hisoblang
print(len(sonlar))
# Ro'yxatning narxin, o'rtadan va boshidan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
# taomlardegan ro'xat yarating va ichimlik 5ta taomni kiriting
taomlar=['mastav', 'moshxorda', 'chuchvar', 'manti', 'kabob']
nonushta=[]
nonushta=taomlar[3:]

