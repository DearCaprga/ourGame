import pygame
import pygame.freetype
from PIL import Image
import random
import os
import datetime

all_sprites = pygame.sprite.Group()


def new_window(width, height):
    pygame.init()
    size = width, height = width, height
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    return screen


def write_some(scren, coordinates, style, sizi, texty, color):
    font = pygame.font.SysFont(style, sizi)
    text = font.render(texty, True, color)
    scren.blit(text, coordinates)
    pygame.display.flip()


def load_image(name, colorkey=None, size=(10, 10), turn=0):
    img = Image.open(os.path.join('data', name))
    img.thumbnail(size=size)
    img = img.rotate(turn)
    img.save('picture.png')
    fullname = os.path.join('picture.png')
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    pygame.display.flip()
    return image


class Sprites(pygame.sprite.Sprite):
    def __init__(self, *group, screen, colorkey=None, name_file, xy, turn=0, size=(50, 50)):
        super().__init__(*group)
        image = load_image(os.path.join(name_file), turn=turn, size=size, colorkey=colorkey)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = xy[0], xy[1]
        all_sprites.draw(screen)
        pygame.display.flip()


def perface():
    screen = new_window(300, 300)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # perface()
                return

    # self.location0()

perface()
pygame.quit()
