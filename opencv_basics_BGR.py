'''
OpenCV Basics - BGR Exercises
'''
import cv2
import math

def pixel_count(BGR_image: list)-> int:
    """ Calculates the total number of pixels in a BGR image.

    Args:
        BGR_image (list): A BGR image represented by 3 channels of 8-bit integers

    Returns:
        int: The number of pixels in a BGR image.
    """
    # WRITE YOUR CODE HERE.
    return(len(BGR_image) * len(BGR_image[0]))
    # END OF FUNCTION.

def tint_red(BGR_image:list)->list:
    """ This function tints a color image red. Given an input image that is BRG color,
    set the value of all pixels in the red channel to full on (255). 

    Args:
        BGR_image (list): A color image represented in a numpy array with 3 channels.

    Returns:
        image (list): The tinted image.

    """
    # WRITE YOUR CODE HERE.
    tinted = BGR_image.copy()

    for r, row in enumerate(BGR_image):
        for c, value in enumerate(row):
            tinted[r][c][2] = 255

    return(tinted)
    # END OF FUNCTION.

def to_BW(BGR_image: list)-> list:
    """ Converts a BGR image to a black and white image.
        If the pixel value (defined by (B+G+R)/3) in the original image is strictly greater than 128, 
        set the pixel to 255. Otherwise, set the pixel to 0. 

        Notes: 
            - You may NOT use any thresholding functions provided by OpenCV to do this.
            - Be careful not to modify the original image! 

    Args:
        BGR_image (list): A BGR image represented by 3 channels of 8-bit integers

    Returns:
        image (list): The black and white image.
    """
    # WRITE YOUR CODE HERE.
    new_image = BGR_image.copy()

    for r, row in enumerate(BGR_image):
        for c, pixel in enumerate(row):
            avgpixel = math.trunc((int(pixel[0])+int(pixel[1])+int(pixel[2]))/3)
            if avgpixel > 128:
                new_image[r][c][0] = 255
                new_image[r][c][1] = 255
                new_image[r][c][2] = 255
            else:
                new_image[r][c][0] = 0
                new_image[r][c][1] = 0
                new_image[r][c][2] = 0

    return(new_image)
    # END OF FUNCTION.

def to_grayscale(BGR_image: list)-> list:
    """ Converts a BGR image to a grayscale image by taking a uniform average of all 3 
        color channels: B (1/3), G (1/3) , R(1/3)
    
        Notes: 
            - Be careful not to modify the original image! 

    Args:
        BGR_image (list): A BGR image represented by 3 channels of 8-bit integers

    Returns:
        image (list): The grayscale image of 8-bit integers.
    """
    # WRITE YOUR CODE HERE.
    new_image = BGR_image.copy()

    for r, row in enumerate(BGR_image):
        for c, pixel in enumerate(row):
            avgpixel = math.trunc((int(pixel[0])+int(pixel[1])+int(pixel[2]))/3)
            new_image[r][c][0] = avgpixel
            new_image[r][c][1] = avgpixel
            new_image[r][c][2] = avgpixel

    return(new_image)

    # END OF FUNCTION.

def image_average_BGR(BGR_image1:list, BGR_image2:list)-> list:
    """ Averages the pixels of the two BGR input images by adding up the two input
        images on a per pixel, per channel basis and dividing each by two (truncated).

        Notes: 
            - You may assume image1 and image2 are the SAME size.
            - Be careful not to modify the original image! 
            - Be careful to avoid integer overflow!

    Args:
        BGR_image1 (list): A BGR image represented in an array represented by 3 channels of 8-bit integers
        BGR_image2 (list): A BGR image represented in an array represented by 3 channels of 8-bit integers

    Returns:
        image3 (list): An BGR image which is the average of image1 and image2.

    """
    # WRITE YOUR CODE HERE.
    image3 = BGR_image1.copy()

    for r, row in enumerate(BGR_image1):
        for c, pixel in enumerate(row):
            image3[r][c][0] = (int(pixel[0])+int(BGR_image2[r][c][0]))/2
            image3[r][c][1] = (int(pixel[1])+int(BGR_image2[r][c][1]))/2
            image3[r][c][2] = (int(pixel[2])+int(BGR_image2[r][c][2]))/2
    return(image3)
    
    # END OF FUNCTION.

