import cv2
import numpy as np

white = (225, 225, 255)


def mapFromTo(x, a, b, c, d):
    y = (x-a)/(b-a)*(d-c)+c
    return y


def main():
    print(cv2.__version__)

    while True:
        x_frame = np.zeros([255, 600, 3], dtype=np.uint8)
        x_frame[:100, :100] = (0, 0, 225)

        y_frame = cv2.cvtColor(x_frame[:100, :100], cv2.COLOR_BGR2HSV)
        y_frame [:, :] = (100, 225, 225)
        y_frame = cv2.cvtColor(y_frame[:100, :100], cv2.COLOR_HSV2BGR)

        cv2.imshow("webcam1", x_frame)
        cv2.moveWindow("webcam1", 0, 10)
        cv2.imshow("webcam", y_frame)
        cv2.moveWindow("webcam", 610, 10)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
