import cv2
import imutils
import numpy as np
vs = cv2.VideoCapture('./data/video.mp4')
while True:
    # read frame1, resize and convert to grayscale
    ret, frame1 = vs.read()
    if frame1 is None:
        break
    frame1 = imutils.resize(frame1, width=600)
    print(frame1.shape)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # read frame2, resize and convert to grayscale
    ret2, frame2 = vs.read()
    if frame2 is None:
        break
    frame2 = imutils.resize(frame2, width=600)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # compute the difference between frames
    img = cv2.absdiff(gray1, gray2)
    # blur image
    #blurred = cv2.GaussianBlur(dist, (9, 9), 0)

    b = np.zeros(img.shape[:2], dtype = "uint8")
    r = np.zeros(img.shape[:2], dtype = "uint8")
    fgmask_diff_rgb = cv2.merge([b, img*3, r])
    # global thresholding
    ret3, th1 = cv2.threshold(img,100, 255, cv2.THRESH_BINARY)
    print(th1.dtype)
    cnts = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # other way to find contours = same error
    # hierarchy, contours = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    combined = np.hstack((frame1,fgmask_diff_rgb))
    cv2.imshow("Combined",combined)
    # show the frame to our screen
    key = cv2.waitKey(100) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# otherwise, release the camera
vs.release()
# close all windows
cv2.destroyAllWindows()
