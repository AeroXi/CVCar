from vision import process
from control import *
import cv2


def main():
    p = float(input('p = '))
    angle_threshold = int(input('angle threshold = '))
    cap = cv2.VideoCapture(0)
    last_angle = 0
    angle = 0
    while True:
        ret, frame = cap.read()
        result, position = process(frame)

        angle = 0
        if position != -1000:
            angle = get_angle(position, p)
            if abs(angle - last_angle) < angle_threshold:
                print(angle)
            last_angle = angle

        cv2.namedWindow("capture", cv2.WINDOW_NORMAL)
        cv2.imshow("capture", result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == '__main__':
    main()