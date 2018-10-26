def p_control(position, p):
    angle = position * p
    return angle


def get_angle(position, p):
    angle = p_control(position, p)
    if angle in range(-45, 45):
        return angle
    elif angle > 45:
        return 45
    elif angle < -45:
        return -45


def main():

    return 0


if __name__ == '__main__':
    main()