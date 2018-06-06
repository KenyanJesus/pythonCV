import cv2
#from pyzbar.pyzbar import decode
#from PIL import Image
import numpy as np
import sys

def main(argv):
    while(True):
        cam = cv2.VideoCapture(0)
        #    default_file = "C:/Users/Ejer/Desktop/python/hello/1639.jpg"
        filename = argv[0] if len(argv) > 0 else cam.read()[1]

        src = filename
        # Check if image is loaded fine
        if src is None:
            print ('Error opening image!')
            return -1

        gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
        gray = cv2.GaussianBlur(gray, (9, 9), 2, 2)

        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 100, param1=120, param2=90, minRadius=100, maxRadius=360)

        if circles is None:
            print("no circles")
            cv2.imshow("detected circles", gray)
            cv2.waitKey(0)
        if circles is not None:
            data = circles[0][0]
            x=data[0]
            y=data[1]
            radius = np.round(data[2])
            print(y,x, radius)
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(gray, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(gray, center, radius, (255, 0, 255), 3)
            cv2.imshow("detected circles", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return 0



#def avgCircle(runningBiggestCircle, x):
#    width = 640
#    height = 360
#    xmaxdiff=width*x
#    ymaxdiff=height*x

if __name__ == '__main__':
    main(sys.argv[1:])