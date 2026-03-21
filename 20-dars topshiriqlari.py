# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:59:18 2026
@author: HP
"""
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
1
baza={}
def malumotnoma(ism,familya,viloyat,pochta,yil,raqam):
    '''Malumot yig'uvchi'''
    vaqt = datetime.now().year
    royhat={
        'ism':ism,
        'familya':familya,
        'manzili':viloyat,
        'e-pochta':pochta,
        'tug\'ulgan yili':yil,
        'yoshi':vaqt-int(yil),
        'telfon raqami':raqam
        }
    return royhat
    baza[ism]=royhat
2
while True:
    from datetime import datetime
    ism=input('ism: ')
    familya=input('familya: ')
    viloyat=input('Qayerda yashaysiz: ')
    pochta=input('e-pochta: ')
    yil=input('tug\'ulgan yili:')
    raqam=input('phone number:')
    shaxs_info=malumotnoma(ism,familya,viloyat,pochta,yil,raqam)
    baza[ism]=shaxs_info
    davom_etasizmi=input('davom etasizmi ?')
    if 'yoq'==davom_etasizmi:
        break
print(baza)
3
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def aniqlovchi(a,b,c):
    kattasi=max(a,b,c)
    print(kattasi, 'kiritlgan sonlar kattasi')
4
# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
baza={}
def aylana(radiusi):
    haqida={
        'radiusi':radiusi,
        'diametri':radiusi*2,
        'perimetri':2*3.14*radiusi,
        'yuzi':3.14*radiusi**2
        }
    baza[f'radiusi:{radiusi} teng aylana haqida malumotlar']=haqida
    print('aylana haqida malumotlar:')
    for kalit,qiymat in baza[f'radiusi:{radiusi} teng aylana haqida malumotlar'].items():
        print(f' \n {kalit}={qiymat} \n')