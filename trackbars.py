import cv2

window_width = 640
window_height = 480

cv2.namedWindow("Webcam")
cv2.createTrackbar("xVal", "Webcam", 25, window_width, lambda _: None)
cv2.createTrackbar("yVal", "Webcam", 25, window_height, lambda _: None)
cv2.createTrackbar("width", "Webcam", 25, window_width, lambda _: None)
cv2.createTrackbar("height", "Webcam", 25, window_height, lambda _: None)

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    
    xVal = cv2.getTrackbarPos("xVal", "Webcam") # Bar for changing box X coordinate
    yVal = cv2.getTrackbarPos("yVal", "Webcam") # Bar for changing box Y coordinate
    width = cv2.getTrackbarPos("width", "Webcam") # Bar for changing box width
    height = cv2.getTrackbarPos("height", "Webcam") # Bar for changing box height
    
    frame = cv2.rectangle(frame, (xVal, yVal), (xVal + width, yVal + height), (255, 0, 0), 2)
    
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()