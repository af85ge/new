import cv2 as cv
import numpy as np


img = np.zeros((500, 500, 3), dtype=np.uint8)
p = 0
while True:
    
    copy_img = img.copy()
    p += 1
    print(p)
    cv.arrowedLine(
        copy_img, (0 + p, 0 + p), (50 + p, 50 + p), (0, 255, 0), 6, cv.LINE_AA
    )
    cv.imshow("img", copy_img)
    k = cv.waitKey(30)
    if k == ord("q"):
        break
cv.destroyAllWindows()
