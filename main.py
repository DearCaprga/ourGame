import pygame
import pygame.freetype
from PIL import Image
import pygame_menu as pm


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


def draw_picture(name, size, turn, coor):
    img = Image.open(name)
    img.thumbnail(size=size)
    img = img.rotate(turn)
    img.save('picture.jpg')
    surf = pygame.image.load("picture.jpg")
    screen.blit(surf, coor)


class Settings:
    def __init__(self):
        draw_picture('seting.jpg', (70, 70), 0, (535, 0))

    def settings_view(self):
        screen_set = new_window(600, 400)

        write_some(screen_set, (180, 20), 'Bradley Hand ITC', 50, 'Settings', '#92000a')
        for i in range(3):
            write_some(screen_set, (80, 120 + i * 70), 'Bradley Hand ITC', 40,
                       ['Music', 'Scream', 'Speed'][i], '#92000a')  # 120 190 260
            write_some(screen_set, (300, 120 + i * 70), 'Bradley Hand ITC', 40,
                       ['off / on', 'low / high', 'light / hard'][i], '#92000a')
        pygame.display.flip()

        running1 = True
        st_mus = 0
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 300 <= x <= 420 and 120 <= y <= 160:
                        if x <= 350:
                            pygame.draw.line(screen, "#92000a", (350, 165), (300, 165), 1)
                            pygame.draw.line(screen, 'black', (420, 165), (380, 165), 1)
                            pygame.display.flip()
                            st_mus = 0
                        elif x >= 380:
                            st_mus = 1
                            pygame.draw.line(screen, "#92000a", (420, 165), (380, 165), 1)
                            pygame.draw.line(screen, 'black', (350, 165), (300, 165), 1)
                            pygame.display.flip()
                        self.play_music(st_mus)
                        print('music')
                    elif 300 <= x <= 470 and 190 <= y <= 230:
                        print('screem')
                        if x <= 355:
                            pygame.draw.line(screen, "#92000a", (355, 235), (300, 235), 1)
                            pygame.draw.line(screen, 'black', (460, 235), (390, 235), 1)
                            pygame.display.flip()
                            screem_hard = 0
                        elif x >= 390:
                            screem_hard = 1
                            pygame.draw.line(screen, "#92000a", (460, 235), (390, 235), 1)
                            pygame.draw.line(screen, 'black', (390, 235), (300, 235), 1)
                            pygame.display.flip()
                    elif 300 <= x <= 500 and 260 <= y <= 300:
                        print('speed')
                        if x <= 380:
                            pygame.draw.line(screen, "#92000a", (380, 305), (300, 305), 1)
                            pygame.draw.line(screen, 'black', (490, 305), (390, 305), 1)
                            pygame.display.flip()
                            passing_speed = 0
                        elif x >= 420:
                            passing_speed = 1
                            pygame.draw.line(screen, "#92000a", (490, 305), (420, 305), 1)
                            pygame.draw.line(screen, 'black', (390, 305), (300, 305), 1)
                            pygame.display.flip()
                if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()

    def play_music(self, state):
        if state:
            pygame.mixer.music.load('background music.mp3')
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.pause()


class Start_window:
    def __init__(self):
        pygame.font.init()
        pygame.draw.rect(screen, '#92000a', pygame.Rect(210, 190, 160, 90), 2, 20)
        [write_some(screen, [(130, 40), (230, 190)][i], 'Chiller', 90 - 20 * i, ['Original name', 'Start!'][i],
                    '#92000a') for i in range(2)]

        draw_picture("startovi.jpg", (250, 250), 25, (-40, 150))
        draw_picture('arm.jpg', (200, 200), -45, (400, 300))

        Settings()


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
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    Start_window()

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x >= 535 and y <= 70:  # clicked on settings
                    Settings().settings_view()
                elif 190 <= x <= 380 and 175 <= y <= 295:  # clicked on start
                    Locations().preface()
    pygame.quit()
