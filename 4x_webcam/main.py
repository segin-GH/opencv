import cv2 as cv


def main():
    cam = cv.VideoCapture(2)

    while 1:
        ignore, frame = cam.read()
        greayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("cam1", greayframe)
        cv.imshow("cam2", frame)
        cv.imshow("cam3", frame)
        cv.imshow("cam4", greayframe)
        cv.moveWindow("cam1", 0, 0)
        cv.moveWindow("cam2", 640, 0)
        cv.moveWindow("cam3", 0, 640)
        cv.moveWindow("cam4", 640, 1000)

        if cv.waitKey(1) & 0xFF == ord("q"):  #
            break

    cam.release()


if __name__ == "__main__":
    main()
