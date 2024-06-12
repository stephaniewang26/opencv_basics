import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale
from opencv_basics_BGR import histogram_BGR
import numpy as np
import os

def filter_photo(frame, framecount):
    frame = cv2.imread(frame)
    framecopy = frame.copy()

    ogx = 0
    ogy = 0
    height = 360
    width = 640
    size = 20

    for i in range(int(height/size)):
        ogx=0
        for k in range(int(width/size)):
            blue_list = []
            green_list = []
            red_list = []
            #to get the avg just get all pixels first and then go through each channel and take avg then apply that color to the entire square

            startx = ogx
            endx = ogx+size
            starty = ogy
            endy = ogy+size
            for r, row in enumerate(framecopy):
                for c, value in enumerate(row):
                    if c>=startx and c <=endx and r>=starty and r<=endy:
                        blue_list.append(int(framecopy[r][c][0]))
                        green_list.append(int(framecopy[r][c][1]))
                        red_list.append(int(framecopy[r][c][2]))
                    #DRAW GRID
                    # if c==endx or r==endy:
                    #     framecopy[r][c][0] = 255
                    #     framecopy[r][c][1] = 255
                    #     framecopy[r][c][2] = 255
            bluetotal = 0
            greentotal = 0
            redtotal = 0
            for i in range(len(blue_list)):
                bluetotal += blue_list[i]
                greentotal += green_list[i]
                redtotal += red_list[i]

            blueavg = bluetotal/len(blue_list)
            greenavg = greentotal/len(green_list)
            redavg = redtotal/len(red_list)

            cv2.rectangle(framecopy, (ogx,ogy), (ogx+20,ogy+20), (blueavg,greenavg,redavg), -1)

            # for r, row in enumerate(framecopy):
            #     for c, value in enumerate(row):
            #         if c>=startx and c <=endx and r>=starty and r<=endy:
            #             framecopy[r][c][0] = blueavg
            #             framecopy[r][c][1] = greenavg
            #             framecopy[r][c][2] = redavg

            ogx+=20
        ogy+=20

    folderpath = "/Users/stephanie.wang26/Desktop/ADV_CS/opencv_basics/filtered_images"
    framename = "frame%d.jpg" % framecount
    joined = os.path.join(folderpath, framename)
    cv2.imwrite(joined, framecopy)


def FrameCapture(path): 

    folderpath = "/Users/stephanie.wang26/Desktop/ADV_CS/opencv_basics/images"
  
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        framename = "frame%d.jpg" % count
        joined = os.path.join(folderpath, framename)
        cv2.imwrite(joined, image) 
  
        count += 1

def save_video():
    video = cv2.VideoWriter('filtered_video.mp4', cv2.VideoWriter_fourcc(*"mp4v"), 24, (640, 360))

    for j in range(182):
        folderpath = "/Users/stephanie.wang26/Desktop/ADV_CS/opencv_basics/filtered_images"
        framename = "frame%d.jpg" % j
        joined = os.path.join(folderpath, framename)
        
        img = cv2.imread(joined)
        video.write(img)

    cv2.destroyAllWindows()
    video.release()

if __name__ == '__main__':
    frame_location='opossum_vid_frame.png'
    frame_read = cv2.imread(frame_location)

    video_location = 'opossum_video.mp4'

    #cv2.imshow(f'{frame_location} - filter photo', filter_photo(frame_read,1))  
    #FrameCapture(video_location) 


    # folderpath = "/Users/stephanie.wang26/Desktop/ADV_CS/opencv_basics/images"
    # for i in range(48,182):
    #     framename = "frame%d.jpg" % i
    #     joined = os.path.join(folderpath, framename)
    #     filter_photo(joined, i)

    save_video()

    cv2.waitKey() 
    cv2.destroyAllWindows() 