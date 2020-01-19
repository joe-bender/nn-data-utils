import numpy as np

# put all pixels in the range 0-1
def squeeze_pixels(img):
    img = img/255
    return img