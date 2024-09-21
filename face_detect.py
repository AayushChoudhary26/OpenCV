import cv2

window_width = 640
window_height = 480

def get_positions(cascade_filename: str) -> tuple[int, int, int, int]:
    """Get position of cascades detected in the frame

    Args:
        cascade_filename (str): Name of the cascade file

    Returns:
        tuple[int, int, int, int]: Position of the cascades
    """
    
    cascade = cv2.CascadeClassifier(cascade_filename)
    object_postitions = cascade.detectMultiScale(gray_frame, 1.3, 5)
    
    return object_postitions

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    for (x, y, w, h) in get_positions("xml_files/haarcascade_eye.xml"):
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    for (x, y, w, h) in get_positions("xml_files/haarcascade_frontalface_default.xml"):
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()