import pygame
import pygame.freetype
from PIL import Image
import pygame_menu as pm
import random


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


def draw_picture(name, size, turn, coor, screen):
    img = Image.open(name)
    img.thumbnail(size=size)
    img = img.rotate(turn)
    img.save('picture.jpg')
    surf = pygame.image.load("picture.jpg")
    screen.blit(surf, coor)


class Settings:
    def __init__(self, screen):
        draw_picture('seting.jpg', (70, 70), 0, (535, 0), screen)

    def settings_view(self):
        screen_set = new_window(600, 400)

        write_some(screen_set, (180, 20), 'Bradley Hand ITC', 50, 'Settings', '#92000a')
        for i in range(3):
            write_some(screen_set, (80, 120 + i * 70), 'Bradley Hand ITC', 40,
                       ['Music', 'Scream', 'Speed'][i], '#92000a')  # 120 190 260
            write_some(screen_set, (300, 120 + i * 70), 'Bradley Hand ITC', 40,
                       ['off / on', 'low / high', 'light / hard'][i], '#92000a')
        pygame.display.flip()
        st_mus = 1
        screem_hard = 0
        passing_speed = 0
        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 300 <= x <= 420 and 120 <= y <= 160:
                        if x <= 350:
                            st_mus = 0
                        elif x >= 380:
                            st_mus = 1
                        self.draw_line(st_mus, 350, 420, 380, 165)
                        self.play_music(st_mus)
                    elif 300 <= x <= 470 and 190 <= y <= 230:
                        if x <= 355:
                            screem_hard = 0
                        elif x >= 390:
                            screem_hard = 1
                        self.draw_line(screem_hard, 355, 460, 390, 235)
                    elif 300 <= x <= 500 and 260 <= y <= 300:
                        if x <= 380:
                            passing_speed = 0
                        elif x >= 420:
                            passing_speed = 1
                        self.draw_line(passing_speed, 380, 490, 420, 305)
                if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()

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


class Start_window:
    def __init__(self):
        pygame.font.init()
        pygame.draw.rect(screen, '#92000a', pygame.Rect(210, 190, 160, 90), 2, 20)
        [write_some(screen, [(130, 40), (230, 190)][i], 'Chiller', 90 - 20 * i, ['Original name', 'Start!'][i],
                    '#92000a') for i in range(2)]
        Settings(screen)
        draw_picture("startovi.jpg", (250, 250), 25, (-40, 150), screen)
        draw_picture('ladon.jpg', (200, 200), -45, (400, 300), screen)
        pygame.display.flip()
        pygame.time.wait(5000)
        for i in range(random.randrange(2, 5)):
            turn = random.randrange(1, 90, 1)
            k = random.randrange(100, 150, 1)
            sizee = (k, k)
            coord = (random.randrange(400, 599, 1), random.randrange(110, 399, 1))
            draw_picture('ladon.jpg', sizee, turn, coord, screen)


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


if __name__ == '__main__':
    screen = new_window(600, 400)
    #  Settings(screen).play_music(1)
    Start_window()
    pygame.display.flip()
    running = True

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
    pygame.quit()
