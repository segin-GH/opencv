import cv2

evt = 0


def mouse_click(event, xPos, yPos, flag, params):
    global evt
    global pnt1
    global pnt2
    global pnt3
    global pnt4

    global pnt5
    global pnt6
    if event is cv2.EVENT_LBUTTONDOWN:
        print("Mouse Event was L D : ", event)
        print(f"at position,x={xPos}, y={yPos}")
        evt = event
        pnt1 = xPos
        pnt2 = yPos
        pnt5 = (xPos, yPos)
    if event is cv2.EVENT_LBUTTONUP:
        print("Mouse Event was L U : ", event)
        print(f"at position,x={xPos}, y={yPos}")
        evt = event
        pnt3 = xPos
        pnt4 = yPos
        pnt6 = (xPos, yPos)
    if event is cv2.EVENT_RBUTTONUP:
        print("Mouse Event was R U : ", event)
        print(f"at position,x={xPos}, y={yPos}")
        evt = event


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
        ign, frame = cam.read()
        if evt == 4:
            roi_frame = frame[pnt2: pnt4, pnt1: pnt3]
            #   verifying that both width and height are greater than 0.
            if roi_frame.shape[0] > 0 and roi_frame.shape[1] > 0:
                cv2.rectangle(frame, (pnt5), (pnt6), (0, 255, 0), 2)
                # print(pnt5)
                # print(pnt6)
                cv2.imshow('roi frame', roi_frame)
                cv2.moveWindow('roi frame', int(width*1.1), 0)
        cv2.imshow('webcam', frame)
        cv2.moveWindow('webcam', 10, 20)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cam.release()


if __name__ == "__main__":
    main()
