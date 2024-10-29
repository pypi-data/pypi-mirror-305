# Leitura e escrita.

from skimage.io import imread, imsave

def read_image(path, is_gray = False):
    image = imread(path)
    if is_gray:
        image = rgb2gray(image)
    return image

def save_image(image, path):
    imsave(path, image)