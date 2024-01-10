import pygame
import pygame.freetype
from PIL import Image
import random
import os
import datetime
import sqlite3

# import pygame_menu as pm
# import sys
# from srpiteClass import *
all_sprites = pygame.sprite.Group()
LIST = ['start', 'loc0', 'loc1']
clock = pygame.time.Clock()
with open('setings.txt', 'w', encoding='utf-8') as file:
    file.write('000')


def new_window(width, height):
    pygame.init()
    size = width, height
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    return screen


def write_some(screen, coordinates, style, size, texty, color):
    font = pygame.font.SysFont(style, size)
    text = font.render(texty, True, color)
    screen.blit(text, coordinates)
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
    def __init__(self, screen, corner=535, winds='start'):
        Sprites(all_sprites, screen=screen, colorkey=-1, name_file='seting.jpg', xy=(corner, 0), size=(70, 70))
        self.screen = screen
        self.corner = corner
        self.winds = winds
        print(self.winds)

    def find_set(self, x, y, wind):
        if x >= self.corner and y <= 70:  # clicked on settings
            Settings(self.screen, winds=wind).settings_view()

    def settings_view(self):
        screen_set = new_window(600, 400)
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
                    elif 10 <= x <= 50 and 10 <= y <= 35:  # back to the main window
                        screen_set.fill(pygame.Color("black"))
                        self.screen.fill(pygame.Color("black"))
                        windows(self.winds)
                        return


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
                    Settings(screen).find_set(x, y, 'start')
                    if 190 <= x <= 380 and 175 <= y <= 295:  # clicked on start
                        Locations().perface()
                        return


class Locations:  # write def to print text
    def __init__(self):
        pass

    def perface(self):
        flag5 = 1
        flag10 = 1
        screen = new_window(600, 400)
        sec_start = datetime.datetime.now().second

        write_some(screen, (200, 150), 'Bernard MT Condensed', 25, 'Как я тут оказался?', 'white')
        write_some(screen, (70, 177), 'Bernard MT Condensed', 25,
                   'Голова болит, кажется сильный ушиб, да еще и кровь…', 'white')

        running = True
        while running:
            if datetime.datetime.now().second == sec_start + 1 and flag5:
                screen.fill(pygame.Color("black"))
                text = 'Я точно помню, как мы решили пойти вместе в ту заброшку :' \
                       'про которую говорил весь город. Вроде когда-то тут жила :' \
                       'счастливая семья, но они неожиданно уехали. Никто так и :' \
                       'не знает истинной причины, но каждый старался придумать :' \
                       'свою легенду. '.split(':')
                for i in range(5):
                    write_some(screen, (40, 130 + 27 * i), 'Bernard MT Condensed', 25, text[i], 'white')
                flag5 = 0
            # this comm in ban because of future def 👀
            # I think it will be more correct to use 2 different 'if' because there are only 2 things
            if datetime.datetime.now().second == sec_start + 2 and flag10:
                screen.fill(pygame.Color('black'))
                text = 'Ничего… больше ничего не помню, почему я здесь:' \
                       'один, кто меня ударил и как отсюда выбраться?:' \
                       'Нельзя медлить, иначе будет хуже.'.split(':')
                for i in range(3):
                    write_some(screen, (80, 150 + 27 * i), 'Bernard MT Condensed', 25, text[i], 'white')
                flag10 = 0
            if datetime.datetime.now().second == sec_start + 3:
                self.location0()
                return

    def location0(self):  # for insructins
        clock = pygame.time.Clock()
        start_time = datetime.datetime.now()
        print(start_time)
        screen0 = new_window(800, 560)
        running = True
        Sprites(all_sprites, screen=screen0, name_file='wall0.png', xy=(0, 0), turn=0, size=(800, 600))
        Settings(screen0, 735, 'loc0')
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    Settings(screen0, 735, 'loc0').find_set(x, y, 'loc0')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                    elif event.key == pygame.K_DOWN:
                        pass
                    elif event.key == pygame.K_UP:
                        pass




# Don`t work return to the main window, because of def view_settings last lines.
# It`s necessary to look out mistake in list of def

        pygame.quit()

    def move_poin(self):  # provides 4-sided viewing
        pass

    def click_thing(self):  # bring the pressed item closer
        pass

    def location1(self):
        start_time = datetime.datetime.now()
        print(start_time)
        screen1 = new_window(800, 560)
        running = True
        Sprites(all_sprites, screen=screen1, name_file='wall0.png', xy=(0, 0), turn=0, size=(800, 600))
        Sprites(all_sprites, colorkey=-1, screen=screen1, name_file='book.png', xy=(690, 10), turn=0, size=(50, 50))


def windows(wind):
    if wind == 'start':
        Start_window()
        print(-1)
    elif wind == 'loc0':
        Locations().location0()
        print(0)
    elif wind == 'loc1':
        Locations().location1()
        print(1)


if __name__ == '__main__':
    Start_window()
    pygame.display.flip()
    pygame.quit()



