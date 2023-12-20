import os
import sys

import pygame

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    # if not os.path.isfile(fullname):
    #     print(f"Файл с изображением '{fullname}' не найден")
    #     sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Sprites(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        image = load_image(os.path.join('boom.png'))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 70

    # def update(self, *args):
    #     self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
    #     if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
    #         self.image = Sprites.image_boom

all_sprites = pygame.sprite.Group()

# for i in range(20):
#     # нам уже не нужно даже имя объекта!
#     Sprites(all_sprites)

running = True
while running:
    clock.tick(30)
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
