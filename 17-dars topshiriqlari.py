# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:54:54 2026

@author: HP
"""
# 17-dars
# yaxshi korgan kitoblarini kiritadi exit desa toxtaydi
# 1-usul
sevimli=[]
chiqish=''
while chiqish!='exit':
    a=str((input('sevimli kitobingiz (yoki exit deb yozing): ')).lower())
    if a!='exit':
        sevimli.append(a.title())
    else: chiqish=a
print(sevimli)
# 2-usul
sevimli=[]
chiqish=True
while chiqish:
    a=str(input('sevimli kitobiz yoki exit deb yozing'))
    if a=='exit':
        chiqish=False
    else: 
        sevimli.append(a.title())
print(sevimli)    
# 3-usul
sevimli=[]
while True:
    a=str(input('sevimli kitobiz yoki exit deb yozing'))
    if a=='exit':
        break
    else:
        sevimli.append(a.title())
# Muzeyga chipta yoshlar foydalanuvchining yoshiga bog'liq: 7 dan 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. foydali exityoki quitdeb yozganda dastur to'xtasin (ikkita shartni ham qiladi)
while True:
    qiymat = input('yoshingiz: ')
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    if yosh<=7:
        print('bilet narxi 2 000 so\'m')
    if 18>yosh>7:
        print('bilet narxi 3 000 so\'m')
    if 65>yosh>=18:
        print('bilet narxi 10 000 so\'m')
    if yosh>=65:
        print('bepul')
# dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    qiymat=int(qiymat)
    if qiymat<=0:
        continue
    if qiymat>0:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        