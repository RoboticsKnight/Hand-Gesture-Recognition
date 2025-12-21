import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera failed to open.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame read FAILED")
        break
    
    cv.imshow("Test", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
