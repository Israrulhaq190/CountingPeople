import cv2
import numpy as np
from utils import transform

def draw(name_of_window, img_copy):
    points_of_intresting_place = []
    up_line = []
    down_line = []
    diction = {'w': ['white',(255,255,255)],
               'r': ['red_up_line',(0,0,255)],
               'b': ['blue_down_line',(255,0,0)]}
    ix = -1
    iy = -1
    mode = 'w'
    def draw_circle(event,x,y,flags,param): 
        nonlocal points_of_intresting_place,ix,iy,mode,up_line,down_line
        if event == cv2.EVENT_LBUTTONDOWN:
            ix = x
            iy = y
            if mode == 'w': # область интереса  
                points_of_intresting_place.append((x,y))
            elif mode == 'r':
                up_line.append((x,y))
            elif mode == 'b':
                down_line.append((x,y))
        elif event == cv2.EVENT_LBUTTONUP:
            if mode == 'w':
                cv2.rectangle(img_copy,(ix,iy),(x,y),(255,255,255),1)
                points_of_intresting_place.append((x,y))
            elif mode == 'r':
                cv2.line(img_copy,(ix,iy),(x,y),(0,0,255),2)
                up_line.append((x,y))
            elif mode == 'b':
                cv2.line(img_copy,(ix,iy),(x,y),(255,0,0),2)
                down_line.append((x,y))
    cv2.namedWindow(name_of_window)
    while True :
        img = np.copy(img_copy)
        cv2.setMouseCallback(name_of_window, draw_circle)
        cv2.putText(img, diction[mode][0], (28,17), cv2.FONT_HERSHEY_SIMPLEX, 0.65,diction[mode][1], 1, cv2.LINE_AA)
        cv2.imshow(name_of_window, img)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('q'):
            break
        elif k == ord('m'):
            mode = 'r'
        elif k == ord('n'):
            mode = 'b'
        elif k == ord('b'):
            mode = 'w'
    cv2.destroyAllWindows()
    return {'intresting_zone': transform.rect_to_point_for_line(points_of_intresting_place), 'red_up_line': up_line,\
            'blue_down_line': down_line}
