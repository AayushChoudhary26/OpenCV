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