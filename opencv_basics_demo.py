'''
OpenCV Basics
'''
import cv2  

image_location='dog.png' #1790 × 1016 pixels

#Read image in a variety of color contexts
img1 = cv2.imread(image_location, cv2.IMREAD_COLOR) #BGR 
img2 = cv2.imread(image_location, cv2.IMREAD_GRAYSCALE) #Value/Luminosity  
img3 = cv2.imread(image_location, cv2.IMREAD_UNCHANGED) #BGRA

#Images are collections of BGR values
print(f'BGR Image Values:{img1}')
print(f'BGR Image Height:{len(img1)}')
print(f'BGR Image Width:{len(img1[0])}')
print(f'BGR Image Pixel:{img1[0][0]}')

print(f'GS Image Values:{img2}')
print(f'GS Image Height:{len(img2)}')
print(f'GS Image Width:{len(img2[0])}')
print(f'GS Image Pixel:{img2[0][0]}')

new_image = img2.copy()

for r, row in enumerate(img2):
    for c, value in enumerate(row):
       if value > 128:
          new_image[r][c] = 255
       else:
          new_image[r][c] = 0

# Saving Images
cv2.imwrite("dog_BW.jpg", new_image)




#Basic OpenCV Drawing functions
center_coordinates = (500, 500)
radius= 20
color= (0, 255, 255)
thickness = 2
cv2.circle(img1, center_coordinates, radius, color, thickness)

start_point = (100, 100)
end_point = (1000, 1000)
cv2.rectangle(img2, start_point, end_point, color, thickness)
cv2.line(img3, start_point, end_point, color, thickness)

text = 'Dog'
bottom_left = (10,500)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 10
font_color = (255, 255, 0)
cv2.putText(img3,'Dog',bottom_left, font, font_scale, font_color, thickness)  

#Displaying Images
cv2.imshow(f'color image w/out alpha channel: {image_location}', img1)  
cv2.imshow(f'b&w image: {image_location}', img2)  
cv2.imshow(f'color image w/ alpha channel: {image_location}', img3)  
cv2.imshow(f'only b&w image: {image_location}', new_image)  
 
# Saving Images
cv2.imwrite("dog_with_ball.jpg", img1) 

#Closing Up Shop
cv2.waitKey() 
cv2.destroyAllWindows() 