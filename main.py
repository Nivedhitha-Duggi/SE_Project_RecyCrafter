import pygame
from game_logic import Game
from ui import GameUI

# Initialize the game
pygame.init()

# Set up the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize game logic and UI
game = Game()
ui = GameUI(screen)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    game.update()

    # Render UI
    ui.render(game)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

pygame.quit()
