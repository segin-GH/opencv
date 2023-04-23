import cv2
import numpy as np

evt = 0
x_val = 0
y_val = 0


def mouse_click(event, x_pos, y_pos, flags, prams):
    global evt
    global x_val
    global y_val
    if (event == cv2.EVENT_LBUTTONDOWN):
        x_val = x_pos
        y_val = y_pos
        evt = event
    if (event == cv2.EVENT_LBUTTONUP):
        evt = event


def main():
    print(cv2.__version__)
    width = 640
    height = 460
    cam = cv2.VideoCapture(2)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv2.CAP_PROP_FPS, 30)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
    cv2.namedWindow('webcam')
    cv2.setMouseCallback('webcam', mouse_click)

    while True:
        _, frame = cam.read()
        if evt is 1:
            x = np.zeros([250, 250, 3], dtype=np.uint8)
            clr = frame[y_val, x_val]
            print(clr)
            x[:, :] = clr
            cv2.putText(x, str(clr), (0, 50),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
            cv2.imshow("color_picker", x)
            cv2.moveWindow("color_picker", width, 0)

        cv2.imshow("webcam", frame)
        cv2.moveWindow("webcam", 0, 0)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cam.release()


if __name__ == "__main__":
    main()
