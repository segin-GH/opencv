import cv2 
import numpy as np

def main():
    while True:
       #some code to implement 
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

if __name__ == "__main__":
    main()