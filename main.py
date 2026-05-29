import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

player_x = 350
player_y = 500

speed = 5

running = True

while running:

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed

    if keys[pygame.K_RIGHT]:
        player_x += speed

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 50, 50))

    pygame.display.update()

pygame.quit()
