from pupil_apriltags import Detector
import argparse
import cv2
import os
import numpy as np 
os.environ['DISPLAY'] = ':0'
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image containing AprilTag")
# args = vars(ap.parse_args())
#print("test")
vid = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
width = vid.get(3)
height = vid.get(4)
fps = vid.get(5)

cx = int(width/2)
cy = int(height/2)

cxPlus = cx + 10
cyPlus = cy + 10

cxNeg = cx - 10
cyNeg = cy - 10


print(width)
print(height)

while(True):
    # load the input image and convert it to grayscale
    # print("[INFO] loading image...")
    # image = cv2.imread(args["image"])
    ret, image = vid.read()
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    # cv2.imshow("Image", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # moment = cv2.moments(gray)
    # X = int(moment ["m10"] / moment["m00"])
    # Y = int(moment ["m01"] / moment["m00"])
    cv2.circle(image, (cx, cy), 10, (0, 0, 200), 2)
    cv2.imshow("Image", image)

    # define the AprilTags detector options and then detect the AprilTags
    # in the input image
    # print("[INFO] detecting AprilTags...")
    # options = apriltag.DetectorOptions(families="tag36h11")
    # detector = apriltag.Detector(options)
    # results = detector.detect(gray)
    at_detector = Detector(
    families="tag36h11",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
    )
    results = at_detector.detect(gray)
    # print("[INFO] {} total AprilTags detected".format(len(results)))


    # loop over the AprilTag detection results
    for r in results:
        # extract the bounding box (x, y)-coordinates for the AprilTag
        # and convert each of the (x, y)-coordinate pairs to integers
        (ptA, ptB, ptC, ptD) = r.corners
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))
        # draw the bounding box of the AprilTag detection
        cv2.line(image, ptA, ptB, (0, 255, 0), 2)
        cv2.line(image, ptB, ptC, (0, 255, 0), 2)
        cv2.line(image, ptC, ptD, (0, 255, 0), 2)
        cv2.line(image, ptD, ptA, (0, 255, 0), 2)
        # draw the center (x, y)-coordinates of the AprilTag
        (cX, cY) = (int(r.center[0]), int(r.center[1]))
        cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
        if (cX >= cxNeg and cX <= cxPlus) and (cY >= cyNeg and cY <= cyPlus):
            cv2.circle(image, (cx, cy), 10, (0, 200, 0), 2)
            print("AprilTag is Centered")
        elif (cX < cxNeg and cY < cyNeg):
            print("Move Drone forward and right")
        elif (cX < cxNeg and cY > cyPlus):
            print("Move Drone backwards and right")
        elif (cX > cxPlus and cY > cyPlus):
            print("Move Drone backwards and left")
        elif (cX > cxPlus and cY < cyNeg):
            print("Move Drone forwards and left")
        else:
            print("Unknown Drone location")

 
        # draw the tag family on the image
        tagFamily = r.tag_family.decode("utf-8")
        cv2.putText(image, tagFamily, (ptA[0], ptA[1] - 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # print("[INFO] tag family: {}".format(tagFamily))
    # show the output image after AprilTag detection
        cv2.imshow("Image", image)
image.release()
cv2.destroyAllWindows()
