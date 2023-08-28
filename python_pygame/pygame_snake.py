import pygame
import random
# 初始化遊戲
pygame.init()
# 創建視窗大小
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('貪吃蛇')
# 創建顏色
window_background = (255, 255, 255)
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)
# 創建蛇物件及蘋果物件
snake_pos = [window_width/2, window_height/2]# 蛇蛇
snake_body = [[window_width/2, window_height/2]]# 蛇蛇的身體
food_pos = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]#隨機生成的蘋果
food_spawn = True
# 蛇的移動方向
snake_direction = 'UP'  # 初始方向為向上
# 遊戲變數
snake_speed = 15 # 遊戲幀數
score = 0 # 得分
# 遊戲時間變數
clock = pygame.time.Clock()
# 執行遊戲的主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# 當結束鍵被按下，跳出迴圈
            running = False
        # 偵測案件被按下
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            if event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
    # 根據蛇的移動方向更新位置
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    snake_body.insert(0, list(snake_pos))#將頭的位置添加到身體
    # 檢查頭是否與蘋果重疊
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        # 如果重疊，分數加一，蘋果狀態改為fales
        score += 1
        food_spawn = False
    else:# 如果沒重疊，刪除最後一個身體
        snake_body.pop()
    # 如果食物狀態不是True，隨機生成蘋果在地圖上
    if not food_spawn:
        food_pos = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]
    food_spawn = True
     # 控制蛇超出視窗範圍時結束遊戲
    if snake_pos[0] >= window_width or snake_pos[0] < 0 or snake_pos[1] >= window_height or snake_pos[1] < 0:
        running = False  # 蛇撞到視窗邊界，結束遊戲
    # 檢查蛇是否撞到自己的身體
    for segment in snake_body[1:]:
        if snake_pos[0] == segment[0] and snake_pos[1] == segment[1]:
            running = False  # 蛇撞到自己的身體，結束遊戲
    # 繪製在畫面上
    window.fill(window_background)
    for pos in snake_body:
        pygame.draw.rect(window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, apple_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    # 更新遊戲畫面
    pygame.display.update()
    #控制FPS
    clock.tick(snake_speed)
pygame.quit()# 關閉遊戲

