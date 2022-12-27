# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:43:47 2022

@author: Owner
"""

from PROJET1 import *

G=rectangle(4,5)
print("LE PERIMETRE DU RECTANGLE EST:",G.surface(),"\nLA SURFACE DU RECTANGLE EST:", G.surface())
L=cercle(6)
print("\nLA SURFACE DU CERCLE EST:",L.surface(),"\nLE PERIMETRE DU CERCLE EST:",L.perimetre())
O=triangle(3, 3, 3)
print("\nLA SURFACE DU TRIANGLE EST:",O.surface(),"\nLE PERIMETRE DU TRIANGLE EST:",O.perimetre())
R=carre(3,0)
print("\nLA SURFACE DU CARRE EST:",R.surface(),"\nLE PERIMETRE DU CARRE EST:",R.perimetre())
Y=trianglerectangle(7, 8, 15,0)
print("\nLA SURFACE DU TRIANGLERECTANGLE EST:",Y.surface(),"\nLE PERIMETRE DU TRIANGLERECTANGLE EST:",R.perimetre())    
    