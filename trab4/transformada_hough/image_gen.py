import scipy.misc
import scipy.ndimage
import numpy as np

img = np.zeros((50,50))
img[10:40, 10:40] = np.eye(30)
# NOTE: The magic
img = scipy.ndimage.interpolation.rotate(img,45)
scipy.misc.imsave('imgs/initial_45.png', img)
