import cv2 
import numpy as np

def main():
    while True:
        frame = np.zeros([400,400,3],dtype = np.uint8)  # type: ignore
        frame[:,:] = [255,255,255]
        for i in range(0,400,50):
            j = 50 + i
            k = 100 + i 
            l = 150 + i
            m = 200 + i
            frame[i:j,j:k] = [0,0,0]
            frame[j:k,i:j] = [0,0,0]
            frame[:j,l:] = [0,0,0]
            frame[l:,:j] = [0,0,0]
            cv2.imshow('MyWindow',frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

if __name__ == "__main__":
    main()