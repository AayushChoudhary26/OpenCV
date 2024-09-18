# AI Programming Progress Tracker

This repository is dedicated to tracking my progress in writing various AI-related programs. These initial programs involve basic interactions with the webcam using OpenCV, focusing on concepts like tracking motion, detecting mouse events, and using trackbars to manipulate shapes in real time.

## Programs

### 1. `bouncing_box.py`
This script creates a bouncing box animation on a webcam feed. The box moves in different directions and changes direction when it hits the boundaries of the window.

- **Libraries**: OpenCV (`cv2`)
- **Features**:
  - Detects window boundaries and changes movement direction
  - Displays a rectangle bouncing within the window frame
  - Press 'q' to quit the application

### 2. `track_mouse.py`
This script tracks mouse clicks on the webcam feed, drawing circles at the clicked coordinates and displaying their x, y values. It also provides an option to clear the screen.

- **Libraries**: OpenCV (`cv2`)
- **Features**:
  - Detects left mouse button clicks and displays a circle at the click position
  - Displays coordinate values near the circle
  - Press 'q' to quit the application
  - Press 'c' to clear all circles from the screen

### 3. `trackbars.py`
This program allows you to adjust a rectangle's position and size dynamically using trackbars, which control the x, y coordinates and the width, height of the rectangle on the webcam feed.

- **Libraries**: OpenCV (`cv2`)
- **Features**:
  - Adjustable trackbars for controlling the rectangle’s position and dimensions
  - Real-time display of the rectangle as the values are adjusted
  - Press 'q' to quit the application

### 4. `bouncing_masked_logo.py`
This program expresses how to mask a image to add it to the camera fram or another image. The logo is then bounced like bouncing box, the parts where logo is colored is diplayed on the frame, else it is replaced by the background camera frame

- **Libraries**: OpenCV (`cv2`)
- **Features**:
  - Changeable images and sizes to control logo displaced on the frame
  - Bouncing steps can be changed to make the speed of logo increase or decrease
  - Press 'q' to quit the application

## Requirements
- Python 3.x
- OpenCV (`cv2`)

To install OpenCV:
```bash
pip install opencv-python
```

## How to Run
Each script can be run by executing the Python file in your terminal or command line:
```bash
python <script_name.py>
```
Make sure your webcam is accessible.

## Future Work
This repository will be updated with more AI programs, building upon these fundamental concepts. Stay tuned!