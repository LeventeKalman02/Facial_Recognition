# Facial_Recognition
This project utilizes OpenCV, Cmake, dlib, and face_recognition libraries.

## Basics
The [Basics.py](Basics.py) file is a broken down, step by step explanation for understanding the concept of how the imports and libraries work to be able to recognise the faces in the images along with how to use them

- First the files are loaded, using the cv2(OpenCV) library the image files are converted to RGB.
- Utilizing the Face_Recognition library, the faces locations are detected.
- Once the faces are detected, they are encoded. This returns a ``128-dimension`` face encoding for each face detected in an image.
- A rectangle is placed over each face detected in the images for easy visibility and to ensure that the faces are correctly recognised.
- The faces in 2 images are compare by finding the distance between the dimesions of the encodings.
  - Printing the comparison will print True if the faces are similar and false otherwise. 
  - Printing the distance gives a number between ``0 and 1``, where ``0 is identical and 1 is completely different``.
- Once again the results are printed onto the output image for easy visibility.

This is the basic concept of this project and its inner workings. 
