import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale
from opencv_basics_BGR import histogram_BGR
import numpy as np

image1_location='original_opossum.png'
img = cv2.imread(image1_location)
img75 = cv2.imwrite('opossum_75.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 75])
img50 = cv2.imwrite('opossum_50.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
img25 = cv2.imwrite('opossum_25.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 25])

img75read = cv2.imread('opossum_75.jpg')
img50read = cv2.imread('opossum_50.jpg')
img25read = cv2.imread('opossum_25.jpg')

img_list = [img,img75read,img50read,img25read]

imggs = cv2.imread(image1_location, cv2.IMREAD_GRAYSCALE) #Value/Luminosity 
img75gs = cv2.imread("opossum_75.jpg", cv2.IMREAD_GRAYSCALE)
img50gs = cv2.imread("opossum_50.jpg", cv2.IMREAD_GRAYSCALE)
img25gs = cv2.imread("opossum_25.jpg", cv2.IMREAD_GRAYSCALE)
imggs_list = [imggs,img75gs,img50gs,img25gs]

def luminosity_histogram():
    plt.figure()
    print(f'grayscale Histogram: {histogram_grayscale(imggs)}')
    
    # define data values
    x = range(256) 
    y = histogram_grayscale(imggs)
    plt.plot(x, y, label = "luminosity of original", color='black') 
    y2 = histogram_grayscale(img75gs)
    plt.plot(x, y2, label = "luminosity of 75%", color="#404040") 
    y3 = histogram_grayscale(img50gs)
    plt.plot(x, y3, label = "luminosity of 50%", color='#808080') 
    y4 = histogram_grayscale(img25gs)
    plt.plot(x, y4, label = "luminosity of 25%", color='#c0c0c0') 

    plt.legend()
    plt.xlabel("Luminosity value")
    plt.ylabel("Frequency of value")
    plt.title("Luminosity-Frequency Analysis", loc='center')
    plt.show()  # display

def color_histogram():
    #OG
    plt.figure()
    blue_hist, green_hist, red_hist = histogram_BGR(img)

    x = range(256) 
    y = histogram_grayscale(imggs)
    plt.plot(x, y, label = "luminosity of original", color='black') 
    y = blue_hist
    plt.plot(x, y, label = "blue values of original", color='blue') 
    y = green_hist
    plt.plot(x, y, label = "green values of original", color='green') 
    y = red_hist
    plt.plot(x, y, label = "red values of original", color='red') 

    plt.legend()
    plt.xlabel("Color value")
    plt.ylabel("Frequency of value")
    plt.title("Color-Frequency Analysis for Original", loc='center')
    plt.show()  # display


    #75%
    plt.figure()
    blue_hist, green_hist, red_hist = histogram_BGR(cv2.imread("opossum_75.jpg"))

    x = range(256) 
    y = histogram_grayscale(img75gs)
    plt.plot(x, y, label = "luminosity of 75%", color='black') 
    y = blue_hist
    plt.plot(x, y, label = "blue values of 75%", color='blue') 
    y = green_hist
    plt.plot(x, y, label = "green values of 75%", color='green') 
    y = red_hist
    plt.plot(x, y, label = "red values of 75%", color='red') 

    plt.legend()
    plt.xlabel("Color value")
    plt.ylabel("Frequency of value")
    plt.title("Color-Frequency Analysis for 75%", loc='center')
    plt.show()  # display


    #50%
    plt.figure()
    blue_hist, green_hist, red_hist = histogram_BGR(cv2.imread("opossum_50.jpg"))

    x = range(256) 
    y = histogram_grayscale(img50gs)
    plt.plot(x, y, label = "luminosity of 50%", color='black') 
    y = blue_hist
    plt.plot(x, y, label = "blue values of 50%", color='blue') 
    y = green_hist
    plt.plot(x, y, label = "green values of 50%", color='green') 
    y = red_hist
    plt.plot(x, y, label = "red values of 50%", color='red') 

    plt.legend()
    plt.xlabel("Color value")
    plt.ylabel("Frequency of value")
    plt.title("Color-Frequency Analysis for 50%", loc='center')
    plt.show()  # display


    #25%
    plt.figure()
    blue_hist, green_hist, red_hist = histogram_BGR(cv2.imread("opossum_25.jpg"))

    x = range(256) 
    y = histogram_grayscale(img25gs)
    plt.plot(x, y, label = "luminosity of 25%", color='black') 
    y = blue_hist
    plt.plot(x, y, label = "blue values of 25%", color='blue') 
    y = green_hist
    plt.plot(x, y, label = "green values of 25%", color='green') 
    y = red_hist
    plt.plot(x, y, label = "red values of 25%", color='red') 

    plt.legend()
    plt.xlabel("Color value")
    plt.ylabel("Frequency of value")
    plt.title("Color-Frequency Analysis for 25%", loc='center')
    plt.show()  # display

def unique_values_bar():
    
    images = ("Original","75%","50%","25%")
    unique_values_dict = {
        'luminosity':[],
        'blue':[],
        'green':[],
        'red':[]
    }
    

    for eachimage in imggs_list:
        unique_luminosity = 0
        luminosity_hist = histogram_grayscale(eachimage)
        for value in luminosity_hist:
            if value != 0:
                unique_luminosity +=1
        unique_values_dict["luminosity"].append(unique_luminosity)

    #print("lum values", unique_values_dict["luminosity"])
    unique_values_dict["luminosity"] = tuple(unique_values_dict["luminosity"])

    for eachimage in img_list:
        unique_blue = 0
        unique_green = 0
        unique_red = 0
        blue_hist, green_hist, red_hist = histogram_BGR(eachimage)
        for i in range(256):
            if blue_hist[i] != 0:
                unique_blue +=1
            if green_hist[i] != 0:
                unique_green +=1
            if red_hist[i] != 0:
                unique_red +=1
        unique_values_dict["blue"].append(unique_blue)
        print('blue hist', blue_hist)
        unique_values_dict["green"].append(unique_green)
        unique_values_dict["red"].append(unique_red)
    

    print(unique_values_dict)

    x = np.arange(len(images))  # label locations
    width = 0.2  # the width of the bars

    lumbar = plt.bar(x, unique_values_dict["luminosity"], width, color = 'grey')
    bluebar = plt.bar(x+width, unique_values_dict["blue"], width, color='blue') 
    greenbar = plt.bar(x+width*2, unique_values_dict["green"], width, color='green') 
    redbar = plt.bar(x+width*3, unique_values_dict["red"], width, color='red') 

    plt.title("Unique Channel Values of All Images") 
    plt.xticks(x+width*1.5,['Original', '75%', '50%', '25%']) 
    plt.xlabel("Images")
    plt.ylabel("Unique channel values")
    plt.legend((lumbar, bluebar, greenbar, redbar), ('Luminosity', 'Blue', 'Green', 'Red') ) 
    plt.show()

def unique_colors_bar():
    image_names = ['img','img75','img50','img25']

    unique_colors_dict = {
        'img':set(),
        'img75':set(),
        'img50':set(),
        'img25':set()
    }

    count = -1
    for eachimage in img_list:
        count +=1 
        for r, row in enumerate(eachimage):
            for c, pixel in enumerate(row):
                color_tup = (int(pixel[0]), int(pixel[1]), int(pixel[2]))
                unique_colors_dict[image_names[count]].add(color_tup)

        unique_colors_dict[image_names[count]] = len(unique_colors_dict[image_names[count]])


    realnames = ['Original', "75%", "50%", "25%"]
    values = list(unique_colors_dict.values())
    plt.bar(realnames, values, color ='orange', width = 0.4)
 
    plt.title("Number of Unique Colors in All Images")
    plt.ylabel("Number of unique colors")
    plt.xlabel("Images")
    plt.show()


if __name__ == '__main__':
    
    cv2.imshow(f'{image1_location} - original', img) 

    #luminosity_histogram()
    #color_histogram()
    unique_values_bar()
    #unique_colors_bar()
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 