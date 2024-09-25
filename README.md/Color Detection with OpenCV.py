import cv2
cap = cv2.VideoCapture(1)
_, frame = cap.read()
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    height, width,_ =frame.shape
    center_x = int(width / 2)
    center_y = int(height / 2)
    pixel_center_color = hsv_frame[center_y, center_x]
    color_h = pixel_center_color[0]
    color_s = pixel_center_color[1]
    color_v = pixel_center_color[2]
    color = "Undefined"
    if color_h < 5:
        color = "Red"
    elif color_s < 40:
        color = "White"
    elif color_v< 20:
        color = "Black"
    elif color_h < 22:
        color = "Orange"
    elif color_h< 43:
        color = "Yellow"
    elif color_h < 75:
        color = "Green"
    elif color_h< 129:
        color = "Blue"
    elif color_s < 170:
        color = "Violet"
    else:
        color = "No Recognition"
    
    pixel_center_bgr = frame[center_y, center_x]

    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(frame, color, (40, 110), 0, 4,(b, g, r), 9)

    print(pixel_center_color)
    cv2.circle(frame, (center_x, center_y), 10, (255, 0, 0), 6)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



#README.md
###################################
# Color Detection with OpenCV

#This Python script captures video from a camera and detects the color of the pixel at the center of the frame.

## Overview

# 1. **Capture Video**: 
#    - Initializes video capture from camera index 1.

# 2. **Color Conversion**: 
#    - Converts each frame from BGR to HSV color space for easier color detection.

# 3. **Center Pixel Analysis**: 
#    - Identifies the HSV values of the center pixel to determine its color.

# 4. **Color Classification**: 
#    - Classifies the color based on hue, saturation, and brightness thresholds.

# 5. **Display Color**: 
#    - Draws the recognized color label and a circle at the center of the frame.

# 6. **Exit Condition**: 
#    - Closes the application when the 'Esc' key is pressed.

## Requirements

#- Ensure you have OpenCV installed to run this script effectively.
###########################

# Mohammed Jalal Naji Hasan Omar 202073005
# Osamah Abdullah Motea’a 202073041
# Abdulrahman Afef Al-Aghbari 202079113