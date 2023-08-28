import cv2
import numpy as np
# 讀入圖像與像素大小
def pixelate(image, block_size):
    # 取得皮案的高度與寬度
    height, width = image.shape[:2]
    # 將原始高度與寬度除以想要的像素大小
    small_height = height // block_size
    small_width = width // block_size
    # 使用resize將圖片像素合併，差值使用線性差值計算
    temp = cv2.resize(image, (small_width, small_height), interpolation=cv2.INTER_LINEAR)
    # 將縮小後的圖片放大回原本大小
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    # 回傳圖片
    return output
# 讀取圖像
image = cv2.imread('傻逼.jpg')
# 設定每隔相像素大小
block_size = 20
# 將圖像轉為像素風格儲存於pixelated_image變數
pixelated_image = pixelate(image, block_size)
# 顯示原始圖像與像素風格圖像
cv2.imshow('Original Image', image)
cv2.imshow('Pixelated Image', pixelated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()#關閉所有窗口
