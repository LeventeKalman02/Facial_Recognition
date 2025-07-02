import cv2
import numpy as np
import face_recognition
import os

# Tasks:
# Set the path to the directory containing the images
# Create a list to hold the images and their names
# Generate the encodings for each image in the directory
# Try to recognize face in the webcam feed

path = 'ImagesAttendance'  
images = []

