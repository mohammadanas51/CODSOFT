import cv2 as cv
import face_recognition as fr
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Hide the Tkinter main window
Tk().withdraw

# Ask the user to select an image file
load_image = askopenfilename()

# Load the target image and encode the face(s) in it
target_image = fr.load_image_file(load_image)
target_encoding = fr.face_encodings(target_image)

# Function to encode faces in a folder
def encode_faces(folder):
    list_people_encoding = []

    # Loop through each file in the specified folder
    for filename in os.listdir(folder):
        known_image = fr.load_image_file(f'{folder}{filename}')
        known_encoding = fr.face_encodings(known_image)[0]

        # Append the encoding and filename to the list
        list_people_encoding.append((known_encoding, filename))

    return list_people_encoding

# Function to find and label the target face(s) in the image
def find_target_face():
    face_location = fr.face_locations(target_image)

    # Loop through each encoded face in the "Images/" folder
    for person in encode_faces("Images/"):
        encoded_face = person[0]
        filename = person[1]

        # Compare the target face with the encoded face(s) in the folder
        is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance=0.55)
        print(f'{is_target_face}{filename}')

        # If a face is found in the target image, create a frame and label
        if face_location:
            face_number = 0
            for location in face_location:
                if is_target_face[face_number]:
                    label = filename
                    create_frame(location, label)
                face_number += 1

# Function to create a frame around the detected face and display the label
def create_frame(location, label):
    top, right, bottom, left = location

    cv.rectangle(target_image, (left, top), (right, bottom), (255, 0, 0), 2)
    cv.rectangle(target_image, (left, bottom + 20), (right, bottom), (255, 0, 0), cv.FILLED)
    cv.putText(target_image, label, (left + 100, bottom + 9), cv.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 1)

# Function to render the final image with detected faces and labels
def render_image():
    rgb_img = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)
    cv.imshow('Face Recognition', rgb_img)
    cv.waitKey(0)

# Find and label target face(s), then render the final image
find_target_face()
render_image()
