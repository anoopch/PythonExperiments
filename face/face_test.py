# OpenCV program to detect face in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2

frontal_cascade_path = "../haarcascade_frontalface_default.xml"

# Detector object created
fd = FaceDetector(frontal_cascade_path)
