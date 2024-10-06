import cv2
import numpy

window_width = 640
window_height = 480

points = ()
evt = 0

hue = sat = val = 100

def onclick(event, x, y, flags, params):
    global points, evt
    
    if event == cv2.EVENT_LBUTTONDOWN:
        points = (x, y)
        evt = event

cv2.namedWindow("Webcam")
cv2.namedWindow("Composite")

cv2.moveWindow("Webcam", 0, 0)
cv2.moveWindow("Composite", window_width, 0)

cv2.setMouseCallback("Webcam", onclick)

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if evt == cv2.EVENT_LBUTTONDOWN:
        hue, sat, val = hsv[points[1]][points[0]]
    
    lower_bound = numpy.array([hue - 30, sat - 15, val - 20])
    upper_bound = numpy.array([hue + 30, sat + 15, val + 20])

    FG_mask = cv2.inRange(hsv, lower_bound, upper_bound)
    BG_mask = cv2.bitwise_not(FG_mask)

    FG_frame = cv2.bitwise_and(frame, frame, mask=FG_mask)
    BG_frame = cv2.cvtColor(BG_mask, cv2.COLOR_GRAY2BGR)

    composite_frame = cv2.add(FG_frame, BG_frame)

    contours = cv2.findContours(FG_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for contour in contours:
        if cv2.contourArea(contour) > 50:
            x, y, w, h = cv2.boundingRect(contour)
            print(f"X: {x}, Y: {y}, W: {w}, H: {h}")

            cv2.line(frame, (x + w // 2, 0), (x + w // 2, window_height), (255, 0, 0), 2)
            cv2.line(frame, (0, y + h // 2), (window_width, y + h // 2), (255, 0, 0), 2)
    
    cv2.imshow("Webcam", frame)
    cv2.imshow("Composite", composite_frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()