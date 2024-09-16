import cv2

window_width = 640
window_height = 480

points = ()
evt = 0

def get_color(event, x, y, flags, params):
    global points, evt
    
    if event == cv2.EVENT_LBUTTONDOWN:
        points = (x, y)
        evt = event

cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", get_color)

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    
    if evt == cv2.EVENT_LBUTTONDOWN:
        frame = cv2.putText(frame, f"Color: {frame[points[1]][points[0]]}", points, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()