import pygame
from PIL import Image
import os
import sys
import random


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
    #Start_window()
ALL_TIMER = 90
HEALTH = 40
COUNT_LEVEL = 3
THINGS = []
TIMER = 0


def for_final_window():
    if ALL_TIMER > 500 or HEALTH == 0 or COUNT_LEVEL == 3:
        open_window = Final_window()
        return True
    return False


def for_second_level(screen):
    open_level = Second_level()


def terminate():
    pygame.quit()
    sys.exit()


def update_all_timer():
    ALL_TIMER += 1


def update_timer():
    TIMER += 1


def write_some(screen, coordinates, style, sizi, texty, color):
    font = pygame.font.SysFont(style, sizi)
    text = font.render(texty, True, pygame.Color(color))
    screen.blit(text, coordinates)


def final():
    screen = new_window(500, 500)
    if 'h2o' in THINGS and 'hclo4' in THINGS and 'fe' in THINGS:
        COUNT_LEVEL += 1
        write_some(screen, (5, 10), 'Bradley Hand ITC', 10, f'You have collected the right ingredients and prepared the right medicine that cured you of a dog bite', '#92000a')
        write_some(screen, (50, 70), 'Bradley Hand ITC', 30, f'You complete this level', '#92000a')
        write_some(screen, (0, 140), 'Bradley Hand ITC', 30, '-------------------------------------------',
                   '#92000a')
        directory = [[(50, 170), 'Bradley Hand ITC', 35, f'Time =          {ALL_TIMER}'],
                     [(50, 220), 'Bradley Hand ITC', 35, f'Levels            {COUNT_LEVEL}'],
                     [(50, 270), 'Bradley Hand ITC', 35, f'Health =       {HEALTH}'],
                     [(50, 320), 'Bradley Hand ITC', 35, f'Things          {THINGS}']]
        for i in range(4):
            write_some(screen, directory[i][0], directory[i][1], directory[i][2], directory[i][3],
                       '#92000a')  # parameters
    else:
        write_some(screen, (10, 70), 'Bradley Hand ITC', 10, f'You did not collect the necessary components and died from a dog bite', '#92000a')
        HEALTH = 0
        for_final_window()


def something(number_of_level): # preface to the beginning of the level
    screen = new_window(500, 500)
    with open(f'{number_of_level}.txt') as f:
        for i in f:
            write_some(screen, (10, 70), 'Bradley Hand ITC', 10, i, '#92000a')


class Second_level:
    def __init__(self):
        image_now = ''
        book_list = 1
        screen = new_window(500, 500)
        something(2)
        clock.tick(8000)
        images = ['im21.jpg', 'im22.jpg', '23.jpg', '24.jpg']
        name_images = 0
        image = load_image(images[name_images % 4])
        image = pygame.transform.scale(image, (500, 500))
        arrow = pygame.sprite.Sprite(all_sprites)
        arrow.image = image
        arrow.rect = arrow.image.get_rect()
        running = True
        while running:
            #if TIMER > 1000000000:
            #    running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 267 < x < 302 and 102 < y < 152 and images[name_images % 4] == '24.jpg':
                        image = load_image('book0.jpg')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        image_now = 'book0.jpg'
                    if 63 < x < 456 and 79 < y < 429 and image_now == 'book0.jpg':
                        image = load_image(f'book{book_list % 8}.jpg')
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                        if 250 < x < 500:
                            book_list += 1
                        else:
                            book_list -= 1
                    if 90 < x < 191 and 139 < y < 220 and images[name_images % 4] == 'im21.jpg':
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
                    else:
                        print(1)
                        screen.fill(pygame.Color(0, 0, 0))
                        final()
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        name_images += 1
                        image = load_image(images[name_images % 4])
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
                    elif event.key == pygame.K_d:
                        name_images -= 1
                        image = load_image(images[name_images % 4])
                        image = pygame.transform.scale(image, (500, 500))
                        arrow = pygame.sprite.Sprite(all_sprites)
                        arrow.image = image
                        arrow.rect = arrow.image.get_rect()
            screen.fill(pygame.Color(0, 0, 0))
            all_sprites.draw(screen)
            pygame.display.flip()
            #update_timer()



class Final_window:
    def __init__(self):
        screen = new_window(400, 400)
        directory = []
        if ALL_TIMER > 500:
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
                     [(50, 320), 'Bradley Hand ITC', 35, f'Things          {len(THINGS)}']]
        for i in range(4):
            write_some(screen, directory[i][0], directory[i][1], directory[i][2], directory[i][3],
                       '#92000a')  # parameters


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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                something(2)
                clock.tick(100000)
                for_second_level(new_window(500, 500))
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

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    pygame.quit()
