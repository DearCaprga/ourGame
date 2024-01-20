import pygame
from PIL import Image
import os
import sys
from random import randint
import datetime
from datetime import datetime


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()


def new_window(width, height):
    pygame.init()
    size = width, height = width, height
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    return screen


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
    # Start_window()


FIRST_TIME = datetime.now()

ALL_TIMER = 0
COUNT_LEVEL = 1
HEALTH = 100
HARD = 0
THINGS = []
TIMER = 0
TIME_OF_LEVEL = 0


def terminate():
    pygame.quit()
    sys.exit()


def write_some(screenni, coordinates, style, sizi, texty, color):
    font = pygame.font.SysFont(style, sizi)
    text = font.render(texty, True, pygame.Color(color))
    screenni.blit(text, coordinates)





def final():
    global COUNT_LEVEL, HEALTH, ALL_TIMER, THINGS
    sceeen = new_window(500, 500)
    if 'h2o' in THINGS and 'hclo4' in THINGS and 'fe' in THINGS:
        COUNT_LEVEL += 1
        if ALL_TIMER > 60:
            HEALTH //= ALL_TIMER // 60
        directory = [[(30, 50), 'Bradley Hand ITC', 25, 'You have collected the right ingredients', '#92000a'],
                     [(40, 100), 'Bradley Hand ITC', 30, 'and prepared the right medicine', '#92000a'],
                     [(40, 150), 'Bradley Hand ITC', 30,
                      ' that cured you of a dog bite',
                      '#92000a'],
                     [(100, 200), 'Bradley Hand ITC', 30, f'You complete this level', '#92000a'],
                     [(0, 250), 'Bradley Hand ITC', 30, '------------------------------------------------------',
                      '#92000a'],
                     [(50, 270), 'Bradley Hand ITC', 35, f'Time =          {ALL_TIMER}'],
                     [(50, 320), 'Bradley Hand ITC', 35, f'Levels            {COUNT_LEVEL}'],
                     [(50, 370), 'Bradley Hand ITC', 35, f'Health =       {HEALTH}'],
                     [(50, 420), 'Bradley Hand ITC', 35, f'Things         {len(THINGS)}']]
        for i in range(9):
            write_some(sceeen, directory[i][0], directory[i][1], directory[i][2], directory[i][3],
                       '#92000a')  # parameters
    else:
        write_some(sceeen, (15, 110), 'Bradley Hand ITC', 30,
                   'You did not collect the necessary', '#92000a')
        write_some(sceeen, (15, 150), 'Bradley Hand ITC', 30,
                   'components and died from a dog bite', '#92000a')
        HEALTH = 0
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                sceeen.fill(pygame.Color(0, 0, 0))
                open_window = Final_window()


screen = new_window(500, 500)


