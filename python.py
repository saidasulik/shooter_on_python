# библиотека случайных чисел
import random
# pygame это библиотека для создания игр на питоне
import pygame
# sys это библиотека с функциями которые помогают выходить из игры
import sys

# Initialize PyGame
# это команда устанавливает все модули pygame для правильной работы
# эта команда всегда запускается 
pygame.init()

# Set up the game window
screen_width = 800 # переменная ширины экрана
screen_height = 600 #  переменая высоты экрана
# эта команда которая создаёт окно с задаными порамитрами ширины и высоты
screen = pygame.display.set_mode((screen_width, screen_height))
# эта команда создаёт название окна
pygame.display.set_caption("JUST A HARDCORE GAME")

# Set the frame rate
# эта команда контролирует кадры в игре
clock = pygame.time.Clock()

# Player settings
# ширина и высота персонажа
player_width = 50
player_height = 60
# позиция игрока
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
# скорость персонажа
player_speed = 5

# Bullet settings
# характиристики пули
bullet_width = 5
bullet_height = 10
bullet_speed = 9
bullets = [] # пустой список пуль

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemies = []

# Spawn an enemy every 2 seconds
enemy_timer = 0
enemy_spawn_time = 1000

# Collision detection function
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Main game loop
# это главный игровой цикл который продолжает работать и следит за обновлениями в игре и событиями типа выхода из игры
while True:
    # этот цикл следит за выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # условия: при любом нажатии кнопки 
        if event.type == pygame.KEYDOWN:
            # условия: при любом нажатии кнопки
            if event.key == pygame.K_UP:
                # Create a bullet at the current player position
                # определяет начальную позицию пули
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                # добавление пули в список пуль
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))

# Update enemy positions and spawn new ones
# обновлять и спавнить врагов
    # current_time - текущее время, прошедшее время с начала игры
    current_time = pygame.time.get_ticks()
    # условие спавна врагов
    if current_time - enemy_timer > enemy_spawn_time:
        # рандомное определение позиции врага по x
        enemy_x = random.randint(0, screen_width - enemy_width)
        # позиция врага по y
        enemy_y = -enemy_height
        # создание и добавление врага в список врагов
        enemy_vrag = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        enemies.append(enemy_vrag)
        #(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
        enemy_timer = current_time

    for enemy in enemies:
        enemy.y += enemy_speed

        # Check for collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if check_collision(bullet, enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

        # Remove enemies that are off the screen
    enemies = [enemy for enemy in enemies if enemy.y < screen_height]


# Handle player movement
# условия нажатия кнопок и позиции игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
#        player_x = player_x - player_speed
    if keys[pygame.K_d] and player_x < screen_width - player_height:
        player_x += player_speed
    # if keys[pygame.K_s] and player_y < screen_width - player_height:
    #     player_y += player_speed
    # if keys[pygame.K_w] and player_y < screen_width - player_height:
    #     player_y -= player_speed

        # Update bullet positions
        # это цикл создающий движение пули
    for bullet in bullets:
        bullet.y -= bullet_speed

        # Remove bullets that are off the screen
        # сохрание пуль в списке если они не вышли за экран
    bullets = [bullet for bullet in bullets if bullet.y > 0]

    # Fill the screen with a color (black in this case)
    # эта функция отвечает за цвет
    screen.fill((0, 0, 0))

# Draw the player
# создание игрока и его характиристики,начальная позиция
    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

# Draw the bullets
# цикл прорисовки пули
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)

# Draw the enemies
# цикл прорисовки врага
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    # Update the display
    # эта команда обновляет экран и загружает объекты
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    # эта команда ограничевает кадры в секунду
    clock.tick(60)
    