import pygame
import os
import random
import time

class Game:
    def __init__(self):
        print("Current working directory:", os.getcwd())  # For debugging path issues

        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("ReCy-Crafter")

        # Load images
        self.background_image = pygame.image.load(os.path.join('assets/image/background.png'))
        self.player_image = pygame.image.load(os.path.join('assets/image/player.png'))
        self.bottle_image = pygame.image.load(os.path.join('assets/image/bottle.png'))
        self.paper_image = pygame.image.load(os.path.join('assets/image/paper.png'))

        # Scale down the player and bottle images
        self.player_image = pygame.transform.scale(self.player_image, (32, 32))  # Resize player to 32x32 pixels
        self.bottle_image = pygame.transform.scale(self.bottle_image, (32, 32))  # Resize bottle to 32x32 pixels

        # Initialize the mixer for sound
        pygame.mixer.init()

        # Load your background music
        pygame.mixer.music.load(os.path.join('assets/sound/Forest.mp3'))  # Replace with your music file
        pygame.mixer.music.play(-1)  # Loop the music



        # Player settings
        self.player_x = self.width // 2
        self.player_y = self.height - 50
        self.player_speed = 5

        # Game objects
        self.garbage_items = [self.bottle_image]
        self.garbage_positions = self.spawn_garbage(20)  # Start with 20 bottles

        # Score and level settings
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.level = 1
        self.time_limit = 60  # 60 seconds for the first level
        self.start_time = time.time()

    def spawn_garbage(self, count):
        positions = []
        for _ in range(count):
            x = random.randint(0, self.width - 32)
            y = random.randint(-600, -32)  # Start above the screen
            positions.append((x, y))
        return positions

    def run(self):
        running = True
        while running:
            self.screen.blit(self.background_image, (0, 0))  # Draw background
            self.handle_events()
            self.update()
            self.draw()

            # Check for time limit
            if time.time() - self.start_time >= self.time_limit:
                self.show_result()  # Show pass or fail message
                running = False  # End the game or move to next level

            pygame.display.flip()
            pygame.time.Clock().tick(60)  # Frame rate

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_x += self.player_speed

        # Keep player within screen bounds
        self.player_x = max(0, min(self.player_x, self.width - 32))

        # Update garbage positions (falling effect)
        for i in range(len(self.garbage_positions)):
            x, y = self.garbage_positions[i]
            y += 3  # Speed of falling
            if y > self.height:  # Reset if it goes out of screen
                y = random.randint(-600, -32)  # Respawn above the screen
                x = random.randint(0, self.width - 32)
            self.garbage_positions[i] = (x, y)

        # Collision detection
        for pos in self.garbage_positions:
            if (pos[0] < self.player_x < pos[0] + 32) and (pos[1] < self.player_y < pos[1] + 32):
                self.garbage_positions.remove(pos)
                self.score += 1
                self.play_collection_sound()  # Call a method to play collection sound

                # Level up after reaching a score of 20
                if self.score >= 20:
                    self.level_up()

    def play_collection_sound(self):
        self.collection_sound.play()  # Play the collection sound

    def level_up(self):
        print("Level up!")
        self.level += 1
        self.score = 0  # Reset score for the next level
        self.start_time = time.time()  # Reset the timer
        
        # Reduce time limit and increase player speed for the next level
        if self.level == 2:
            self.time_limit = 30  # 30 seconds for the second level
            self.player_speed = 7  # Increase player speed
            # Change background for the new level
            self.background_image = pygame.image.load(os.path.join('assets/image/water_management_background.png'))  # Update this path

        # Spawn new garbage items or change their behavior here if desired
        self.garbage_positions = self.spawn_garbage(20)  # Reset garbage positions with 20 bottles

    def show_result(self):
        # Create a surface for the result message
        result_surface = pygame.Surface((self.width, self.height))
        result_surface.set_alpha(128)  # Set transparency
        result_surface.fill((0, 0, 0))  # Black overlay

        # Render pass/fail message
        if self.score >= 20:
            result_text = "You Passed the Level!"
        else:
            result_text = "You Failed the Level!"

        text_surface = self.font.render(result_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))

        # Display the result
        self.screen.blit(result_surface, (0, 0))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(3000)  # Show the message for 3 seconds

    def draw(self):
        # Draw player
        self.screen.blit(self.player_image, (self.player_x, self.player_y))

        # Draw garbage (falling bottles)
        for pos in self.garbage_positions:
            self.screen.blit(self.bottle_image, pos)

        # Draw score and level
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        level_text = self.font.render(f'Level: {self.level}', True, (255, 255, 255))

        # Calculate remaining time
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, int(self.time_limit - elapsed_time))
        timer_text = self.font.render(f'Time: {remaining_time}', True, (255, 0, 0))

        # Display score, level, and timer
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))
        self.screen.blit(timer_text, (10, 90))

# Entry point
def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
