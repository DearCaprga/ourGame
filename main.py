import pygame
import pygame.freetype
from PIL import Image
import random
import os
# import pygame_menu as pm
# import sys
# from srpiteClass import *
all_sprites = pygame.sprite.Group()
ST_mus = 0
SCREAM_hard = 0
PASSING_speed = 0


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


def load_image(name, colorkey=None, size=(10, 10), turn=0):
    img = Image.open(os.path.join('data', name))
    img.thumbnail(size=size)
    img = img.rotate(turn)
    img.save('picture.jpg')
    fullname = os.path.join('picture.jpg')
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


class Settings:
    def __init__(self, screen):  # надо сделать так, чтобы когда заново открываются настройки были те же параметры
        Sprites(all_sprites, name_file='seting.jpg', xy=(535, 0), size=(70, 70))  # наверно надо что-то вернуть
        self.st_mus = ST_mus
        self.screem_hard = SCREAM_hard
        self.passing_speed = PASSING_speed

    def settings_view(self):
        screen_set = new_window(600, 400)
        self.enter(screen_set)
        write_some(screen_set, (180, 20), 'Bradley Hand ITC', 50, 'Settings', '#92000a')
        for i in range(3):
            write_some(screen_set, (80, 120 + i * 70), 'Bradley Hand ITC', 40,
                       ['Music', 'Scream', 'Speed'][i], '#92000a')  # 120 190 260
            write_some(screen_set, (300, 120 + i * 70), 'Bradley Hand ITC', 40,
                       ['off / on', 'low / high', 'light / hard'][i], '#92000a')

        self.draw_line(self.st_mus, 350, 420, 380, 165)
        self.draw_line(self.screem_hard, 355, 460, 390, 235)
        self.draw_line(self.passing_speed, 380, 490, 420, 305)
        pygame.display.flip()
        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 300 <= x <= 420 and 120 <= y <= 160:
                        if x <= 350:
                            self.st_mus = 0
                        elif x >= 380:
                            self.st_mus = 1
                        self.draw_line(self.st_mus, 350, 420, 380, 165)
                        self.play_music(self.st_mus)
                    elif 300 <= x <= 470 and 190 <= y <= 230:
                        if x <= 355:
                            self.screem_hard = 0
                        elif x >= 390:
                            self.screem_hard = 1
                        self.draw_line(self.screem_hard, 355, 460, 390, 235)
                    elif 300 <= x <= 500 and 260 <= y <= 300:
                        if x <= 380:
                            self.passing_speed = 0
                        elif x >= 420:
                            self.passing_speed = 1
                        self.draw_line(self.passing_speed, 380, 490, 420, 305)
                    elif 10 <= x <= 50 and 10 <= y <= 35:  # back to the start window
                        screen_set.fill(pygame.Color("black"))
                        screen.fill(pygame.Color("black"))
                        Start_window()
                        return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass

    def play_music(self, state):
        if state:
            pygame.mixer.music.load('background music.mp3')
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.pause()

    def draw_line(self, state, x1, x2, x3, y):
        color1 = 'black'
        color2 = '#92000a'
        if not state:
            color1, color2 = color2, color1
        pygame.draw.line(screen, color1, (x1, y), (300, y), 1)
        pygame.draw.line(screen, color2, (x2, y), (x3, y), 1)
        pygame.display.flip()

    def enter(self, screen):
        write_some(screen, (10, 10), 'Bradley Hand ITC', 25, 'back', 'blue')


class Start_window:
    def __init__(self):
        pygame.font.init()
        pygame.draw.rect(screen, '#92000a', pygame.Rect(210, 190, 160, 90), 2, 20)
        [write_some(screen, [(130, 40), (230, 190)][i], 'Chiller', 90 - 20 * i, ['Original name', 'Start!'][i],
                    '#92000a') for i in range(2)]

        Settings(screen)
        Sprites(all_sprites, name_file="startovi.jpg", xy=(-40, 150), turn=25, size=(250, 250))
        Sprites(all_sprites, name_file="ladon.jpg", xy=(400, 300), turn=-45, size=(200, 200))
        pygame.time.wait(2000)
        # clock = pygame.time.Clock()  # do that depends on real time? not on wait
        # start_time = pygame.time.get_ticks()
        for i in range(random.randrange(2, 4)):
            turn = random.randrange(1, 70, 5)
            k = random.randrange(50, 150, 10)
            size = (k, k)
            coord = random.choice([(random.randrange(400, 520, 10), random.randrange(110, 250, 10)),
                                   (random.randrange(100, 350, 10), random.randrange(295, 320, 10))])
            Sprites(all_sprites, name_file='blood.jpg', xy=coord, turn=turn, size=size)


class Locations:
    def __init__(self):
        pass

    def location0(self):  # for insructins
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        print(start_time)

        screen0 = new_window(800, 600)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

        pygame.quit()

    def preface(self):  # there will be small preface. It will be with pictures
        self.location0()

    def move_poin(self):  # provides 4-sided viewing
        pass

    def click_thing(self):  # bring the pressed item closer
        pass


# def make_cursor(screen):
#     clock = pygame.time.Clock()
#     all_sprites = pygame.sprite.Group()
#
#     image = load_image("cursor.png")
#     arrow = pygame.sprite.Sprite(all_sprites)
#     arrow.image = image
#     arrow.rect = arrow.image.get_rect()
#     pygame.mouse.set_visible(False)
#
#     running = True
#     while running:
#         clock.tick(30)
#         all_sprites.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEMOTION:
#                 arrow.rect.topleft = event.pos
#         if pygame.mouse.get_focused():
#             all_sprites.draw(screen)
#
#         pygame.display.flip()


if __name__ == '__main__':
    screen = new_window(600, 400)
    #  Settings(screen).play_music(1)
    Start_window()
    pygame.display.flip()
    # make_cursor(screen)
    running = True

    #  def restart_game

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if x >= 535 and y <= 70:  # clicked on settings
                    Settings(screen).settings_view()
                elif 190 <= x <= 380 and 175 <= y <= 295:  # clicked on start
                    Locations().preface()
        # screen.fill(pygame.Color("white"))

    pygame.quit()
