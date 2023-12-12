import pygame

ALL_TIMER = 40
HEALTH = 100
COUNT_LEVEL = 0


def for_final_window(screen):
    if ALL_TIMER > 30 or HEALTH == 0 or COUNT_LEVEL == 3:
        open_window = Final_window(screen)
        return True
    return False


def all_part_draw(screen, number, name_mistake):
    screen.fill(pygame.Color(0, 0, 0))
    if number == 1:
        colour = '#65000b'
        name_text = 'You fall'
    else:
        colour = '#00ff00'
        name_text = 'You win'
    font = pygame.font.Font(None, 50)
    text_1 = font.render(name_text, True, pygame.Color(colour))
    text_2 = font.render(name_mistake, True, pygame.Color('#a366ff'))
    screen.blit(text_1, (200, 30))
    screen.blit(text_2, (10, 100))


class Final_window:
    def __init__(self, screen):
        if ALL_TIMER > 30:
            all_part_draw(screen, 1, 'You think to long, so you are killed')  # were
        elif HEALTH == 0:
            all_part_draw(screen, 1, 'Your health is too small')  # was
        elif COUNT_LEVEL == 3:
            all_part_draw(screen, 0, 'You finished this game')


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    for_final_window(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
