import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale

if __name__ == '__main__':
    image1_location='original_opossum.png'
    img = cv2.imread(image1_location)
    img90 = cv2.imwrite('opossum_90.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
    img75 = cv2.imwrite('opossum_75.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 75])
    img50 = cv2.imwrite('opossum_50.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

    imggs = cv2.imread(image1_location, cv2.IMREAD_GRAYSCALE) #Value/Luminosity 
    img90gs = cv2.imread("opossum_90.jpg", cv2.IMREAD_GRAYSCALE)
    img75gs = cv2.imread("opossum_75.jpg", cv2.IMREAD_GRAYSCALE)
    img50gs = cv2.imread("opossum_50.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow(f'{image1_location} - original', img) 

    print(f'grayscale Histogram: {histogram_grayscale(imggs)}')
    
    # define data values
    x = range(256) 
    y = histogram_grayscale(imggs)
    plt.plot(x, y, label = "luminosity of original", color='black') 
    y2 = histogram_grayscale(img90gs)
    plt.plot(x, y2, label = "luminosity of 90%", color="#404040") 
    y3 = histogram_grayscale(img75gs)
    plt.plot(x, y3, label = "luminosity of 75%", color='#808080') 
    y4 = histogram_grayscale(img50gs)
    plt.plot(x, y4, label = "luminosity of 50%", color='#c0c0c0') 

    plt.legend()
    plt.title("Luminosity-Frequency Analysis", loc='center')
    plt.show()  # display
    cv2.waitKey() 
    cv2.destroyAllWindows() 