import cv2

window_width = 480
window_height = 240

mask_logo_size = 64
change_pos_step = 8

move_directions = ['left-up', 'left-down', 'right-up', 'right-down']
move_direction = move_directions[3]

current_x_pos = previous_x_pos = current_y_pos = previous_y_pos = 0
current_end_x_pos = previous_end_x_pos = current_x_pos + mask_logo_size
current_end_y_pos = previous_end_y_pos = current_y_pos + mask_logo_size

python_logo = cv2.resize(cv2.imread("images/python_logo.jpg"), (64, 64))
python_logo_gray = cv2.cvtColor(python_logo, cv2.COLOR_BGR2GRAY)
python_logo_BG_MASK = cv2.threshold(python_logo_gray, 230, 255, cv2.THRESH_BINARY)[1]
python_logo_FG_MASK = cv2.bitwise_not(python_logo_BG_MASK)
FG_frame = cv2.bitwise_and(python_logo, python_logo, mask=python_logo_FG_MASK)

def change_move_direction(current_x_pos: int, current_y_pos: int, current_end_x_pos: int, current_end_y_pos: int, previous_x_pos: int, previous_y_pos: int, previous_end_x_pos: int, previous_end_y_pos: int) -> None:
    """Change move direction for the bouncing box

    Args:
        current_x_pos (int): Current X position of the bouncing box
        current_y_pos (int): Current Y position of the bouncing box
        current_end_x_pos (int): Current end X position of the bouncing box
        current_end_y_pos (int): Current end Y position of the bouncing box
        previous_x_pos (int): Previous X position of the bouncing box
        previous_y_pos (int): Previous Y position of the bouncing box
        previous_end_x_pos (int): Previous end X position of the bouncing box
        previous_end_y_pos (int): Previous end Y position of the bouncing box
    """
    
    global move_direction, window_width, window_height

    if current_x_pos == 0 or current_y_pos == 0 or current_end_x_pos == window_width or current_end_y_pos == window_height:
        if (current_x_pos == 0 and previous_y_pos < current_y_pos) or (current_y_pos == 0 and previous_x_pos < current_x_pos):
            move_direction = move_directions[3]
        
        elif (current_x_pos == 0 and previous_y_pos > current_y_pos) or (current_end_y_pos == window_height and previous_end_x_pos < current_end_x_pos):
            move_direction = move_directions[2]
        
        elif (current_y_pos == 0 and previous_x_pos > current_x_pos) or (current_end_x_pos == window_width and previous_end_y_pos < current_end_y_pos):
            move_direction = move_directions[1]
        
        elif (current_end_x_pos == window_width and previous_end_y_pos > current_end_y_pos) or (current_end_y_pos == window_height and previous_end_x_pos > current_end_x_pos):
            move_direction = move_directions[0]

def bouncing_box(current_x_pos: int, current_y_pos: int, current_end_x_pos: int, current_end_y_pos: int) -> tuple[int, int, int, int]:
    """Change the position of the bouncing box

    Args:
        current_x_pos (int): Current X position of the bouncing box
        current_y_pos (int): Current Y position of the bouncing box
        current_end_x_pos (int): Current end X position of the bouncing box
        current_end_y_pos (int): Current end Y position of the bouncing box

    Returns:
        tuple[int, int, int, int]: New position of the bouncing box
    """
    
    global move_direction, change_pos_step
    
    if move_direction == move_directions[0]:
        current_x_pos -= change_pos_step
        current_end_x_pos -= change_pos_step
        current_y_pos -= change_pos_step
        current_end_y_pos -= change_pos_step
    
    elif move_direction == move_directions[1]:
        current_x_pos -= change_pos_step
        current_end_x_pos -= change_pos_step
        current_y_pos += change_pos_step
        current_end_y_pos += change_pos_step
    
    elif move_direction == move_directions[2]:
        current_x_pos += change_pos_step
        current_end_x_pos += change_pos_step
        current_y_pos -= change_pos_step
        current_end_y_pos -= change_pos_step
    
    elif move_direction == move_directions[3]:
        current_x_pos += change_pos_step
        current_end_x_pos += change_pos_step
        current_y_pos += change_pos_step
        current_end_y_pos += change_pos_step
    
    return (current_x_pos, current_y_pos, current_end_x_pos, current_end_y_pos)

cv2.namedWindow("Webcam")
cv2.namedWindow("Python Logo")
cv2.namedWindow("Python Logo BG Mask")
cv2.namedWindow("Python Logo FG Mask")
cv2.namedWindow("BG_frame")
cv2.namedWindow("FG_frame")
cv2.namedWindow("Frame_logo")
cv2.namedWindow("Final_frame")

cv2.moveWindow("Python Logo", window_width, 0)
cv2.moveWindow("Python Logo BG Mask", window_width * 2, 0)
cv2.moveWindow("Python Logo FG Mask", window_width * 3, 0)
cv2.moveWindow("FG_frame", window_width, window_height * 2)

cv2.imshow("Python Logo", python_logo_gray)
cv2.imshow("Python Logo BG Mask", python_logo_BG_MASK)
cv2.imshow("Python Logo FG Mask", python_logo_FG_MASK)
cv2.imshow("FG_frame", FG_frame)

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    
    current_x_pos, current_y_pos, current_end_x_pos, current_end_y_pos = bouncing_box(current_x_pos, current_y_pos, current_end_x_pos, current_end_y_pos)
    change_move_direction(current_x_pos, current_y_pos, current_end_x_pos, current_end_y_pos, previous_x_pos, previous_y_pos, previous_end_x_pos, previous_end_y_pos)
    
    print(f"Current X Pos: {current_x_pos}, Current Y Pos: {current_y_pos}, Current End X Pos: {current_end_x_pos}, Current End Y Pos: {current_end_y_pos}")
    
    BG_frame = cv2.bitwise_and(
        frame[current_y_pos:current_end_y_pos, current_x_pos:current_end_x_pos], 
        frame[current_y_pos:current_end_y_pos, current_x_pos:current_end_x_pos], 
        mask=python_logo_BG_MASK)
    
    frame_logo = cv2.add(FG_frame, BG_frame)
    final_frame = frame.copy()
    final_frame[current_y_pos:current_end_y_pos, current_x_pos:current_end_x_pos] = frame_logo
    
    cv2.moveWindow("Webcam", 0, 0)
    cv2.moveWindow("BG_frame", 0, window_height * 2)
    cv2.moveWindow("Frame_logo", window_width * 2, window_height * 2)
    cv2.moveWindow("Final_frame", window_width * 3, window_height * 2)
    
    cv2.imshow("Webcam", frame)
    cv2.imshow("BG_frame", BG_frame)
    cv2.imshow("Frame_logo", frame_logo)
    cv2.imshow("Final_frame", final_frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    previous_x_pos = current_x_pos
    previous_y_pos = current_y_pos
    previous_end_x_pos = current_end_x_pos
    previous_end_y_pos = current_end_y_pos

cam.release()
cv2.destroyAllWindows()