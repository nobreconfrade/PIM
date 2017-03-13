# -*- coding: cp1252 -*-
from PIL import Image
import time
import numpy as np
pil1=Image.open('insetoGray.jpg')
pil2=Image.open('insetoGray_B.jpg')

(l1,h1)=pil1.size
(l2,h2)=pil2.size
print(l1,h1)
print(l2,h2)
u=0
out=Image.new(pil1.mode, (l1,h1))
#####################  Inefficient
#for j in range(0, h1):
#    for i in range(0, l1):
#        new=(1-u)* pil1.getpixel((i,j)) + u * pil2.getpixel((i,j))
#        out.putpixel((i,j),new)
#out.show()
#time.sleep(30)
#out.save("outExMorph.jpg","JPEG")

####################  Efficient: without loops
for u in range(0,11,1): 
	M1=np.array(pil1)
	M2=np.array(pil2)
	M3=(1-(u*0.1))*M1+(u*0.1)*M2

## numpyarray to image
##    First ensure your numpy array, myarray, is normalised with the max value at 1.0.
##    Convert to integers, using np.uint8().
##    Use Image.fromarray()
	out = Image.fromarray(np.uint8(M3))
#out.show()
#time.sleep(10)
	out.save("outExMorph"+str(u)+"_fast.jpg","JPEG")
