import cv2

img = cv2.imread("L20-CoinsAndCandys.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
edges = cv2.Canny(img, 200, 200)

cv2.imshow("pampalini", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

