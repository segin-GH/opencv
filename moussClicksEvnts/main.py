import cv2


def mouse_click(event, xPos, yPos, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse Event was: ", event)
        print(f"at position,{xPos}, {yPos}")
    if event == cv2.EVENT_LBUTTONUP:
        print("Mouse Event was: ", event)
        print(f"at position,{xPos}, {yPos}")


def main():

    print(cv2.__version__)
    width = 640
    height = 460
    cam = cv2.VideoCapture(2)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv2.CAP_PROP_FPS, 30)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cv2.namedWindow('webcam')
    cv2.setMouseCallback('webcam', mouse_click)

    while True:
        _, frame = cam.read()
        cv2.imshow('webcam', frame)
        cv2.moveWindow('webcam', 10, 20)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cam.release()


if __name__ == "__main__":
    main()
