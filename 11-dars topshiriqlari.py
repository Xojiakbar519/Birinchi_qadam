# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:35:08 2026

@author: HP
"""
# 11-dars
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
j_s=float(input('juft son kirirting: '))
if j_s % 2 == 0:
    print('Rahmat juft son kiritganiz uchun !')
else : print('siz kiritgan son juft emas !')
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring: Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepulAgar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
f_yoshi=int(input('iltimos yoshingizni yozing : '))
if f_yoshi<=4 or f_yoshi>=60 :
    print('Sizga krish bepul ')
elif f_yoshi<18 and f_yoshi>4 :
    print('kirish narxi 10 000 so\'m')
else : print('kirish 20 000 so\'m')
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
print ('Iltimos so\'lishtirish uchun ikkita son kiriting : \n')
son_1=float(input(" 1- son : "))
son_2=float(input(" 2- son : "))
if son_1 > son_2:
    print(f'{son_1} > {son_2} ')
elif son_1 == son_2:
    print(f'{son_1} = {son_2} ')
else: print(f'{son_1} < {son_2} ')
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mevalar = [ 'anor', 'anjir', 'uzum', 'nok', 'olma', 'behi', 'mandarin' ]
savat=[]
for i in range(3):
    kiritish=input(f'{i+1} - meva : ')
    savat.append(kiritish)
for meva in savat : 
    if meva in mevalar :
        print(f'bizning omborda {meva} bor')
    else:
        print(f'bizning omborda {meva} yoq')
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
mevalar = [ 'anor', 'anjir', 'uzum', 'nok', 'olma', 'behi', 'mandarin' ]
bor=[]
yoq=[]
for i in range(5):
    kiritish=str(input().lower())
    if kiritish in mevalar :
        bor.append(kiritish)
    else : 
        yoq.append(kiritish)
print('bizda quyidagilar bor : ')
for i in bor:
    print(i)
print('bizda quyidagilar yoq : ')
for i in yoq:
    print(i)
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
foydalanuvchi=['zulayho','hushnud','bekzod']
k=str((input().lower()).strip())
if k in foydalanuvchi:
    print(" Iltimos boshqa login tanlang ")
else:
    foydalanuvchi.append(k)
    print('hush kelibsiz ')
# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
son=int(input('Butun son kiriting: '))
for i in range(2,11,2):
    if son%i==0:
        print(f'son {i} ga qoldiqsiz bo\'linadi')
    else:
        print(f'son {i} ga qoldiqli bo\'linadi')