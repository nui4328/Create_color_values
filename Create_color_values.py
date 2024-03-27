import cv2

def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        bgr_color = image[y, x]  # ค่าสี BGR ของจุดที่คลิก
        hsv_color = cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)  # แปลงเป็นระบบสี HSV
        print('BGR:', bgr_color)
        print('HSV:', hsv_color)

image = cv2.imread('example.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_color)

while True:
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
