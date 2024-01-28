import cv2

img = cv2.imread('lena.jpg', 0)  # imread read image in gray shade
# and image in matrix format

print(img)  # print the matrix

cv2.imshow('image', img)  # imshow method show the image
# and it will show image quickly and disappear. To add wait and waitkey method
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()  # it will close all new window
elif k == ord('s'):
    cv2.imwrite('lena_gray.png', img)  # create new file
    cv2.destroyAllWindows()
