import pygame
from PIL import Image
import os
import sys
import random


all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()


def new_window(width, height):
    pygame.init()
    size = width, height = width, height
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    return screen


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
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
    def __init__(self, *group, colorkey=None, name_file, xy, turn=0, size=(50, 50)):
        super().__init__(*group)
        image = load_image(os.path.join(name_file), turn=turn, size=size, colorkey=colorkey)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = xy[0], xy[1]
        all_sprites.draw(screen)
        pygame.display.flip()


def restart():
    screen.fill(pygame.Color(0, 0, 0))
    #Start_window()
    ALL_TIMER = 0
    HEALTH = 100
    COUNT_LEVEL = 0
    THINGS = 0


def for_final_window(screen):
    if ALL_TIMER > 30 or HEALTH == 0 or COUNT_LEVEL == 3:
        open_window = Final_window(screen)
        return True
    return False


def for_second_level(screen):
    open_level = Second_level()


def terminate():
    pygame.quit()
    sys.exit()


def write_some(screen, coordinates, style, sizi, texty, color):
    font = pygame.font.SysFont(style, sizi)
    text = font.render(texty, True, pygame.Color(color))
    screen.blit(text, coordinates)


class Second_level:
    def __init__(self):
        screen = new_window(500, 500)
        images = ['im21.jpg', 'im22.jpg', '23.jpg', '24.jpg']
        name_images = 0
        image = load_image(images[name_images % 4])
        image = pygame.transform.scale(image, (500, 500))
        arrow = pygame.sprite.Sprite(all_sprites)
        arrow.image = image
        arrow.rect = arrow.image.get_rect()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 10 < x > 100 and 120 < y < 300:
                        image = load_image('im_lek.jpg')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        screen.fill(pygame.Color(0, 0, 0))
                        write_some(screen, (10, 100), 'Bradley Hand ITC', 50, f'Выберете 3 бутылки', '#92000a')
                        clock.tick(10)
                        image = load_image('im_lek.jpg')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        screen.fill(pygame.Color(0, 0, 0))
                elif event.type == pygame.KEYDOWN or event.type == pygame.K_a:
                    name_images += 1
                    image = load_image(images[name_images % 4])
                    image = pygame.transform.scale(image, (500, 500))
                    arrow = pygame.sprite.Sprite(all_sprites)
                    arrow.image = image
                    arrow.rect = arrow.image.get_rect()
                elif event.type == pygame.KEYDOWN or event.type == pygame.K_s:
                    image = load_image(images[name_images % 4])
                    image = pygame.transform.scale(image, (500, 500))
                    arrow = pygame.sprite.Sprite(all_sprites)
                    arrow.image = image
                    arrow.rect = arrow.image.get_rect()
                elif event.type == pygame.KEYDOWN or event.type == pygame.K_d:
                    name_images -= 1
                    image = load_image(images[name_images % 4])
                    arrow = pygame.sprite.Sprite(all_sprites)
                    arrow.image = image
                    arrow.rect = arrow.image.get_rect()

            screen.fill(pygame.Color(0, 0, 0))
            all_sprites.draw(screen)
            pygame.display.flip()


class Final_window:
    def __init__(self, screen):
        directory = []
        if ALL_TIMER > 30:
            directory = [[(90, 10), 'Chiller', 50, 'You fall'],
                         [(30, 60), 'Bradley Hand ITC', 'You thought to long...'],
                         [(30, 100), 'Bradley Hand ITC', 30, 'So you were killed']]
        elif HEALTH == 0:
            directory = [[(90, 10), 'Chiller', 50, 'You fall'],
                         [(30, 60), 'Bradley Hand ITC', 30, 'Your health is...'],
                         [(170, 100), 'Bradley Hand ITC', 30, 'Too small']]
        elif COUNT_LEVEL == 3:
            directory = [[(150, 30), 'Chiller', 45, 'You win'],
                         [(50, 90), 'Bradley Hand ITC', 28, 'You finished this game'],
                         [(90, 120), 'Bradley Hand ITC', 28, 'You are lucky']]
        for i in range(3):
            write_some(screen, directory[i][0], directory[i][1], directory[i][2], directory[i][3], '#92000a')
        write_some(screen, (0, 140), 'Bradley Hand ITC', 30, '-------------------------------------------', '#92000a')
        directory = [[(50, 170), 'Bradley Hand ITC', 35, f'Time =          {ALL_TIMER}'],
                     [(50, 220), 'Bradley Hand ITC', 35, f'Levels            {COUNT_LEVEL}'],
                     [(50, 270), 'Bradley Hand ITC', 35, f'Health =       {HEALTH}'],
                     [(50, 320), 'Bradley Hand ITC', 35, f'Things          {THINGS}']]
        for i in range(4):
            write_some(screen, directory[i][0], directory[i][1], directory[i][2], directory[i][3],
                       '#92000a')  # parameters


if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    #restart()

    for_second_level(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
