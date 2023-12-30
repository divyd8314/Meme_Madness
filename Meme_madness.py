import pygame 

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8) #80 percent of height 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meme Royale Madness")

x = 200
y = 200
scale = 3
img = pygame.image.load("images/char.png")
img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
rect = img.get_rect()
rect.center = (x, y)

# Game loop
run = True #executes the game 
while run:

  screen.blit(img, rect) #display image 

  # Handle events
  for event in pygame.event.get():
      #Quits the game
      if event.type == pygame.QUIT:
          run = False
  pygame.display.update()

pygame.quit()