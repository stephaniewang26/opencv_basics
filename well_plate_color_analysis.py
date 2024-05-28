import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale
from opencv_basics_BGR import histogram_BGR
import numpy as np

def binary_mask(wellimage):
    bwmask = wellimage.copy()
    for r, row in enumerate(bwmask):
        for c, value in enumerate(row):
            bwmask[r][c][0] = 0
            bwmask[r][c][1] = 0
            bwmask[r][c][2] = 0

    ogx=75
    ogy=73
    for i in range(4):
        ogx=75
        for k in range(12):
            cv2.circle(bwmask,(ogx,ogy),40,(255,255,255),-1)
            ogx+=129
        ogy+=129

    cv2.imwrite("bwmask.png", bwmask)
    return(bwmask)

def color_mask(bwmask):
    colormask = bwmask.copy()

    return(colormask)

if __name__ == '__main__':
    well_image_location = 'colorplate.png'
    well_image_read = cv2.imread(well_image_location)

    bw_mask_location = "bwmask.png"
    color_mask_location = "colormask.png"

    cv2.imshow(f'{well_image_location} - original', well_image_read)
    cv2.imshow(f'{bw_mask_location} - BW mask', binary_mask(well_image_read))  

    bw_mask_read = cv2.imread(bw_mask_location)

    cv2.imshow(f'{color_mask_location} - color mask', color_mask(bw_mask_read))  
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 