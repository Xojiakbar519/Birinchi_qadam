# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:56:06 2026

@author: HP
"""
#  ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funktsiyasi yozing.
from datetime import datetime
current_year = datetime.now().year
# 19-dars
# ismi=input('ismingiz ? ')
# yosh=int(input('yoshingiz? '))
def yilini_hisoblash() :
    ismi=input('ismingiz ? ')
    yosh=int(input('yoshingiz? '))
    '''yoshini hisoblash funkisiyasi'''
    print(f'Assalomu alaykum {ismi}, siz {current_year-yosh}-yilda tug\'ulgansiz')
yilini_hisoblash()    
# son olib, uning kvadrati va kubini konsolga funktsiyasi yozing.
#  def hisoblash(kirish)  bunday yozsa ham bo'ladi bunda kirishni finksiya ichiga yozish majburiy bo'ladi yani kirish(30). bu hol huddi range(start,step,stop) ga o'xshaydi.
def hisoblash() :
    kirish=int(input('son yozing'))
    print(f'{kirish} kubi:{kirish**3} va kvadrati: {kirish**2}')
hisoblash()
# son olib, son juft yoki to'qligini konsolga funktsiyasi yozing.
def aniqla():
    '''son juft yoki toqligini aniqlovchi funksiya '''
    son=int(input('Son kiritish: '))
    if son%2==0:
        print("BU JUFT SON")
    else:
        print("BU TOQ SON")
# foydadan ikkita son, ulardan kattasini konsolga olib funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
