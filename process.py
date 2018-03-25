from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
import numpy
import scipy
from scipy import ndimage

orginial_image = scipy.misc.imread("pill.jpg")
inverted_image = numpy.invert(orginial_image)



im = im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('sobel.jpg', mag)
#enhancer = ImageEnhance.Sharpness(im)
#f = 1
#inter = enhancer.enhance(f)
#enhancer = ImageEnhance.Contrast(inter)
#nhancer.enhance(1).show("Sharpness %f" % f) '''

