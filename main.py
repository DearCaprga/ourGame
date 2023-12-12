import pygame
import pygame.freetype
from PIL import Image
import pygame_menu as pm


def write_some(scren, coordinates, style, sizi, texty, color):
    font = pygame.font.SysFont(style, sizi)
    text = font.render(texty, True, color)
    scren.blit(text, coordinates)


class Settings:
    def __init__(self):
        img = Image.open("seting.jpg")
        img.thumbnail(size=(70, 70))
        img.save('picture.jpg')
        car_surf = pygame.image.load("picture.jpg")
        screen.blit(car_surf, (535, 0))

    def settings_view(self):
        size = width, height = 600, 400
        pygame.font.init()
        screen_set = pygame.display.set_mode(size)
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
                    print(x, y)
                    if 300 <= x <= 420 and 120 <= y <= 160:
                        if x <= 350:
                            #write_some(screen_set, (80, 120), 'Bradley Hand ITC', 40, 'off / on', 'blue')
                            st_mus = 0
                            print(1)
                        elif x >= 380:
                            st_mus = 1
                        self.play_music(st_mus)
                        print('music')
                    elif 300 <= x <= 470 and 190 <= y <= 230:
                        screem_hard = (0, 1)
                        print('screem')
                    elif 300 <= x <= 500 and 260 <= y <= 300:
                        passing_speed = (0, 1)
                        print('speed')
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
                    '#92000a')
         for i in range(2)]
        Settings()


def location0():
    pass


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    Start_window()
    mytheme = pm.themes.THEME_DARK.copy()
    mytheme.background_color = (0, 0, 0)

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
                    location0()
    pygame.quit()
