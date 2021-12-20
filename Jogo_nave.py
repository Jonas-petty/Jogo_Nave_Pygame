import pygame
from sys import exit
from random import randint

# Initialize the Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('sprites/ufo.png').convert_alpha()
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('sprites/spaceship.png').convert_alpha()
player_rect = player_img.get_rect(center=(400, 500))

# Enemy
enemy_img = pygame.image.load('sprites/enemy.png').convert_alpha()
enemy_rect = enemy_img.get_rect(center=(randint(50, 750), randint(50, 200)))
enemy_x_direction = 5
enemy_y_direction = 4

# aim_img = pygame.image.load('sprites/aim.png').convert_alpha()


clock = pygame.time.Clock()

# Game Loop
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     mouse_pos = pygame.mouse.get_pos()
        #     print(mouse_pos)
    if pygame.key.get_pressed()[pygame.K_a] and player_rect.left >= 0:
        player_rect.x -= 10
    if pygame.key.get_pressed()[pygame.K_d] and player_rect.right <= 800:
        player_rect.x += 10

    screen.blit(player_img, player_rect)

    enemy_rect.x += enemy_x_direction
    if enemy_rect.left <= 0:
        enemy_direction = 3
        enemy_rect.y += enemy_y_direction
    elif enemy_rect.right >= 800:
        enemy_direction = -3
        enemy_rect.y += enemy_y_direction

    screen.blit(enemy_img, enemy_rect)
    # aim_rect = aim_img.get_rect(center=mouse_pos)
    # screen.blit(aim_img, aim_rect)
    # circle = pygame.draw.circle(screen, (255, 0, 0), mouse_pos, 5)
    pygame.display.flip()
