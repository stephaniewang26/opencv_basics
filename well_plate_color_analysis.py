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

    cv2.imwrite("plate_mask.png", bwmask)
    return(bwmask)

def color_mask(bwmask, wellimage):
    colormask = bwmask.copy()
    ogimage = wellimage.copy()

    for r, row in enumerate(bwmask):
        for c, value in enumerate(row):
            if tuple(colormask[r][c]) != (0,0,0):
                colormask[r][c] = ogimage[r][c]

    cv2.imwrite("plate_color_grid.png", colormask)
    return(colormask)

def avg_rgb_dilution(colormask):
    dilutionticks = []

    count = 1
    for i in range(12):
        dilutionticks.append(count)
        count *= 2

    ogx = 75
    ogy = 73
    rad = 40
    count = 0

    for i in range(4):
        count += 1
        ogx=75
        for k in range(12):
            avgcircle = 0
            totalpixelcircle = 0

            startx = ogx - 40
            endx = ogx+40
            starty = ogy - 40
            endy = ogy+40
            for r, row in enumerate(colormask):
                for c, value in enumerate(row):
                    for 
                        avgpixel = 0
                        if tuple(colormask[r][c]) != (0,0,0):
                            avgpixel += colormask[r][c][0] 
                            avgpixel += colormask[r][c][1]
                            avgpixel += colormask[r][c][2]
                            avgpixel /= 3
                            avgcircle += avgpixel
                            totalpixelcircle += 1

            ogx+=129
        ogy+=129

    # yellowdict = {

    # }
    # reddict = {}
    # bluedict = {}
    # greendict = {}
    # dictlist = [yellowdict,reddict,bluedict,greendict]

    # for eachdict in dictlist:
    #     for i in range(12):
    #         eachdict[i] = dict()
    #         eachdict[i]["minx"] = ogx-40
    #         eachdict[i]["maxx"] = ogx+40
    #         eachdict[i]["miny"] = ogy-40
    #         eachdict[i]["maxy"] = ogy+40

    #         ogx += 129
    #         ogy += 129

    # print(dictlist)

    # for eachdict in dictlist:
    #     for eachkey in eachdict:
    #         avgcircle = 0
    #         xrange = eachdict[eachkey]["maxx"] - eachdict[eachkey]["minx"]
    #         yrange = eachdict[eachkey]["maxy"] - eachdict[eachkey]["miny"]
            
                

    
    print(dilutionticks)

if __name__ == '__main__':
    well_image_location = 'colorplate.png'
    well_image_read = cv2.imread(well_image_location)

    bw_mask_location = "plate_mask.png"
    color_mask_location = "plate_color_grid.png"

    cv2.imshow(f'{well_image_location} - original', well_image_read)
    cv2.imshow(f'{bw_mask_location} - BW mask', binary_mask(well_image_read))  

    bw_mask_read = cv2.imread(bw_mask_location)

    cv2.imshow(f'{color_mask_location} - color mask', color_mask(bw_mask_read, well_image_read))  

    color_mask_read = cv2.imread(color_mask_location)

    #avg_rgb_dilution(color_mask_read)
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 