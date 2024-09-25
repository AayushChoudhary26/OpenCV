# OpenCV-based Video Manipulation and Object Tracking

This repository is being used to track the progress of various OpenCV-based programs. Below are the descriptions of different programs included in this repository, ranging from basic OpenCV usage to more advanced projects.

## 1. Basic Webcam Display

```python

import cv2

window_width = 640
window_height = 480

cv2.namedWindow("Webcam")

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    
    cv2.imshow("Webcam", frame)
    cv2.moveWindow("Webcam", 0, 0)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

```

This is a simple program to capture and display the webcam feed using OpenCV. The video feed is resized and flipped horizontally before being displayed in a window titled "Webcam." The user can exit the program by pressing the 'q' key. It demonstrates the basic principles of capturing video, resizing frames, and displaying images using OpenCV.

## 2. Get Color on Mouse Click

This program captures the webcam feed and allows the user to click on the window to get the color of the pixel at the clicked position. When the user clicks, it displays the RGB values of the pixel at that point in the video frame. The program uses OpenCV's mouse callback feature to detect clicks, capture the coordinates, and display color values on the video feed.

### How `get_color.py` works

- The webcam feed is captured and displayed in real-time.
- A callback function is set to detect mouse clicks.
- On a left-click, the program retrieves the coordinates and fetches the pixel’s color at that point.
- The color values are displayed on the video frame.

## 3. Bouncing Box

This program creates a bouncing rectangle within the webcam feed. The rectangle moves in a certain direction and changes its direction upon hitting the boundaries of the frame. The movement directions are controlled based on collision detection with the frame's edges.

### How `bouncing_box.py` works

- A rectangle is drawn at an initial position and moves based on pre-defined directions (up-left, down-left, up-right, down-right).
- The rectangle changes its direction when it hits the window boundaries.
- The rectangle’s position is updated frame by frame to simulate bouncing within the window.

## 4. Bouncing Masked Logo

This advanced program bounces a Python logo within the webcam feed. The logo moves around the window, and its direction changes when it hits the window boundaries. A mask is used to blend the logo with the background, making the background of the logo transparent.

### How `bouncing_mask_logo.py` works

- The webcam feed is captured, and the Python logo is loaded and resized.
- Background and foreground masks are created to remove the logo's background and overlay it on the webcam feed.
- The logo moves in different directions and bounces when it touches the edges of the frame.
- The program uses OpenCV bitwise operations to blend the logo seamlessly with the video feed.

## 5. Forhead Detection / Aimbot

This advanced project uses Haar cascades to detect faces and eyes in real-time using the webcam feed. It identifies the position of the forehead by calculating the midpoint between the detected eyes. The program then draws target lines over the forehead for aiming purposes, simulating a basic "aimbot" behavior.

### How `forhead_detection.py` works

- Haar cascades are used to detect the face and eyes within the webcam feed.
- The program calculates the position of the forehead based on the eye positions.
- Target lines and circles are drawn at the detected forehead position, visually marking it in the frame.
- This simulates an "aimbot" by pinpointing the forehead region for precise targeting.

---

This repository documents the progress in OpenCV-based video manipulation and object tracking programs. Each program is progressively more complex, demonstrating the power and flexibility of OpenCV for real-time computer vision applications.
