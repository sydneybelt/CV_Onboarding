# Testing video 1: https://drive.google.com/file/d/1JXjhM3kF8Ppxf_5KFo8B5cUNkvRUj2jx/view?usp=drive_web
# Testing video 2: https://drive.google.com/file/d/1s9znh-0sU5iL3tWyVh2-reaZezfDXsJ2/view?usp=drive_web

#importing some useful packages
import sys
import numpy as np
import cv2

# You will be able to use this file for lane detection algorithms on a video of lanes.
# Please finish the TODOs to make it work
# Try different values and combinations to optimize your lane detection results
 
# TODO:
# threshold using color from original image, and combine that with the houged image
def threshold(img, edges):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # TODO:
    # define range of white color in HSV
    # change thresholding values according to your need !
    # HINT: research about how HSV works before filling in the values
    lower_white = np.array(["your_values_here"], dtype=np.uint8)
    upper_white = np.array(["your)values_here"], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(edges, edges, mask= mask)

    return res

#this funtion is done for you
def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# TODO:
# GaussianBlur is an important CV technique.
# Please do your research online to learn more about GaussianBlur and how to call cv2.GaussianBlur
def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur("missing_arguments")

# TODO:
# define your own region of interest
# feel free to change the shape and dimensions during testing for it to work best 
def region_of_interest(img, vertices):
    """
    Applies an image mask.

    """
    # add code here

    return img

# TODO:
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    # TODO: complete this function call
    lines = cv2.HoughLinesP("missing_arguments")
    
    # import pdb; pdb.set_trace() //done
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    # rospy.loginfo(type(lines)) //done
    # rospy.loginfo(lines) //done
    if isinstance(lines, np.ndarray):
        # rospy.loginfo(lines) //done
        draw_lines(line_img, lines)
    return line_img

# This function is done BUT
# Feel free to change the values of color and THRESHOLD during testing to see how things work
def draw_lines(img, lines, color=[255, 255, 255], thickness=2):
    """
    This function draws `lines` with `color` and `thickness`.
    """
    lines = np.squeeze(lines)
    distances = np.linalg.norm(lines[:, 0:2] - lines[:, 2:], axis=1, keepdims=True)
    MAX_COLOR = 99
    MIN_COLOR = 0
    m = (MAX_COLOR - MIN_COLOR)/(np.max(distances) - np.min(distances)) # Resize distances between MIN and MAX COLOR
    color_range = m * distances
    THRESHOLD = 50 # Get rid of lines smaller than threshold

    # cv2.line is slow because of the for loop, but can be used to show various colors.
    # This can help if we want a continous probability of lines based on distance
    color_range[color_range < THRESHOLD] = 0
    for ((x1,y1,x2,y2), col) in zip(lines, color_range):
        cv2.line(img, (x1, y1), (x2, y2), [255, 255, 255], thickness)

    # cv2.polylines is faster but can draw only one color. Thus, the only type of filtering is binary with the threshold
    # filtered_lines = lines[(color_range > THRESHOLD).ravel(), :]
    # cv2.polylines(img, filtered_lines.reshape((-1, 2, 2)), False, 255, thickness) # Faster but can't draw multiple colors. Thus, no thresholding

# TODO:
# IMPORTANT: this part is the heart of our lane detection algorithm, where the previous functions 
# are COMBINED IN DIFFERENT WAYS to process an image.
# Make sure you know how each functions work, and design your own way of lane detection.
# You can choose not to use all of the functions
# IMPORTANT: Other functions to consider: Canny, MorphologyEx
# NOT REQUIRED: Feel free to research if you want to use more functions https://docs.opencv.org/4.x/d7/dbd/group__imgproc.html
def detect_lanes(image):
   
   # Process the image with your own combinations of the previous fuunctions!
   # HINT: You can use some of the functions more than once if necessary. 
   # HINT: The order functions are used might not be the same as how they are listed above.

    
    # Show the result //done
    cv2.imshow("window", image)
    cv2.waitKey(1)

#this function is done for you
def main():
    count = 0
    # opening the video
    cap = cv2.VideoCapture(VIDEO_PATH)

    # error opening the video
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
        exit(1)
    # initialize frame size variables
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    # while the video is still running
    while(cap.isOpened()):
        # read each frame
        ret, frame = cap.read()
        if ret == True:
            # detect the lanes on the frame
            if count >= 0:
             detect_lanes(frame)
            
        else: 
            break
    cap.release()
    cv2.destroyAllWindows()
    # out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    # for frame in frames:
    #     detect_lanes(frame, out)
    # out.release()

# this is done for you
if __name__ == '__main__':
    argv = sys.argv
    global VIDEO_PATH
    if (len(argv) != 2):
        print("Usage: ADSDetection.py (video_path)")
        exit(1)
    else:
        VIDEO_PATH = argv[1]
    main()
