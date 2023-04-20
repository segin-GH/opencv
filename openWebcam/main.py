import cv2


def main():
    print(cv2.__version__)
    cam = cv2.VideoCapture(2)
    while True:
        ignore, frame = cam.read()
        # greayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("myWebcam", frame)
        cv2.moveWindow("myWebcam", 0, 0)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cam.release()


if __name__ == "__main__":
    main()
