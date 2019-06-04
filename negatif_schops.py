#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:11:08 2019

@author: gilles
"""

# importation des librairies utilisées
import sys
from PIL import Image,ImageChops

# ouverture du fichier image
ImageFile = 'maureen.jpg'
try:
   img = Image.open(ImageFile)
except IOError:
    print ('Erreur sur ouverture du fichier ' + ImageFile)
    exit(1)

# la fonction de PIL qui donne le négatif d'une image
imgF = ImageChops.invert(img)     

# affichage de l'image
imgF.show()

# fermeture du fichier image
img.close()