import cv2

window_width = 640
window_height = 480

color_bouncing_box_size = 100
change_pos_step = 10

move_directions = ['left-up', 'left-down', 'right-up', 'right-down']
move_direction = move_directions[3]

current_x_pos = previous_x_pos = current_y_pos = previous_y_pos = 0
current_end_x_pos = previous_end_x_pos = current_x_pos + color_bouncing_box_size
current_end_y_pos = previous_end_y_pos = current_y_pos + color_bouncing_box_size

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

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    frame = cv2.resize(frame, (window_width, window_height))
    frame = cv2.flip(frame, 1)
    
    grayframe = frame.copy()
    grayframe = cv2.cvtColor(grayframe, cv2.COLOR_BGR2GRAY)
    
    cv2.moveWindow("Webcam", 0, 0)
    
    current_x_pos, current_y_pos, current_end_x_pos, current_end_y_pos = bouncing_box(current_x_pos, current_y_pos, current_end_x_pos, current_end_y_pos)
    change_move_direction(current_x_pos, current_y_pos, current_end_x_pos, current_end_y_pos, previous_x_pos, previous_y_pos, previous_end_x_pos, previous_end_y_pos)
    
    grayframe = cv2.rectangle(grayframe, (current_x_pos, current_y_pos), (current_end_x_pos, current_end_y_pos), (0, 0, 255), 3)
    grayframe = cv2.cvtColor(grayframe, cv2.COLOR_GRAY2BGR)
    grayframe[current_y_pos:current_end_y_pos, current_x_pos:current_end_x_pos] = frame[current_y_pos:current_end_y_pos, current_x_pos:current_end_x_pos]
    
    cv2.imshow("Webcam", grayframe)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    previous_x_pos = current_x_pos
    previous_y_pos = current_y_pos
    previous_end_x_pos = current_end_x_pos
    previous_end_y_pos = current_end_y_pos

cam.release()
cv2.destroyAllWindows()