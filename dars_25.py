# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:17:42 2026

@author: HP
"""
# dars 25 
import random

# print('Assalomu alaykum')
# sonlar_toplami=list(range(0,5))
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
print('Bir son oylang ')
b=int(input('necha xonali ?: '))
hajmi=10**b
a=0
while True:
    k_oy=random.randint(a,hajmi)
    print(f' {k_oy} tog\'rimi? ')
    javob=input('to\'ri bo\'lsa h, Xato bo\'lsa y: ')
    if javob=='h':
        print('Topdimmi 😁')
        break
    else: 
        savol=input('kattaroqmi kichikromi?  katta bo\'lsa k yoki ki: ')
        if savol=='k':
            a = k_oy+1
            
            
        elif savol=='ki': 
            hajmi = k_oy-1
            
        
         
      
        
    