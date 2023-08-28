import cv2
import os

# 設定目標目錄
target_directory = '/Users/waiqiyang/Desktop/專題'

# 檢查目錄是否具有寫入權限
if not os.access(target_directory, os.W_OK):
    print("no")
else:
    # 開啟影片檔案
    video = cv2.VideoCapture('慘冬大背頭.mp4')
    # 迴圈遍歷每一幀
    frame_count = 0
    while True:
        # 讀取一幀
        ret, frame = video.read()
        # 檢查是否成功讀取幀
        if not ret:
            break
        # 設定圖片檔案名稱
        image_name = os.path.join(target_directory, '/Users/waiqiyang/Desktop/專題/frame_{}.jpg'.format(frame_count))

        # 儲存圖片
        cv2.imwrite(image_name, frame)
        frame_count += 1
    # 釋放影片物件
    video.release()
    
