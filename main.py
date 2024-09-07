import pygame
import random 
import sys

pygame.init()
screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()

class Snake: 
  def __init__(self): 
    self.x = 200
    self.y = 200
    self.x_point = 1
    self.y_point = 0
    self.head = pygame.Rect(self.x, self.y, 20,20)
    self.parts = [pygame.Rect(self.x - 20, self.y, 20,20)]
    self.is_alive = True

  def move(self): 
    for part in self.parts: 
      if self.head.x == part.x and self.head.y == part.y: 
        self.is_alive = False
      if self.head.x < 0 or self.head.x > 380 or self.head.y < 0 or self.head.y > 380: 
        self.is_alive = False

    self.parts.append(self.head)
    for i in range(len(self.parts) - 1): 
      self.parts[i].x = self.parts[i + 1].x
      self.parts[i].y = self.parts[i + 1].y
      
    self.head.x += self.x_point * 20
    self.head.y += self.y_point * 20
    self.parts.remove(self.head)

  

class Apple: 
  def __init__(self): 
    self.x = self.x = random.randrange(0,400,20,)
    self.y = self.y = random.randrange(0,400,20)
    self.apple_image = pygame.image.load('apple.png')
    self.apple_image = pygame.transform.scale(self.apple_image, (20, 20))
    self.rect = pygame.Rect(self.x, self.y, 20, 20)
   
  def draw_it(self): 
    screen.blit(self.apple_image, self.rect )


def make_the_board(): 
  board = pygame.image.load('board.png')
  screen.blit(board)


def reset(): 
  global score
  global apple
  snake.x = 0 
  snake.y = 0
  snake.x_point = 1
  snake.y_point = 0
  snake.head = pygame.Rect(snake.x, snake.y, 20,20)
  snake.parts = [pygame.Rect(snake.x - 20, snake.y, 20,20)]
  snake.is_alive = True
  apple = Apple()
  score = 0

make_the_board()
snake = Snake()
apple = Apple()

crunch = pygame.mixer.Sound('crunch.mp3')

test_font = pygame.font.Font(None, 40)
score = 0 
score_text = test_font.render(f'score: {score}', True, 'yellow')
score_rect = score_text.get_rect(center = (200,500))


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit()
      sys.exit()
      
    if snake.is_alive == True: 
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_UP and snake.y_point == 0: 
          snake.y_point = -1
          snake.x_point = 0
        elif event.key == pygame.K_DOWN and snake.y_point == 0: 
          snake.y_point = 1
          snake.x_point = 0
        elif event.key == pygame.K_RIGHT and snake.x_point == 0: 
          snake.x_point = 1
          snake.y_point = 0
        elif event.key == pygame.K_LEFT and snake.x_point == 0: 
          snake.x_point = -1
          snake.y_point = 0
      
  if snake.is_alive == True: 
    snake.move()
    
    screen.fill('black')
    make_the_board()
    apple.draw_it()

    score_text = test_font.render(f'score: {score}', True, 'yellow')
    screen.blit(score_text, score_rect)

    pygame.draw.rect(screen, 'blue', snake.head)
    for piece in snake.parts: 
      pygame.draw.rect(screen, 'blue', piece)


    if snake.head.x == apple.x and snake.head.y == apple.y: 
      crunch.play()
      score += 1
      snake.parts.append(pygame.Rect(piece.x, piece.y, 20,20))
      apple = Apple()

  if snake.is_alive == False: 
    screen.fill('green')
    message = test_font.render('space to play', True, 'black')
    message_rect = message.get_rect(center = (200,300))
    screen.blit(message,message_rect)
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]: 
      reset()
      
  pygame.display.update()
  clock.tick(8)
