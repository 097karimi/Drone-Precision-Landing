import cv2 as cv

def center_of_aruco(corners):
    if corners == []:
        return (0,0)
    for corner in corners:
        center_of_aruco_on_x = (corner[0][0][0] + corner[0][1][0] + corner[0][2][0] + corner[0][3][0]) / 4
        center_of_aruco_on_Y = (corner[0][0][1] + corner[0][1][1] + corner[0][2][1] + corner[0][3][1]) / 4
    return (int(center_of_aruco_on_x), int(center_of_aruco_on_Y))

def center_of_camera(cap):
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)/2)
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)/2)
    return (w, h)

def estimate_error(center_of_aruco_on_x, center_of_aruco_on_y, center_of_camera_on_x, center_of_camera_on_y):
    error_x = int(center_of_aruco_on_x) - center_of_camera_on_x
    error_y = (int(center_of_aruco_on_y) - center_of_camera_on_y) * -1
    return (error_x, error_y)

def show_on_screen(frame, lable_text_dict, axix_y=20):
    for k, v in lable_text_dict.items():
        cv.putText(frame, str(k), (10, axix_y),
        cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv.putText(frame, str(v), (90, axix_y),
        cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        axix_y += 20

def identify_corners(corners):
    point_one   = (int(corners[0][0][0][0]), int(corners[0][0][0][1]))
    point_two   = (int(corners[0][0][1][0]), int(corners[0][0][1][1]))
    point_three = (int(corners[0][0][2][0]), int(corners[0][0][2][1]))
    point_four  = (int(corners[0][0][3][0]), int(corners[0][0][3][1]))
    return (point_one, point_two, point_three, point_four)

def draw_rectangle(frame,one,two,three,four):
    cv.line(frame, one, two, color=(255,0,0), thickness=3)
    cv.line(frame, one, four, color=(0,255,0), thickness=3)
    cv.line(frame, two, three, color=(255,0,0), thickness=3)
    cv.line(frame, three, four, color=(255,0,0), thickness=3)
