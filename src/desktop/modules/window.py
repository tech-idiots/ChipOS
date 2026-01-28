import pygame
import configparser
pygame.font.init()
font = pygame.font.Font('src/fonts/Pix32.ttf', 16)
config = configparser.ConfigParser()
config.read('src/home/config/main.ini')

class window():
    """Makes a window in a desktop of ChipOS"""
    def __init__(self, x, y, width, height, title="New Window"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.color = (200, 200, 200)

        self.window = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.toolbar = pygame.Rect((self.x, self.y), (self.width, int(config['size']['taskbar'])))
        
        # Render the text surface
        self.title_text = font.render(self.title, True, (0, 0, 0))
        
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect(topleft=(x, y))
        return 

    def draw(self, screen):
        # Draw window background
        pygame.draw.rect(screen, (128, 128, 128), self.window)
        
        # Draw toolbar
        pygame.draw.rect(screen, (100, 100, 100), self.toolbar)
        
        # Draw the title text on the toolbar
        # Position it with some padding from the left edge of the toolbar
        text_x = self.x + 55
        text_y = self.y + (int(config['size']['taskbar']) - self.title_text.get_height()) // 2
        screen.blit(self.title_text, (text_x, text_y))