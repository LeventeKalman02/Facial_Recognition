import cv2
import numpy as np
import face_recognition # This library is used for face recognition tasks and simplifies the process of detecting and recognizing faces in images as it handles the backend complexities

# load main image file
# The main image file is a clear image of Markiplier
# This will be used to create the face encoding for recognition
imgMark = face_recognition.load_image_file("Images/Markiplier.jpg") # Load the image file
imgMark = cv2.cvtColor(imgMark, cv2.COLOR_BGR2RGB) # Convert the image from BGR to RGB

# load test image file
# The test image is at an angle and has different lighting conditions
# This will test the robustness of the face recognition model
imgTest = face_recognition.load_image_file("Images/Markiplier_test.jpg") # Load the image file
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB) # Convert the image from BGR to RGB

# Detect faces in the image so we can see where the face is located and that it is detected correctly
faceLoc = face_recognition.face_locations(imgMark)[0] # Get the location of the first face detected
print(faceLoc) # Prints 4 values: top, right, bottom, left
# Encode the face from the main image
encodeMark = face_recognition.face_encodings(imgMark)[0] # Get the face encoding for the first face detected
cv2.rectangle(imgMark, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2) # Draw a rectangle around the face in the main image

faceLocTest = face_recognition.face_locations(imgTest)[0] # Get the location of the first face detected in the test image
print(faceLocTest) # Prints 4 values: top, right, bottom, left
# Encode the face from the image
encodeTest = face_recognition.face_encodings(imgTest)[0] # Get the face encoding for the first face detected
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2) # Draw a rectangle around the face in the main image

# Compare the faces to see if they match by finding the distance between the face encodings. These are 128 size vectors that represent the face
results = face_recognition.compare_faces([encodeMark], encodeTest) # Compare the face encodings
faceDis = face_recognition.face_distance([encodeMark], encodeTest) # Calculate the distance between the face encodings to find out hour similar they are
print(results, faceDis) # Results: Prints True if the faces match, False otherwise. faceDis: Prints the distance between the faces, lower means more similar


# Display the images using OpenCV to ensure they are loaded correctly
cv2.imshow("Markiplier", imgMark) # Display the image in a window
cv2.imshow("Markiplier Test", imgTest)
cv2.waitKey(0) # Wait for a key press to close the window
