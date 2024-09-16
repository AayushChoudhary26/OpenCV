import cv2

window_width = 640
window_height = 480

circle_radius = 5
coordinates = []

def left_click(event: int, x: int, y: int, flags: int, params: list) -> None:
    """Create a list of coordinates where the mouse was clicked

    Args:
        event (int): Specifies if event occured
        x (int): X coordinate of the mouse click
        y (int): Y coordinate of the mouse click
        flags (int): If any flags are set
        params (list): List of parameters
    """
    
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x,y))

cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", left_click)

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    
    for coordinate in coordinates:
        frame = cv2.circle(frame, coordinate, circle_radius, (255, 0, 0), -1)
        frame = cv2.putText(frame, f"X: {coordinate[0]}, Y: {coordinate[1]}", coordinate, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    cv2.imshow("Webcam", frame)
    
    keyEvent = cv2.waitKey(1)
    if keyEvent == ord('q'):
        break
    
    if keyEvent == ord('c'):
        coordinates = []

cam.release()
cv2.destroyAllWindows()