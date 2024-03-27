import cv2
import numpy as np

# เปิดกล้อง
cap = cv2.VideoCapture(0)

# ตรวจสอบว่ากล้องถูกเปิดหรือไม่
if not cap.isOpened():
    print("ไม่สามารถเปิดกล้องได้")
    exit()

# วนลูปอ่านภาพจากกล้อง
while True:
    # อ่านภาพจากกล้อง
    ret, frame = cap.read()

    # ตรวจสอบว่าอ่านภาพได้สำเร็จหรือไม่
    if not ret:
        print("ไม่สามารถอ่านภาพจากกล้องได้")
        break

   # แปลงรูปเป็นระบบสี HSV
    hsv_cap = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

    # กำหนดช่วงของสีน้ำเงินในระบบสี HSV
    lower_blue = np.array([90, 100, 100])  # ค่าสีน้ำเงินต่ำสุด (Hue, Saturation, Value)
    upper_blue = np.array([130, 255, 255])  # ค่าสีน้ำเงินสูงสุด (Hue, Saturation, Value)

    # สร้าง binary mask เพื่อแสดงส่วนของภาพที่มีสีน้ำเงินอยู่ในช่วงที่กำหนด
    mask = cv2.inRange(hsv_cap, lower_blue, upper_blue) 

    # ค้นหาเส้นขอบ
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # วาดกรอบรอบวัตถุที่พบ
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # แสดงภาพต้นฉบับและมาส์ค
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)

    # รอการกดปุ่ม 'q' เพื่อออกจากการแสดงภาพ
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดกล้องเมื่อเสร็จสิ้น
cap.release()
cv2.destroyAllWindows()