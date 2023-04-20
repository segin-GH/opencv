import cv2
import numpy as np


def main():
    boardSize = int(input("Enter your board size: "))
    numSquares = int(input("How many squares: "))
    squareSize = int(boardSize / numSquares)

    darkColor = (0, 0, 0)
    lightColor = (0, 0, 100)
    nowColor = darkColor

    while True:
        x = np.zeros([boardSize, boardSize, 3], dtype=np.uint8)  # type: ignore

        for row in range(0, numSquares):
            for column in range(0, numSquares):
                x[
                    squareSize * row : squareSize * (row + 1),
                    squareSize * column : squareSize * (column + 1),
                ] = nowColor
                if nowColor == darkColor:
                    nowColor = lightColor
                else:
                    nowColor = darkColor

            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor
        cv2.imshow("board", x)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
