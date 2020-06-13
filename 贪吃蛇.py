import pygame
import random
import copy

# 颜色常量
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Snake():
    def __init__(self):
        self.gameScrSize = (526, 526)  # 游戏窗口大小
        self.blockSize = 20  # 像素块大小
        self.MYWIDOWS = pygame.display.set_mode(self.gameScrSize)
        self.score = 0
        pygame.display.set_caption('贪吃蛇 分数：' + str(self.score))
        self.food = []
        self.where = 'stop'
        self.snakeList = [[16, 13], [15, 13], [14, 13], [13, 13], [12, 13], [11, 13], [10, 13]]  # 初始化蛇列表
        self.draw_snake()
        self.rand_food()
        self.draw_food()


    # 将游戏窗口分成 25 * 25 块像素块
    def draw_snake(self):
        num = 0
        for snake in self.snakeList:
            for i in range(1, 26):
                if snake[0] == i:
                    for j in range(1, 26):
                        if snake[1] == j:
                            color = WHITE
                            if num == 0:
                                color = RED
                                num += 1
                            pygame.draw.rect(self.MYWIDOWS, color, (
                            1 + (snake[0] - 1) * (self.blockSize + 1), 1 + (snake[1] - 1) * (self.blockSize + 1), self.blockSize,
                            self.blockSize))
    
    
    def move(self):
        if self.snakeList[0] in self.snakeList[1:]:
            self.where = 'stop'
            print('撞到自己了')
        if self.where == 'stop':
            pass
        if self.where == 'right':
            tempList = copy.deepcopy(self.snakeList)
            newSnakeList = []
            if tempList[0][0] > 24:
                tempList[0][0] = 0
            tempList[0][0] += 1
            newSnakeList.append(tempList[0])
            for i in range(len(self.snakeList)):
                if i != len(self.snakeList) - 1:
                    newSnakeList.append(self.snakeList[i])
            self.snakeList = newSnakeList
            pygame.draw.rect(self.MYWIDOWS, BLACK, (0, 0, 526, 526))
            self.draw_snake()
            self.draw_food()
        if self.where == 'left':
            tempList = copy.deepcopy(self.snakeList)
            newSnakeList = []
            if tempList[0][0] < 2:
                tempList[0][0] = 26
            tempList[0][0] -= 1
            newSnakeList.append(tempList[0])
            for i in range(len(self.snakeList)):
                if i != len(self.snakeList) - 1:
                    newSnakeList.append(self.snakeList[i])
            self.snakeList = newSnakeList
            pygame.draw.rect(self.MYWIDOWS, BLACK, (0, 0, 526, 526))
            self.draw_snake()
            self.draw_food()
        if self.where == 'up':
            tempList = copy.deepcopy(self.snakeList)
            newSnakeList = []
            if tempList[0][1] < 2:
                tempList[0][1] = 26
            tempList[0][1] -= 1
            newSnakeList.append(tempList[0])
            for i in range(len(self.snakeList)):
                if i != len(self.snakeList)-1:
                    newSnakeList.append(self.snakeList[i])
            self.snakeList = newSnakeList
            pygame.draw.rect(self.MYWIDOWS, BLACK, (0, 0, 526, 526))
            self.draw_snake()
            self.draw_food()
        if self.where == 'down':
            tempList = copy.deepcopy(self.snakeList)
            newSnakeList = []
            if tempList[0][1] > 24:
                tempList[0][1] = 0
            tempList[0][1] += 1
            newSnakeList.append(tempList[0])
            for i in range(len(self.snakeList)):
                if i != len(self.snakeList)-1:
                    newSnakeList.append(self.snakeList[i])
            self.snakeList = newSnakeList
            pygame.draw.rect(self.MYWIDOWS, BLACK, (0, 0, 526, 526))
            self.draw_snake()
            self.draw_food()
    
    def ctrl_snake(self, where):
        self.where = where


    def rand_food(self):
        areaList = [[i, j] for i in range(1, 26) for j in range(1, 26)]
        self.food = random.choice(areaList)
        is_snakeBody = True
        while is_snakeBody:
            if self.food in self.snakeList:
                self.food = random.choice(areaList)
            else:
                is_snakeBody = False
        # return food
    
    def draw_food(self):
        pygame.draw.rect(self.MYWIDOWS, BLUE, (
            1 + (self.food[0] - 1) * (self.blockSize + 1), 1 + (self.food[1] - 1) * (self.blockSize + 1), self.blockSize,
            self.blockSize))


    def eat(self):
        if self.snakeList[0] == self.food:
            self.score += 1
            newEnd = copy.deepcopy(self.snakeList[-1])
            if self.snakeList[-1][0] == self.snakeList[-2][0]:
                if self.snakeList[-1][1] > self.snakeList[-2][1]:
                    newEnd[1] += 1
                    self.snakeList.append(newEnd)
                else:
                    newEnd[1] -= 1
                    self.snakeList.append(newEnd)
            if self.snakeList[-1][1] == self.snakeList[-2][1]:
                if self.snakeList[-1][0] > self.snakeList[-2][0]:
                    newEnd[0] += 1
                    self.snakeList.append(newEnd)
                else:
                    newEnd[0] -= 1
                    self.snakeList.append(newEnd)
            self.rand_food()


if __name__ == '__main__':
    pygame.init()
    snake = Snake()
    while True:
        pygame.time.Clock().tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.where != 'down':
                    snake.ctrl_snake('up')
                if event.key == pygame.K_DOWN and snake.where != 'up':
                    snake.ctrl_snake('down')
                if event.key == pygame.K_LEFT and snake.where != 'right' and snake.where != 'stop':
                    snake.ctrl_snake('left')
                if event.key == pygame.K_RIGHT and snake.where != 'left':
                    snake.ctrl_snake('right')
                if event.key == pygame.K_SPACE:
                    snake.ctrl_snake('stop')
        snake.move()
        snake.eat()
        pygame.display.set_caption('贪吃蛇 分数：' + str(snake.score))
        pygame.display.flip()


