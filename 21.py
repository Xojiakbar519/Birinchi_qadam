# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 18:31:21 2026

@author: HP
"""
ismlar = ['ali', 'vali', 'hasan', 'husan']
ozgaruvchi=[]
def katta():
    for i in ismlar[:]:
        ozgaruvchi.append(i.title())
        ismlar.remove(i)
    print(ozgaruvchi)
