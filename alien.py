import pygame, random
from pygame.sprite import Sprite, Group
from bullet import Bullet

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Inititialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.health = 100  

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/spacecraft.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

        # Add a bullets group for alien bullets
        self.bullets = Group()

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def draw_health_bar(self):
        bar_width = 100
        bar_height = 50

        # Draw the background (full) health bar in green
        pygame.draw.rect(self.screen, (0, 255, 0), [self.rect.x, self.rect.y - 10, bar_width, bar_height])
        
        # Calculate the width of the health portion based on the current health percentage
        health_width = (self.health / 100) * bar_width

        # Draw the actual health portion in red
        pygame.draw.rect(self.screen, (255, 0, 0), [self.rect.x, self.rect.y - 10, health_width, bar_height])