import cv2


def process_track_bar(val):
    global x_pos
    print(f"XPos:{val}")
    x_pos = val


def process_track_bar2(val):
    global y_pos
    print(f"YPos:{val}")
    y_pos = val


def process_track_bar3(val):
    global radius
    print(f"Radius:{val}")
    radius = val


def main():
    print(cv2.__version__)
    width = 640
    height = 460

    global x_pos
    global y_pos
    global radius
    radius = 25
    x_pos = int(width / 2)
    y_pos = int(height / 2)

    cam = cv2.VideoCapture(2)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv2.CAP_PROP_FPS, 30)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
    cv2.namedWindow("myTrackBars")
    cv2.resizeWindow("myTrackBars", 400, 500)
    cv2.moveWindow("myTrackBars", width, 100)
    cv2.createTrackbar("trackBarX", "myTrackBars", 0, 1920, process_track_bar)
    cv2.createTrackbar("trackBarY", "myTrackBars", 0, 1080, process_track_bar2)
    cv2.createTrackbar("Radius", "myTrackBars", 0,
                       int(height/2), process_track_bar3)

    while True:
        _, frame = cam.read()
        cv2.circle(frame, (x_pos, y_pos), radius, (255, 0, 0), 2)
        cv2.imshow("webcam", frame)
        cv2.moveWindow("webcam", 0, 0)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cam.release()


if __name__ == "__main__":
    main()
