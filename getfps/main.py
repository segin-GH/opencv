import time

import cv2


def main():
    print(cv2.__version__)
    width = 640
    height = 460
    cam = cv2.VideoCapture(2)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv2.CAP_PROP_FPS, 30)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
    previousTime = time.time()

    while True:
        ignore, frame = cam.read()
        printFPS(previousTime, frame)
        previousTime = time.time()
        cv2.imshow("webcam", frame)
        cv2.moveWindow("webcam", 0, 0)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cam.release()


def printFPS(previousTime, frame):
    currentTime = time.time() - previousTime
    fps = 1 / currentTime
    cv2.rectangle(frame, (0, 0), (100, 20), (255, 255, 255), -1)
    cv2.putText(
        frame,
        "FPS:" + str(int(fps)),
        (2, 15),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        0.8,
        (0, 0, 0),
        1,
    )


if __name__ == "__main__":
    main()
