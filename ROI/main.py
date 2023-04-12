import cv2

def main():
    print(cv2.__version__)
    width = 640
    height = 460
    cam = cv2.VideoCapture(2)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv2.CAP_PROP_FPS, 30)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    while True:
        ignore, frame = cam.read()
        frame_roi = frame[100:210, 250:390]
        frame_gray_roi = cv2.cvtColor(frame_roi, cv2.COLOR_BGR2GRAY)
        frame_gray_roi = cv2.cvtColor(frame_gray_roi, cv2.COLOR_GRAY2BGR)
        frame[100:210, 250:390] = frame_gray_roi

        cv2.imshow('webcam', frame)
        cv2.moveWindow('webcam', 0, 0)
        cv2.imshow('myROI', frame_roi)
        cv2.moveWindow('myROI', 650, 0)
        cv2.imshow('myGrayROI', frame_gray_roi)
        cv2.moveWindow('myGrayROI', 650, 300)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cam.release()


if __name__ == "__main__":
    main()
