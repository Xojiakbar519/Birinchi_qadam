# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:58:17 2026

@author: HP
"""

# 7-dars
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
ismlar=['Abror', 'Burxon', 'Sevara']
print(f'Assalomu alaykum, {ismlar[0]} ishlaring yaxshimi ?')
print(f'{ismlar[1]} bugun o\'qishga borasanmi? ')
print(f'Kelayotgan 8-mart bilan {ismlar[2]}')
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
sonlar=[1, -2, 2.8]
print(f'sonlar yig\'indisi: {sum(sonlar)}' )
print(sonlar[0]-sonlar[1]+sonlar[2])
# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
t_shaxslar=['Bobur', 'Salim', 'Karim']
z_shaxslar=['Mirzohid', 'Muborak', 'Temur']
print(f'men tarixiy shaxlardan {t_shaxslar[0]} bilan, zamonaviy shaxslardan {z_shaxslar[0]} bilan suhbat qurishni hohlardim')
print(f'men tarixiy shaxlardan {t_shaxslar[1]} bilan, zamonaviy shaxslardan {z_shaxslar[1]} bilan suhbat qurishni hohlardim')
print(f'men tarixiy shaxlardan {t_shaxslar[2]} bilan, zamonaviy shaxslardan {z_shaxslar[2]} bilan suhbat qurishni hohlardim')
olingan_malumotlar=[]
olingan_malumotlar.append(t_shaxslar.pop(0))
# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends=[]
friends.append(str(input('taklif qilmoqchi bo\'lgan do\'stingiz: ')))
print('taklif qildingiz : ', friends[0])
# qo'shimcha idea
friends=[]
for i in range(6):
    friends.append(str(input('taklif qilmoqchi bo\'lgan do\'stingiz: ')))
print('siz quyidagilarni taklif qildingiz: ')
for taklif in friends:
    print(f'{taklif}')
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
kelmaydi=[]
kelmaydi.append(str(input('kelmaydigon 1 kishi:')))
friends.remove(kelmaydi[0])
print('keladigonlar royhati')
for taklif in friends:
    print(f'{taklif}')
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(3,input('Yangi odam:'))

