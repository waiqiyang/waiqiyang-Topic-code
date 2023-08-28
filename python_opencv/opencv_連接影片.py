import cv2

# 讀取第一個影片
video1 = cv2.VideoCapture('1.MP4')

# 讀取第二個影片
video2 = cv2.VideoCapture('2.MP4')

# 檢查文件是否符合格式
if not video1.isOpened() or not video2.isOpened():
    print("影片格式不符")
    exit()

fps = video1.get(cv2.CAP_PROP_FPS)
width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 創建一個新的影片文件儲存製作出來的影片
# 格式為mp4
# 輸出為output.mp4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# 逐幀讀取並寫入第一個影片
while True:
    ret, frame = video1.read()
    if not ret:
        break

    output.write(frame)

# 逐幀讀取並寫入第二個影片
while True:
    ret, frame = video2.read()
    if not ret:
        break

    output.write(frame)

# 輸出並關閉資源
video1.release()
video2.release()
output.release()
