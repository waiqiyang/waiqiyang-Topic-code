import cv2
import mediapipe as mp
import time
# 讀取視訊鏡頭儲存在變數lens
lens = cv2.VideoCapture(0)
# 下載手部模型
mpHands = mp.solutions.hands
# 呼叫Hands函式設定判斷的參數(圖片或影片, 最多幾隻手, 模型複雜度(越高越準但越耗能), 偵測嚴謹度(0到1，越高越準但越耗能), 追蹤嚴謹度(0到1，越高越準但越耗能))
hands = mpHands.Hands()
# 畫出所有節點
mpDraw = mp.solutions.drawing_utils
# 點的樣式變數(顏色=(R, G, B), 粗細)
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=3)
# 線的樣式變數(顏色=(R, G, B), 粗細)
handConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=5)
pTime = 0
cTime = 0

# 視訊判斷迴圈
while True:
    ret, img = lens.read()
    if ret:
        # 將圖片轉為RGB(opencv讀取為BGR)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 在圖片中比對手部，結果放入result中
        result = hands.process(imgRGB)
        # 視窗的高度變數(第0個值)
        imgHeight = img.shape[0]
        # 視窗的寬度變數(第1個值)
        imgWidth = img.shape[1]
        if result.multi_hand_landmarks:# 回傳所有手部節點座標， 如果未偵測到回傳None
            for handLms in result.multi_hand_landmarks:
                # 將每隻手的結果都跑一次
                # 用draw_landmarks函式畫出所有節點(繪製的圖片,繪製的節點, 在相連的節點上繪製線, 點的樣式, 線的樣式)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
                # 印出每個節點座標，跑過每一隻手的每個點
                for i, lm in enumerate(handLms.landmark):
                    # 將編筐比例座標轉為像素座標，轉為int去除小數點
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    # 將每個節點的編號寫在節點旁(繪製的圖片, 繪製的東西, 位置(X, Y), 字體, 大小, 文字顏色, 粗細)
                    cv2.putText(img, str(i), (xPos-25, yPos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
                    # 印出每個節點,X座標,Y座標
                    print(i, xPos, yPos)
        # 在畫面中繪製FPS
        # 現在時間
        cTime = time.time()
        # 現在時間檢調上次執行時間
        fps = 1/(cTime-pTime)
        # 記錄現在時間
        pTime = cTime
        # 將FPS寫在畫面中
        cv2.putText(img, f"FPS : {int(fps)}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        # 在畫面中顯示出
        cv2.imshow('img', img)
    # 當輸入為空白鍵時，跳出迴圈
    if cv2.waitKey(1) == ord(' '):
        break
