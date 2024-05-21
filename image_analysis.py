import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale
from opencv_basics_BGR import histogram_BGR

image1_location='original_opossum.png'
img = cv2.imread(image1_location)
img75 = cv2.imwrite('opossum_75.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 75])
img50 = cv2.imwrite('opossum_50.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
img25 = cv2.imwrite('opossum_25.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 25])

imggs = cv2.imread(image1_location, cv2.IMREAD_GRAYSCALE) #Value/Luminosity 
img75gs = cv2.imread("opossum_75.jpg", cv2.IMREAD_GRAYSCALE)
img50gs = cv2.imread("opossum_50.jpg", cv2.IMREAD_GRAYSCALE)
img25gs = cv2.imread("opossum_25.jpg", cv2.IMREAD_GRAYSCALE)

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
    plt.title("Color-Frequency Analysis for 25%", loc='center')
    plt.show()  # display

def unique_values_bar():
    plt.figure().set_figwidth(15)

    #OG
    blue_hist, green_hist, red_hist = histogram_BGR(img)
    unique_blue = set(blue_hist)
    unique_green = set(green_hist)
    unique_red = set(red_hist)

    luminosity_hist = histogram_grayscale(imggs)
    unique_luminosity = set(luminosity_hist)

    https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html

    plt.title("Unique Channel Values of All Images", loc='center')
    plt.show()




if __name__ == '__main__':
    
    cv2.imshow(f'{image1_location} - original', img) 

    luminosity_histogram()
    color_histogram()
    unique_values_bar()
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 