class Mountain(pygame.sprite.Sprite):
    image = load_image("стол.png", -1)
    image = pygame.transform.scale(image, (500, 100))

    def __init__(self):
        super().__init__(com_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 500


class Landing(pygame.sprite.Sprite):
    image = load_image("im_camen.jpg", -1)
    image = pygame.transform.scale(image, (100, 100))

    def __init__(self, pos):
        super().__init__(com_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


com_sprites = pygame.sprite.Group()
mountain = Mountain()


def something(number_of_level):  # preface to the beginning of the level
    screenn = new_window(500, 500)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if event.key == pygame.K_DOWN:
                        Landing((randint(0, 500), randint(0, 300)))
                if event.key == pygame.K_RIGHT:
                    screenn.fill(pygame.Color(0, 0, 0))
                    running = False
                    open_level = Second_level()

        screen.fill(pygame.Color("black"))
        with open(f'{number_of_level}.txt', 'rt', encoding='utf-8') as f:
            y = 50
            for i in f:
                write_some(screenn, (50, y), 'Bradley Hand ITC', 30, i.rstrip(), '#92000a')
                y += 40
        pygame.display.flip()
        com_sprites.draw(screen)
        com_sprites.update()
        pygame.display.flip()
        clock.tick(50)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Second_level:
    def __init__(self):
        global TIMER, ALL_TIMER, TIME_OF_LEVEL
        TIME_OF_LEVEL = datetime.now()
        print(TIME_OF_LEVEL, FIRST_TIME)
        image_now = 'im21.jpg'
        book_list = 0
        screen = new_window(500, 500)
        images = ['im21.jpg', 'im22.jpg', '23.jpg', '24.jpg']
        name_images = 0
        image = load_image(images[name_images % 4])
        image = pygame.transform.scale(image, (500, 500))
        arrow = pygame.sprite.Sprite(all_sprites)
        arrow.image = image
        arrow.rect = arrow.image.get_rect()
        running = True
        while running:
            # pygame.draw.rect(screen, pygame.Color('red'), pygame.Rect(400, 0, 500, 50))
            # pygame.display.flip()
            time = str(datetime.now() - TIME_OF_LEVEL).split(':')
            TIMER = int(time[0][-2:]) * 360 + int(time[1]) * 60 + int(time[-1][:2])
            time_all = str(datetime.now() - FIRST_TIME).split(':')
            ALL_TIMER = int(time_all[0][-2:]) * 360 + int(time_all[1]) * 60 + int(time_all[-1][:2])
            print(ALL_TIMER)
            # write_some(screen, (410, 20), None, 20, f'{TIMER}', 'black')
            if TIMER >= 180 + 120 * HARD or ALL_TIMER >= 780 + 120 * HARD or len(THINGS) == 4:
                # если HARD = 1 то 5 мин, если 0, то 3 мин
                # если HARD = 1 то 15 мин, если 0, то 13 мин
                arrow.kill()
                print(TIMER)
                running = False
                screen.fill(pygame.Color(0, 0, 0))
                final()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 96 < x < 194 and 32 < y < 105 and image_now == 'im21.jpg':
                        arrow.kill()
                        image = load_image('image_stol.jpg')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        image_now = 'image_stol.jpg'
                    if 237 < x < 277 and 113 < y < 172 and image_now == 'im21.jpg':
                        arrow.kill()
                        image = load_image('24.jpg')
                        image = pygame.transform.scale(image, (470, 470))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        image_now = '24.jpg'
                    if 154 < x < 180 and 172 < y < 202 and image_now == '24.jpg':
                        arrow.kill()
                        image = load_image('imbook.PNG')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        image_now = 'imbook.PNG'
                    if 267 < x < 302 and 102 < y < 152 and image_now == '24.jpg':
                        arrow.kill()
                        image = load_image('book0.jpg')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        image_now = 'book0.jpg'
                    if 63 < x < 456 and 79 < y < 429 and image_now == 'book0.jpg':
                        arrow.kill()
                        image = load_image(f'book{book_list % 8}.jpg')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        if 250 < x < 500:
                            book_list += 1
                        else:
                            book_list -= 1
                    if 90 < x < 191 and 139 < y < 220 and image_now == 'im21.jpg':
                        arrow.kill()
                        image = load_image('im_lek1.jpg')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        image_now = 'im_lek1.jpg'
                    if len(THINGS) < 4:
                        if 118 < x < 138 and 62 < y < 134 and image_now == 'im_lek1.jpg':
                            THINGS.append('h2o')
                        if 118 < x < 138 and 62 < y < 134 and image_now == 'im_lek1.jpg':
                            THINGS.append('fe')
                        if 352 < x < 395 and 29 < y < 160 and image_now == 'im_lek1.jpg':
                            THINGS.append('hclo4')
                        if 180 < x < 196 and 107 < y < 137 and image_now == 'im_lek1.jpg':
                            THINGS.append('cu')
                        if 207 < x < 224 and 80 < y < 142 and image_now == 'im_lek1.jpg':
                            THINGS.append('zn')
                        if 229 < x < 245 and 123 < y < 145 and image_now == 'im_lek1.jpg':
                            THINGS.append('be')
                        if 49 < x < 90 and 309 < y < 385 and image_now == 'im_lek1.jpg':
                            THINGS.append('кровь человеческая')
                        if 94 < x < 111 and 425 < y < 460 and image_now == 'im_lek1.jpg':
                            THINGS.append('cl')
                        if 29 < x < 57 and 377 < y < 461 and image_now == 'im_lek1.jpg':
                            THINGS.append('cm')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        arrow.kill()
                        image_now = images[name_images % 4]
                        image = load_image(images[name_images % 4])
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                    if event.key == pygame.K_LEFT:
                        arrow.kill()
                        name_images += 1
                        image = load_image(images[name_images % 4])
                        image_now = images[name_images % 4]
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                    elif event.key == pygame.K_RIGHT:
                        arrow.kill()
                        name_images -= 1
                        image_now = images[name_images % 4]
                        image = load_image(images[name_images % 4])
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
            screen.fill(pygame.Color(0, 0, 0))
            all_sprites.draw(screen)
            pygame.display.flip()


class Final_window:
    def __init__(self):
        global TIMER, ALL_TIMER
        screen = new_window(400, 400)
        directory = []
        if TIMER >= 180 + 120 * HARD or ALL_TIMER >= 780 + 120 * HARD:
            directory = [[(150, 10), 'Chiller', 50, 'You fall'],
                         [(30, 60), 'Bradley Hand ITC', 30, 'You thought to long...'],
                         [(30, 100), 'Bradley Hand ITC', 30, 'So you were killed']]
        elif HEALTH == 0:
            directory = [[(150, 10), 'Chiller', 50, 'You fall'],
                         [(30, 60), 'Bradley Hand ITC', 30, 'Your health is...'],
                         [(170, 100), 'Bradley Hand ITC', 30, 'Too small']]
        elif COUNT_LEVEL == 2:
            directory = [[(150, 30), 'Chiller', 45, 'You win'],
                         [(50, 90), 'Bradley Hand ITC', 28, 'You finished this game'],
                         [(90, 120), 'Bradley Hand ITC', 28, 'You are lucky']]
        for i in range(3):
            write_some(screen, directory[i][0], directory[i][1], directory[i][2], directory[i][3], '#92000a')
        write_some(screen, (0, 140), 'Bradley Hand ITC', 30, '-------------------------------------------', '#92000a')
        directory = [[(50, 170), 'Bradley Hand ITC', 35, f'Time =          {ALL_TIMER}'],
                     [(50, 220), 'Bradley Hand ITC', 35, f'Levels            {COUNT_LEVEL}'],
                     [(50, 270), 'Bradley Hand ITC', 35, f'Health =       {HEALTH}'],
                     [(50, 320), 'Bradley Hand ITC', 35, f'Things          {len(THINGS)}']]
        for i in range(4):
            write_some(screen, directory[i][0], directory[i][1], directory[i][2], directory[i][3],
                       '#92000a')  # parameters
        pygame.display.flip()


def animation(width_pic, height_pic, fps, name_pic, position=(0, 0)):
    all_shot = width_pic * height_pic
    timer = pygame.time.Clock()
    frames = []
    screen = pygame.display.set_mode((500, 500))
    image = pygame.image.load(name_pic)
    width, height = image.get_size()
    w_each, h_each = width / width_pic, height / height_pic
    shot = 0
    for j in range(int(height / h_each)):
        for i in range(int(width / w_each)):
            frames.append(image.subsurface(pygame.Rect(w_each * i, shot, w_each, h_each)))
        shot += int(h_each)
    number = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 0))
                running = False
                something(2)


        screen.fill((0, 0, 0))
        number += 1
        number %= all_shot
        screen.blit(frames[number], position)

        pygame.display.update()
        timer.tick(fps)


animation(17, 1, 50, "image_anima.jpg", (0, 0))

if __name__ == '__main__':
    pygame.init()
    running = True

    while running:
        # restart()
        # for_final_window()
        # something(2)
        final()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    pygame.quit()
