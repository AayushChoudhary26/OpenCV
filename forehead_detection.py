import cv2

window_width = 640
window_height = 480

def get_positions(cascade_filename: str, frame: cv2.VideoCapture) -> tuple[int, int, int, int]:
    """Get position of cascades detected in the frame

    Args:
        cascade_filename (str): Name of the cascade file

    Returns:
        tuple[int, int, int, int]: Position of the cascades
    """
    
    cascade = cv2.CascadeClassifier(cascade_filename)
    object_postitions = cascade.detectMultiScale(frame, 1.3, 5)
    
    return object_postitions

def detect_forehead(face_position: tuple, left_position: tuple | None = None, right_position: tuple | None = None) -> tuple[int, int]:
    """Detect forehead in the frame

    Args:
        face_position (tuple): Position of the face
        eye_positions (tuple): Position of the eyes

    Returns:
        tuple[int, int, int, int]: Position of the forehead
    """
    
    _, face_y, _, _ = face_position
    forehead_position_x = 0
    forehead_position_y = 0
    
    left_eye_available: bool = False if len(left_position) == 0 else True
    right_eye_available: bool = False if len(right_position) == 0 else True
    
    if left_eye_available or right_eye_available:
        if right_eye_available:
            right_eye_x, right_eye_y, _, _ = right_position
            forehead_position_y = face_y + ((right_eye_y - face_y) // 2)
            print(f"Forhead Position Y: {forehead_position_y}")
        
        if left_eye_available and forehead_position_y == 0:
            left_eye_x, left_eye_y, left_eye_w, _ = left_position
            forehead_position_y = face_y + ((left_eye_y - face_y) // 2)
            print(f"Forhead Position Y: {forehead_position_y}")

        if left_eye_available and right_eye_available:
            right_eye_x, _, _, _ = right_position
            left_eye_x, _, left_eye_w, _ = left_position
            forehead_position_x = (left_eye_x + left_eye_w) + (((right_eye_x) - (left_eye_x + left_eye_w)) // 2)
        
            print(f"Forehead Position X: {forehead_position_x}, Forehead Position Y: {forehead_position_y}")
        
            return (forehead_position_x, forehead_position_y)
        
    return []

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    eye_positions = get_positions("xml_files/haarcascade_eye.xml", gray_frame)
    face_positions = get_positions("xml_files/haarcascade_frontalface_default.xml", gray_frame)
    
    for left_eye_position, right_eye_position, face_position in zip(eye_positions[::2], eye_positions[1::2], face_positions):
        print(f"Face Position: {face_position}, Left Eye Position: {left_eye_position}, Right Eye Position: {right_eye_position}")
        
        # cv2.rectangle(frame, (left_eye_position[0], left_eye_position[1]), (left_eye_position[0] + left_eye_position[2], left_eye_position[1] + left_eye_position[3]), (0, 255, 0), 2)
        # cv2.rectangle(frame, (right_eye_position[0], right_eye_position[1]), (right_eye_position[0] + right_eye_position[2], right_eye_position[1] + right_eye_position[3]), (0, 255, 0), 2)
        # cv2.rectangle(frame, (face_position[0], face_position[1]), (face_position[0] + face_position[2], face_position[1] + face_position[3]), (255, 0, 0), 2)
        
        forhead_position = detect_forehead(face_position, left_eye_position, right_eye_position)
        
        if len(forhead_position) != 0:
            forehead_position_x, forehead_position_y = forhead_position
            cv2.line(frame, (forehead_position_x, 0), (forehead_position_x, window_height), (0, 0, 255), 2)
            cv2.line(frame, (0, forehead_position_y), (window_width, forehead_position_y), (0, 0, 255), 2)
            
            cv2.circle(frame, (forehead_position_x, forehead_position_y), 5, (0, 0, 255), -1)
            cv2.circle(frame, (forehead_position_x, forehead_position_y), 30, (0, 0, 255), 2)
    
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()