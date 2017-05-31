from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from PIL import Image

def figEscura():
    pil1=Image.open('figuraEscura.jpg')
    (l,h)=pil1.size
    print("Tamanho do arquivo:")
    print(l,h)

    Iout=Image.new('RGB', (l,h))

    for j in range(0, h):
        for i in range(0, l):
            val=pil1.getpixel((i,j))
            # print M[val,0:3]
            if val != 16:
                Iout.putpixel((i,j),(randint(0,255),randint(0,255),randint(0,255)))
            else:
                Iout.putpixel((i,j),(val,val,val))
                Iout.show()
                Iout.save("mapapintado.jpg","JPEG")



figEscura()
