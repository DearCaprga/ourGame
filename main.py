import pygame
import pygame.freetype
from PIL import Image
import pygame_menu as pm


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
        font = pygame.font.SysFont('Bradley Hand ITC', 50)
        text = font.render('Settings', True, '#92000a')
        screen_set.blit(text, (200, 20))
        pygame.display.flip()
        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()

    def play_music(self, state):
        if state:
            pygame.mixer.music.load('background music.mp3')
            pygame.mixer.music.play(-1)


class Start_window:
    def __init__(self):
        pygame.font.init()
        font = pygame.font.SysFont('Chiller', 70)
        text = font.render('Original name', True, '#92000a')
        screen.blit(text, (150, 40))
        pygame.draw.rect(screen, '#92000a', pygame.Rect(190, 175, 190, 120), 2, 20)
        text = font.render('Start!', True, '#92000a')
        screen.blit(text, (230, 190))
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
                elif x >= 190 and y >= 175:  # clicked on start
                    location0()
    pygame.quit()