def flip_horizontal_BGR(BGR_image:list)->list:
    """ Flips the input image across the horizontal axis. This can be interpreted as 
    switching the first and last column of the image, the second and second to last column, and so on.
    
    Note: Be careful not to modify the original image! 

    Args:
        BGR_image (list): A BGR image represented in an array represented by 3 channels of 8-bit integers

    Returns:
        image (list): The horizontally flipped image.

    """
    # WRITE YOUR CODE HERE.
    image2 = BGR_image.copy()
    
    for r, row in enumerate(BGR_image):
        for c, pixel in enumerate(row):
            oppval = (len(BGR_image[0])-c)-1
            image2[r][c] = BGR_image[r][oppval]

    
    return(image2)
    # END OF FUNCTION.

def histogram_BGR(BGR_image:list)->list:
    """ Counts the number of pixels of each value (0 -> 255) in the BGR image

    Args:
        BGR_image (list): A BGR image represented in an array represented by 3 channels of 8-bit integers

    Returns:
        blue_list: A list with 256 elements, where the value of the ith element represents the ith Blue count
        green_list: A list with 256 elements, where the value of the ith element represents the ith Green count
        red_list: A list with 256 elements, where the value of the ith element represents the ith Red count
    """
    # WRITE YOUR CODE HERE.
    blue_list = []
    green_list = []
    red_list = []

    bluetempdict = {}
    greentempdict = {}
    redtempdict = {}
    for i in range(0,256):
        blue_list.append(i)
        green_list.append(i)
        red_list.append(i)

        bluetempdict[i] = 0
        greentempdict[i] = 0
        redtempdict[i] = 0

    for r, row in enumerate(BGR_image):
        for c, pixel in enumerate(row):
            bluetempdict[int(pixel[0])] += 1
            greentempdict[int(pixel[1])] += 1
            redtempdict[int(pixel[2])] += 1

    for i in range(0,256):
        blue_list[i] = bluetempdict[i]
        green_list[i] = greentempdict[i]
        red_list[i] = redtempdict[i]

    return(blue_list,green_list,red_list)

    # END OF FUNCTION.

if __name__ == '__main__':
    image1_location='dog.jpg' #400 × 217 pixels
    image2_location='dog2.jpg' #400 × 217 pixels
    img = cv2.imread(image1_location, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image1_location} - original', img) 
    img2 = cv2.imread(image2_location, cv2.IMREAD_COLOR) 
   
    print(f'Pixel Count: {pixel_count(img)}')

    #cv2.imwrite("Tinted.jpg", tint_red(img)) 
    cv2.imshow(f'{image1_location} - tint_red', tint_red(img)) 
    #cv2.imwrite("BW.jpg", to_BW(img)) 
    cv2.imshow(f'{image1_location} - to_BW', to_BW(img)) 
    #cv2.imwrite("GS.jpg", to_grayscale(img)) 
    cv2.imshow(f'{image1_location} - to_grayscale', to_grayscale(img)) 
    #cv2.imwrite("Averaged.jpg", image_average_BGR(img, img2)) 
    cv2.imshow(f'{image1_location} v. {image2_location} - average_BGR', image_average_BGR(img, img2)) 
    #cv2.imwrite("Flipped.jpg", flip_horizontal_BGR(img))
    cv2.imshow(f'{image1_location} - flip_horizontal_BGR', flip_horizontal_BGR(img))


    blue_hist, green_hist, red_hist = histogram_BGR(img)
    print(f'Blue Histogram: {blue_hist}')
    print(f'Green Histogram: {blue_hist}')
    print(f'Red Histogram: {blue_hist}')
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 

