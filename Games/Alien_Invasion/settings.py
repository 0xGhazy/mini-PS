import os
import json

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        os.chdir(os.path.dirname(__file__))
        self.content = ""
        with open("ai_configurations.json", 'r') as f:
            self.content = json.load(f)

        # Screen settings.
        self.screen_width = self.content['screen_width']
        self.screen_height = self.content['screen_height']
        self.bg_color = tuple(self.content['bg_color'])

        # Ship settings.
        self.ship_limit = self.content['ship_limit']

        # Bullet settings.
        self.bullet_width = self.content['bullet_width']
        self.bullet_height = self.content['bullet_height']
        self.bullet_color = tuple(self.content['bullet_color'])
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = self.content['fleet_drop_speed']

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3

        # Scoring.
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
