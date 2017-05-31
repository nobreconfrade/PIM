
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from PIL import Image

pil1=Image.open('mapaEUA.jpg')
(l,h)=pil1.size
print("Tamanho do arquivo:")
print(l,h)

Iout=Image.new('RGB', (l,h))

for j in range(0, h):
    for i in range(0, l):
        val=pil1.getpixel((i,j))
        # print M[val,0:3]
        if val == 255:
            Iout.putpixel((i,j),(255,255,255))
        if 104 < val < 108:
            Iout.putpixel((i,j),(171,30,30))
        if 126 < val < 130:
            Iout.putpixel((i,j),(76,81,228))
        if 158 < val < 162:
            Iout.putpixel((i,j),(228,138,59))

Iout.show()
Iout.save("mapapintado.jpg","JPEG")
