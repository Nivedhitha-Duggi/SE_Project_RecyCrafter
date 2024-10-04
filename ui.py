class GameUI:
    def _init_(self, screen):
        self.screen = screen

    def render(self, game):
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render(f"Items Collected: {game.items_collected}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))
