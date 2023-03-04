import cv2
import numpy as np

img = cv2.imread('./data/image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img)

car_cascade = cv2.CascadeClassifier('./data/cars.xml')
cars = car_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x + int(w/5), y), (x + int(w/1.1), y + int(h/1.5)), (0, 0, 255), 2)

cv2.imwrite('hw0_111511198_1.png', img)



