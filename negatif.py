#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Tue May 14 13:11:08 2019
@author: gilles.naviliat@ac-nice.fr

"""


# importation des librairies nécessaires
import sys
from PIL import Image,ImageChops

# ouverture du fichier image utilisé
ImageFile = 'maureen.jpg'
try:
   img = Image.open(ImageFile)
except IOError:
    print ('Erreur sur ouverture du fichier ' + ImageFile)
    exit(1)

# récupération des dimensions de l'image (largeur, hauteur)
colonne,ligne = img.size

# création d'une image de même type que l'image originale, mais vide
imgF = Image.new(img.mode,img.size)

#boucle de traitement des pixels
for i in range(ligne):
    for j in range(colonne):
        pixel = img.getpixel((j,i))
        # on calcule le complement ‡ MAX pour chaque composante - effet négatif
        p = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
        # composition de la nouvelle image
        imgF.putpixel((j,i), p)    

# affichage de l'image créée
imgF.show()

# fermeture du fichier image initial
img.close()