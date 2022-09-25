import numpy as np
import argparse
import cv2


stream = cv2.VideoCapture(0)
ball_video = "./output.avi"
cap = cv2.VideoCapture(ball_video)

# Check if video opened successfully
if (cap.isOpened()== False):
    print("Error opening video stream or file")
frame_count = 0
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame_count += 1
    print(ret)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect circles in the image
    circles = cv2.HoughCircles(gray, 
        cv2.HOUGH_GRADIENT, 
        dp=10,               #resolution of accumulator array.
        minDist=100,          #number of pixels center of circles should be from each other, hardcode
        param1=50,
        minRadius=(10),    #HoughCircles will look for circles at minimum this size
        maxRadius=(40)     #HoughCircles will look for circles at maximum this size
        )
    # ensure at least some circles were found
    print(circles)
    if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the rectangle corresponding to the location of the ball
            cv2.rectangle(frame, (x-r-5, y-r-5), (x+r+5, y+r+5), (0, 255, 0), 1)
            cv2.rectangle(frame, (x - 3, y - 3), (x + 3, y + 3), (0, 128, 255), -1)
            cv2.putText(frame, 'Ball', (x-r-3, y-r-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        

    cv2.putText(frame, 'Frame no:      '+ str(frame_count), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, 'Ball position: ('+ str(x) + ',' + str(y) + ')', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
    # show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break


