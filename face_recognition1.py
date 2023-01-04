# Import necessary libraries
import cv2

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the image and convert it to grayscale
image = cv2.imread('test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Run the face detection model on the image
faces = face_cascade.detectMultiScale(gray, 1.2, 5)

# Draw a rectangle around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image
cv2.imshow('Face Detection', image)
cv2.waitKey()
