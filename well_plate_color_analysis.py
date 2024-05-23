import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale
from opencv_basics_BGR import histogram_BGR
import numpy as np

def binary_mask(wellimage):
    bwmask = wellimage.copy()

if __name__ == '__main__':
    well_image_location = 'colorplate.png'
    well_image_read = cv2.imread(well_image_location)
    cv2.imshow(f'{well_image_location} - original', well_image_read) 