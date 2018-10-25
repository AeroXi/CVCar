from vision import *
from control import *


def main():
    p = float(input('p = '))
    cap = cv2.VideoCapture(0)
    last_position = 0
    while True:
        ret, frame = cap.read()
        result, position = process(frame)
        if position == -100:
            angle = p_control(last_position, p)
        else:
            angle = p_control(position, p)
        print(f'angle = {angle}')
        cv2.namedWindow("capture", cv2.WINDOW_NORMAL)
        cv2.imshow("capture", result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == '__main__':
    main()