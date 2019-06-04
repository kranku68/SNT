#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:11:08 2019

@author: gilles
"""

from PIL import Image

im=Image.open("maureen.jpg")
im.show()

print(im.size,im.format)