from PIL import Image
import numpy as np

img = Image.open("imgs/output_45.png").convert("L")
shifted = np.fft.fftshift(np.fft.fft2(np.asarray(img)))

mag = np.hypot(shifted.real, shifted.imag)

mag = np.log10(mag)
t = 255.0 * mag / mag.max()
img = Image.fromarray(np.uint8(t), 'L')
img.show()
img.save("imgs/fourier_45.png")
