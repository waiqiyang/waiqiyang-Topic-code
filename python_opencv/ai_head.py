import cv2

# 加載人臉識別模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 讀取圖像
image = cv2.imread('image1.jpg')

# 轉換為灰度圖像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 在圖片中檢測人臉
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

# 在檢測到的人臉周圍繪製邊匡
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 顯示繪製了人臉的圖像
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
