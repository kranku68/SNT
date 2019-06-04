#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:49:55 2019

@author: gilles
"""
from PIL import Image

# ouverture de l'image et stockage dans une variable nommée img
# en utilisant la fonction Image de la bibliothèque PIL
img = Image.open('maureen.jpg')
img.show()
# on récupère les dimensions de l'image grâce à la
# fonction size appliquée à la variable image et on les place dans un tuple
a,b=img.size
taille=(a,b)
#on affiche les valeurs de la taille

print('taille de l image :')
print('largeur :',a)
print('hauteur :',b)
bands=img.getbands()
print(bands)
extrem=img.getextrema()
print(extrem)
palette=img.getpalette()
print('palette associée :',palette)
exif_donnees = img._getexif()
print(exif_donnees)

r,g,b=img.split()
listr=list(r.getdata())
listg=list(g.getdata())
listb=list(b.getdata())

newr=Image.new("L",taille)
newr.putdata(listr)
newr.save("Maureen_R.jpg")

newg=Image.new("L",taille)
newg.putdata(listg)
newg.save("Maureen_G.jpg")

newb=Image.new("L",taille)
newb.putdata(listb)
newb.save("Maureen_B.jpg")