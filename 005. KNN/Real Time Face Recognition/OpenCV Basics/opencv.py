# Sample Program to read and display images

# importing modules
import cv2

# Reading the image
img=cv2.imread("sample.jpg")

# Reading as Grayscale image
gray = cv2.imread('sample.jpg',cv2.IMREAD_GRAYSCALE)


# Displaying the image (<title of the window>,<img object>)
cv2.imshow("Doggo!",img)
cv2.imshow("Gray Doggo!",gray)

# 0 - puts window to hold unless I destroy it myself
cv2.waitKey(0)
cv2.destroyAllWindows()
