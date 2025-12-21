import cv2 as cv

for i in range(0, 5):
    cap = cv.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i} WORKS")
    else:
        print(f"Camera {i} does NOT work")
    cap.release()
