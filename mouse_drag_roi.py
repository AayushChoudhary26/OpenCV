import cv2

window_width: int = 640 # Height of the cv2 window
window_height: int = 480 # Width of the cv2 window

points_1: tuple = () # Points of mouse down event
points_2: tuple = () # Points of mouse up event

if_mouse_up = 0 # Checking if mouse press is released

def mouse_drag(event: int, x: int, y: int, flags: int, params: list) -> None:
    """Get the points at which the mouse was clicked

    Args:
        event (int): Specifies if event occured
        x (int): X coordinate of the mouse click
        y (int): Y coordinate of the mouse click
        flags (int): If any flags are set
        params (list): List of parameters
    """
    
    global points_1, points_2, if_mouse_up
    
    if event == cv2.EVENT_LBUTTONDOWN:
        points_1 = (x, y)
        if_mouse_up = 0

    elif event == cv2.EVENT_LBUTTONUP:
        points_2 = (x, y)
        if_mouse_up = 1
        
cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", mouse_drag)

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    
    cv2.moveWindow("Webcam", 0, 0)
    
    if if_mouse_up == 1:
        frame = cv2.rectangle(frame, points_1, points_2, (255, 0, 0), 2)
        roi_frame = frame[points_1[1]:points_2[1], points_1[0]:points_2[0]]
        
        cv2.moveWindow("ROI", window_width, 0)
        # cv2.resizeWindow("ROI", points_2[0] - points_1[0], points_2[1] - points_1[1])
        
        cv2.imshow("ROI", roi_frame)
    
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()