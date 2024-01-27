# Face Recognition App

## Overview

This Python script performs face recognition on a target image using the `face_recognition` library. It allows the user to select a target image and compares the faces in that image with the faces encoded in a specified folder (`Images/` in this case). If a match is found, it draws a frame around the detected face and displays the corresponding label.

## Dependencies

- [OpenCV (cv2)](https://pypi.org/project/opencv-python/): Used for image processing and drawing frames.
- [face_recognition](https://pypi.org/project/face-recognition/): A face recognition library.

## Usage

1. Ensure you have the required dependencies installed:

   ```bash
   pip install opencv-python face-recognition
   ```

2. Run the script:

   ```bash
   python face_recognition_app.py
   ```

3. The script will prompt you to select a target image. Once selected, it will compare the faces in the target image with the encoded faces in the `Images/` folder. Detected faces will be framed, and the corresponding labels will be displayed.

4. Press any key to close the final image window.

## Script Structure

- `face_recognition_app.py`: The main Python script.
- `Images/`: Folder containing images used to encode faces for comparison.

## Credits

- [OpenCV](https://opencv.org/): Open Source Computer Vision Library.
- [face_recognition](https://github.com/ageitgey/face_recognition): Face recognition library by Adam Geitgey.
