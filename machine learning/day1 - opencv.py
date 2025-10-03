import cv2

img = cv2.imread(r"C:\Users\kushu\OneDrive\Desktop\Hathi\Learnings\machine learning\image.jpg")

# print(img.shape)

# cv2.imshow("My Image", img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Gray Image", gray)

# print(gray.shape)

cv2.line(img, (50,50), (200, 200), (255, 0, 0), 3)

cv2.rectangle(img, (100,100), (300, 300), (0, 255, 0), 2)

cv2.circle(img, (250, 250), 100, (0, 0, 255), -1)

cv2.putText(img, "Hathi Kushu Shukla", (50,50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Shapes", img)

cv2.waitKey()

cv2.destroyAllWindows()