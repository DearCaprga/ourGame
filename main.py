import pygame
import pygame.freetype
from PIL import Image
import random
import os
import datetime

# import pygame_menu as pm
# import sys
# from srpiteClass import *
all_sprites = pygame.sprite.Group()
ST_mus, SCREAM_hard, PASSING_speed = 0, 0, 0
clock = pygame.time.Clock()
with open('setings.txt', 'w', encoding='utf-8') as file:
    file.write('000')


def new_window(width, height):
    pygame.init()
    size = width, height
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
        clock.tick(1000)


class Settings:  # in txt will be settings
    def __init__(self, screen):
        Sprites(all_sprites, screen=screen, name_file='seting.jpg', xy=(535, 0), size=(70, 70))
        self.screen = screen

    def settings_view(self):
        screen_set = new_window(600, 400)
        line = []
        write_some(self.screen, (10, 10), 'Bradley Hand ITC', 25, 'back', 'blue')
        write_some(screen_set, (180, 20), 'Bradley Hand ITC', 50, 'Settings', '#92000a')
        for i in range(3):
            write_some(screen_set, (80, 120 + i * 70), 'Bradley Hand ITC', 40,
                       ['Music', 'Scream', 'Speed'][i], '#92000a')  # 120 190 260
            write_some(screen_set, (300, 120 + i * 70), 'Bradley Hand ITC', 40,
                       ['off / on', 'low / high', 'light / hard'][i], '#92000a')

        running = True
        while running:
            file1, line = self.file_open()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 300 <= x <= 420 and 120 <= y <= 160:
                        if x <= 350:
                            file1.write('0' + str(line[1]) + str(line[2]))
                        elif x >= 380:
                            file1.write('1' + str(line[1]) + str(line[2]))
                        file1.close()
                        file, line = self.file_open()
                        self.play_music(line[0])
                    elif 300 <= x <= 470 and 190 <= y <= 230:
                        if x <= 355:
                            file1.write(str(line[0]) + '0' + str(line[2]))
                        elif x >= 390:
                            file1.write(str(line[0]) + '1' + str(line[2]))

                        file1, line = self.file_open()
                        file1.close()

                    elif 300 <= x <= 500 and 260 <= y <= 300:
                        if x <= 380:
                            file1.write(str(line[0]) + str(line[1]) + '0')
                        elif x >= 420:
                            file1.write(str(line[0]) + str(line[1]) + '1')

                        file1, line = self.file_open()
                        file1.close()
                    elif 10 <= x <= 50 and 10 <= y <= 35:  # back to the start window
                        screen_set.fill(pygame.Color("black"))
                        self.screen.fill(pygame.Color("black"))
                        Start_window()

    def file_open(self):
        file1 = open('setings.txt', 'r+')
        line = [int(i) for i in file1.read()]
        file1.seek(0)
        self.draw_line(line[0], 350, 420, 380, 165)
        self.draw_line(line[1], 355, 460, 390, 235)
        pygame.display.flip()
        self.draw_line(line[2], 380, 490, 420, 305)
        return file1, line

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
        pygame.draw.line(self.screen, color1, (x1, y), (300, y), 1)
        pygame.draw.line(self.screen, color2, (x2, y), (x3, y), 1)
        pygame.display.flip()


class Start_window:
    def __init__(self):
        screen = new_window(600, 400)
        # arrow = make_cursor(screen)
        pygame.font.init()
        running = True
        pygame.draw.rect(screen, '#92000a', pygame.Rect(210, 190, 160, 90), 2, 20)
        [write_some(screen, [(130, 40), (230, 190)][i], 'Chiller', 90 - 20 * i, ['Original name', 'Start!'][i],
                    '#92000a') for i in range(2)]

        Settings(screen)
        Sprites(all_sprites, screen=screen, name_file="startovi.jpg", xy=(-40, 150), turn=25, size=(250, 250))
        Sprites(all_sprites, screen=screen, name_file="ladon.jpg", xy=(400, 300), turn=-45, size=(200, 200))

        sec_start = datetime.datetime.now().second
        flag_drop = True

        while running:
            pygame.display.flip()

            if datetime.datetime.now().second == sec_start + 5 and flag_drop:
                flag_drop = False
                for i in range(random.randrange(2, 3)):
                    turn = random.randrange(1, 70, 5)
                    size = random.randrange(50, 150, 10)
                    coord = random.choice([(random.randrange(400, 520, 10), random.randrange(110, 250, 10)),
                                           (random.randrange(100, 350, 10), random.randrange(295, 320, 10))])
                    Sprites(all_sprites, screen=screen, name_file='blood.jpg', xy=coord, turn=turn, size=(size, size))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    if x >= 535 and y <= 70:  # clicked on settings

                        Settings(screen).settings_view()
                        # ST_mus, SCREAM_hard, PASSING_speed = Settings(screen).settings_view(ST_mus, SCREAM_hard,
                        #                                                                     PASSING_speed)
                        # st_mus, screem_hard, passing_speed = ST_mus, SCREAM_hard, PASSING_speed
                    elif 190 <= x <= 380 and 175 <= y <= 295:  # clicked on start
                        Locations().preface()
                # if event.type == pygame.MOUSEMOTION:
                #     arrow.topleft = event.pos
            # screen.fill(pygame.Color("black"))
            # clock.tick(100)
            # all_sprites.update()

            # Start_window()

            # if pygame.mouse.get_focused():
            #     all_sprites.draw(screen)
            #     pygame.display.flip()
            # screen.fill(pygame.Color("white"))


class Locations:
    def __init__(self):
        pass

    def location0(self):  # for insructins
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        print(start_time)

        screen0 = new_window(800, 600)
        fon = pygame.transform.scale(load_image('fon.jpg'), (800, 600))
        screen0.blit(fon, (0, 0))
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

        pygame.quit()

    def preface(self):  # there will be small preface. It will be with pictures
        screen = new_window(600, 600)
        fon = pygame.transform.scale(load_image('fon.jpg'), (600, 600))
        screen.blit(fon, (0, 0))
        running = True
        self.location0()

    def move_poin(self):  # provides 4-sided viewing
        pass

    def click_thing(self):  # bring the pressed item closer
        pass



if __name__ == '__main__':
    # screen = new_window(600, 400)
    #  Settings(screen).play_music(1)
    st_mus, screem_hard, passing_speed = 0, 0, 0
    Start_window()
    pygame.display.flip()
    # running = True

    #  def restart_game
    #
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             x, y = pygame.mouse.get_pos()
    #             print(x, y)
    #             if x >= 535 and y <= 70:  # clicked on settings
    #                 st_mus, screem_hard, passing_speed = Settings(screen).settings_view(st_mus, screem_hard,
    #                                                                                     passing_speed)
    #             elif 190 <= x <= 380 and 175 <= y <= 295:  # clicked on start
    #                 Locations().preface()
    # screen.fill(pygame.Color("white"))

    pygame.quit()
