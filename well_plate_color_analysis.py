import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale
from opencv_basics_BGR import histogram_BGR
from opencv_basics_BGR import to_grayscale
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
    colorcopy = colormask.copy()
    dilutionticks = []
    colorrows = ["yellow","red","blue","green"]
    colordict = {
        "yellow":[],
        "red":[],
        "blue":[],
        "green":[]
    }

    count = 1
    for i in range(12):
        dilutionticks.append(str(count))
        count *= 2

    ogx = 75
    ogy = 73
    rad = 40

    for i in range(4):
        ogx=75
        for k in range(12):
            avgcircle = 0
            totalpixelsincircle = 0
            sumincircle = 0

            startx = ogx-rad
            endx = ogx+rad
            starty = ogy-rad
            endy = ogy+rad
            for r, row in enumerate(colormask):
                for c, value in enumerate(row):
                    if c>=startx and c <=endx and r>=starty and r<=endy:
                        # colorcopy[r][c][0] = 255
                        # colorcopy[r][c][1] = 255
                        # colorcopy[r][c][2] = 255
                        if tuple(colormask[r][c]) != (0,0,0):
                            totalpixelsincircle += 1
                            avgpixel = 0
                            avgpixel += colormask[r][c][0] 
                            avgpixel += colormask[r][c][1] 
                            avgpixel += colormask[r][c][2] 
                            avgpixel /= 3
                            sumincircle += avgpixel
                            
            if totalpixelsincircle != 0:
                avgcircle = sumincircle/totalpixelsincircle
            colordict[colorrows[i]].append(avgcircle)        
            ogx+=129
        ogy+=129

    print(colordict)
    print(dilutionticks)

    x = dilutionticks
    y = colordict["yellow"]

    plt.figure()
    plt.plot(x, y, label = "yellow row", color='goldenrod') 

    y = colordict["red"]
    plt.plot(x, y, label = "red row", color='red') 

    y = colordict["blue"]
    plt.plot(x, y, label = "blue row", color='blue') 

    y = colordict["green"]
    plt.plot(x, y, label = "green row", color='green') 
    
    plt.legend()
    plt.xlabel("Dilution factor")
    plt.xticks(dilutionticks)
    plt.ylabel("Avg RGB Value")
    plt.title("Correlation between Color and Dilution", loc='center')
    plt.show()  # display

    # cv2.imwrite("plate_color_grid_copy.png", colorcopy)
    # return(colorcopy)

def color_channel_histograms(colormask):
    fig, axs = plt.subplots(4, 12)
    grayscalemask = colormask.copy()
    grayscalemask = cv2.cvtColor(grayscalemask, cv2.COLOR_BGR2GRAY) 

    welldict={
    }

    for i in range(48):
        welldict[i] = dict()
        welldict[i]["blue_hist"] = []
        welldict[i]["green_hist"] = []
        welldict[i]["red_hist"] = []
        welldict[i]["lum_hist"] = []

    ogx = 75
    ogy = 73
    rad = 40
    circlenum = -1

    for i in range(4):
        ogx=75
        for k in range(12):
            circlenum+=1

            bluetempdict = {}
            greentempdict = {}
            redtempdict = {}
            lumtempdict = {}

            for i in range(0,256):
                welldict[circlenum]["blue_hist"].append(i)
                welldict[circlenum]["green_hist"].append(i)
                welldict[circlenum]["red_hist"].append(i)
                welldict[circlenum]["lum_hist"].append(i)

                bluetempdict[i] = 0
                greentempdict[i] = 0
                redtempdict[i] = 0
                lumtempdict[i] = 0

            startx = ogx-rad
            endx = ogx+rad
            starty = ogy-rad
            endy = ogy+rad

            for r, row in enumerate(colormask):
                for c, value in enumerate(row):
                    if c>=startx and c <=endx and r>=starty and r<=endy:
                        if tuple(colormask[r][c]) != (0,0,0):
                            bluetempdict[int(value[0])] += 1
                            greentempdict[int(value[1])] += 1
                            redtempdict[int(value[2])] += 1
                            lumtempdict[int(grayscalemask[r][c])] += 1

                    
            for i in range(0,256):
                welldict[circlenum]["blue_hist"][i] = bluetempdict[i]
                welldict[circlenum]["green_hist"][i] = greentempdict[i]
                welldict[circlenum]["red_hist"][i] = redtempdict[i]
                welldict[circlenum]["lum_hist"][i] = lumtempdict[i]
            ogx+=129
        ogy+=129
    
    x = range(256)
    row = -1
    col = -1
    circlenum = -1

    for i in range(4):
        row += 1
        col = -1
        for i in range(12):
            col += 1
            circlenum += 1
            y = welldict[circlenum]["blue_hist"]
            axs[row, col].plot(x, y, "blue")
            y = welldict[circlenum]["green_hist"]
            axs[row, col].plot(x, y, "green")
            y = welldict[circlenum]["red_hist"]
            axs[row, col].plot(x, y, "red")
            y = welldict[circlenum]["lum_hist"]
            axs[row, col].plot(x, y, "gray")

    fig.supxlabel('Color value')
    fig.supylabel("Frequency of value")
    fig.suptitle("Well Color Channel Histograms")
    plt.show() 



if __name__ == '__main__':
    well_image_location = 'colorplate.png'
    well_image_read = cv2.imread(well_image_location)

    bw_mask_location = "plate_mask.png"
    color_mask_location = "plate_color_grid.png"

    #cv2.imshow(f'{well_image_location} - original', well_image_read)
    #cv2.imshow(f'{bw_mask_location} - BW mask', binary_mask(well_image_read))  

    bw_mask_read = cv2.imread(bw_mask_location)

    #cv2.imshow(f'{color_mask_location} - color mask', color_mask(bw_mask_read, well_image_read))  

    color_mask_read = cv2.imread(color_mask_location)

    color_mask_copy_location = "plate_color_grid_copy.png"

    #cv2.imshow(f'{color_mask_location} - color copy',avg_rgb_dilution(color_mask_read))

    color_channel_histograms(color_mask_read)
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 