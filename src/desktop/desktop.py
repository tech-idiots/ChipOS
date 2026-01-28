import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import ast
import configparser
import time
from .modules import window

# Initialize Pygame
windows = [window_obj, window_es]
active_window = None
def main():
    pygame.init()
    config = configparser.ConfigParser()
    config.read('src/home/config/main.ini')
    
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    bg_str = config['colors']['background']
    bg_tuple = ast.literal_eval(bg_str)
    mouse_size = config['size']['mouse_size']
    mouse_img_surface = pygame.image.load('src/images/icons/mouse.png').convert_alpha()
    mouse_img_surface = pygame.transform.scale(mouse_img_surface, (int(mouse_size), int(mouse_size)))
    hotspot = (0, 0)
    custom_cursor = pygame.cursors.Cursor(hotspot, mouse_img_surface)

    pygame.mouse.set_cursor(custom_cursor)
    
    running = True
    dragging = False
    offset_x = 0
    offset_y = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for win in reversed(windows):  # topmost first
                    if win.toolbar.collidepoint(event.pos):
                        active_window = win
                        dragging = True
                        offset_x = event.pos[0] - win.x
                        offset_y = event.pos[1] - win.y
                        windows.remove(win)
                        windows.append(win)  # bring to front
            

            
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    window_obj.x = event.pos[0] - offset_x
                    window_obj.y = event.pos[1] - offset_y
                    # Update rects
                    window_obj.window.topleft = (window_obj.x, window_obj.y)
                    window_obj.toolbar.topleft = (window_obj.x, window_obj.y)
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LSHIFT] and keys[pygame.K_F10]:
            running = False
        
        screen.fill(bg_tuple)
        window_obj.draw(screen)
        window_es.draw(screen)
        pygame.display.flip()

    pygame.quit()