import cv2
import pyzbar.pyzbar as pyzbar
import argparse
from PIL import Image
import numpy as np
import sys
from Result import Result

class ImageAnalysis:
    def returnResult(self, mat):
        frame = mat

        result = Result()
        # START QR
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            pArray = np.array_split(obj.polygon,4)
            p1,p2,p3,p4=pArray
            result.add_qr(obj.data,p1,p2,p3,p4)

        # START CIRCLES
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        gray = cv2.GaussianBlur(gray, (9, 9), 2, 2)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 100, param1=120, param2=90, minRadius=100, maxRadius=360)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                radius = np.round(i[2])
                result.add_circle(center, radius)

        return result