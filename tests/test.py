import sys
import os
import unittest
from unittest.mock import patch, Mock
import pygame
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game import Game  # Import the Game class

class GameTestCase(unittest.TestCase):

    @patch('pygame.display.set_mode')
    @patch('pygame.image.load')
    @patch('pygame.mixer.music.load')
    @patch('pygame.mixer.music.play')
    def setUp(self, mock_play, mock_music_load, mock_image_load, mock_set_mode):
        # Mock images to prevent file loading issues
        mock_image = Mock()
        mock_image.get_width.return_value = 32
        mock_image.get_height.return_value = 32
        mock_image_load.return_value = mock_image

        # Create an instance of the game
        self.game = Game()

    def test_initial_score(self):
        # Test that the initial score is zero
        self.assertEqual(self.game.score, 0)

    def test_initial_level(self):
        # Test that the initial level is 1
        self.assertEqual(self.game.level, 1)

    def test_player_initial_position(self):
        # Test the player's initial position
        self.assertEqual(self.game.player_x, self.game.width // 2)
        self.assertEqual(self.game.player_y, self.game.height - 50)

    def test_spawn_garbage(self):
        # Test spawning garbage items
        garbage_positions = self.game.spawn_garbage(10)
        self.assertEqual(len(garbage_positions), 10)
        for pos in garbage_positions:
            self.assertTrue(0 <= pos[0] <= self.game.width - 32)
            self.assertTrue(-600 <= pos[1] <= -32)

    def test_level_up(self):
        # Increase the score to trigger a level-up
        self.game.score = 20
        self.game.level_up()
        
        # Check that the level increased, score reset, and time limit is updated
        self.assertEqual(self.game.level, 2)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.time_limit, 30)
        self.assertEqual(self.game.player_speed, 7)

if __name__ == '__main__':
    unittest.main()

