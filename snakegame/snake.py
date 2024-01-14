import pygame
import time
import random

pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake parameters
snake_block = 10
snake_speed = 15

# Initialize snake
snake_list = []
snake_length = 1

# Initialize snake position and movement
snake_head = [width // 2, height // 2]
snake_direction = 'RIGHT'
change_to = snake_direction

# Initialize food position
food_position = [random.randrange(1, (width // snake_block)) * snake_block,
                 random.randrange(1, (height // snake_block)) * snake_block]

# Initialize score
score = 0
font = pygame.font.SysFont(None, 35)

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

# Function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, [10, 10])

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_direction == 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and not snake_direction == 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and not snake_direction == 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and not snake_direction == 'LEFT':
                change_to = 'RIGHT'

    # Update snake direction
    if change_to == 'UP' and not snake_direction == 'DOWN':
        snake_direction = 'UP'
    elif change_to == 'DOWN' and not snake_direction == 'UP':
        snake_direction = 'DOWN'
    elif change_to == 'LEFT' and not snake_direction == 'RIGHT':
        snake_direction = 'LEFT'
    elif change_to == 'RIGHT' and not snake_direction == 'LEFT':
        snake_direction = 'RIGHT'

    # Move the snake
    if snake_direction == 'UP':
        snake_head[1] -= snake_block
    elif snake_direction == 'DOWN':
        snake_head[1] += snake_block
    elif snake_direction == 'LEFT':
        snake_head[0] -= snake_block
    elif snake_direction == 'RIGHT':
        snake_head[0] += snake_block

    # Check for collisions with walls
    if snake_head[0] >= width or snake_head[0] < 0 or snake_head[1] >= height or snake_head[1] < 0:
        game_over = True

    # Check for collisions with itself
    for segment in snake_list[1:]:
        if snake_head == segment:
            game_over = True

    # Update snake length
    snake_list.append(list(snake_head))
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Draw background
    screen.fill(black)

    # Draw food
    pygame.draw.rect(screen, red, [food_position[0], food_position[1], snake_block, snake_block])

    # Draw snake
    draw_snake(snake_block, snake_list)

    # Display score
    display_score(score)

    # Update display
    pygame.display.update()

    # Check for collisions with food
    if snake_head[0] == food_position[0] and snake_head[1] == food_position[1]:
        food_position = [random.randrange(1, (width // snake_block)) * snake_block,
                         random.randrange(1, (height // snake_block)) * snake_block]
        snake_length += 1
        score += 10

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
