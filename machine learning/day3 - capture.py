import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to recored frame")
        break

    cv2.imshow("Webcam", frame)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("output.jpg", frame)
        print("Bahote sundar")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
