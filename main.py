import pygame
import pygame.freetype
from PIL import Image


def settings_draw():
    img = Image.open("seting.jpg")
    img.thumbnail(size=(70, 70))
    img.save('picture.jpg')
    car_surf = pygame.image.load("picture.jpg")
    screen.blit(car_surf, (535, 0))


def settings_view():
    size = width, height = 500, 500
    screen_set = pygame.display.set_mode(size)
    screen_set.fill(pygame.Color(0, 5, 0))
    font_set = pygame.font.SysFont('Chiller', 50)
    text = font_set.render('Settings', True, '#92000a')
    screen_set.blit(text, (130, 50))
    # running1 = True
    # while running1:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running1 = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             x, y = pygame.mouse.get_pos()


class Start_window:
    def __init__(self):
        pygame.font.init()
        font = pygame.font.SysFont('Bradley Hand ITC', 50)
        text = font.render('Original name', True, '#92000a')
        screen.blit(text, (130, 50))
        settings_draw()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 600
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
                    settings_view()

    pygame.quit()
