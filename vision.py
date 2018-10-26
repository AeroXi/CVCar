import cv2
cap = cv2.VideoCapture(0)


def process(image):
    height, width, depth = image.shape
    half_width = width / 20
    image = cv2.resize(image, (int(width/10), int(height/10)), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (11, 11),0)
    ret,thresh = cv2.threshold(blur, 140, 255, cv2.THRESH_BINARY)
    pic, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 200, 0))
    try:
        cnt = contours[0]
        M = cv2.moments(cnt)
        centroid_x = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.line(image, (centroid_x, 0), (centroid_x, 255), (200, 0, 0))
        position = centroid_x - half_width
    except:
        position = -1000
        pass
    return image, position


def main():
    while (True):
        ret, frame = cap.read()
        result, position= process(frame)
        cv2.namedWindow("capture", cv2.WINDOW_NORMAL)
        cv2.imshow("capture", result)
        print(position)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == '__main__':
    main()

