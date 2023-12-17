import pygame

ALL_TIMER = 0
HEALTH = 100
COUNT_LEVEL = 3
THINGS = 0


def for_final_window(screen):
    if ALL_TIMER > 30 or HEALTH == 0 or COUNT_LEVEL == 3:
        open_window = Final_window(screen)
        return True
    return False


def write_some(screen, coordinates, style, sizi, texty, color):
    font = pygame.font.SysFont(style, sizi)
    text = font.render(texty, True, color)
    screen.blit(text, coordinates)


def all_part_draw(screen, number, name_mistake):
    screen.fill(pygame.Color(0, 0, 0))
    if number == 1:
        colour = '#65000b'
        name_text = 'You fall'
    else:
        colour = '#00ff00'
        name_text = 'You win'
    font = pygame.font.Font(None, 30)
    text_1 = font.render(name_text, True, pygame.Color(colour))
    text_2 = font.render(name_mistake, True, pygame.Color('#65000b'))
    screen.blit(text_1, (200, 30))
    screen.blit(text_2, (10, 100))


class Final_window:
    def __init__(self, screen):
        if ALL_TIMER > 30:
            write_some(screen, (90, 10), 'Chiller', 50, 'You fall', '#92000a')
            write_some(screen, (30, 60), 'Bradley Hand ITC', 30, 'You thought to long...', '#92000a')
            write_some(screen, (30, 100), 'Bradley Hand ITC', 30, 'So you were killed', '#92000a')
        elif HEALTH == 0:
            write_some(screen, (100, 10), 'Chiller', 50, 'You fall', '#92000a')
            write_some(screen, (30, 60), 'Bradley Hand ITC', 30, 'Your health is...', '#92000a')
            write_some(screen, (170, 100), 'Bradley Hand ITC', 30, 'Too small', '#92000a')
        elif COUNT_LEVEL == 3:
            write_some(screen, (100, 10), 'Chiller', 50, 'You win', '#92000a')
            write_some(screen, (15, 60), 'Bradley Hand ITC', 28, 'You finished this game', '#92000a')
            write_some(screen, (30, 100), 'Bradley Hand ITC', 30, 'You are lucky', '#92000a')
        write_some(screen, (0, 140), 'Bradley Hand ITC', 30, '-------------------------------------------', '#92000a')
        write_some(screen, (20, 170), 'Bradley Hand ITC', 30, f'Time = {ALL_TIMER}', '#92000a')
        write_some(screen, (20, 200), 'Bradley Hand ITC', 30, f'Levels {COUNT_LEVEL}', '#92000a')
        write_some(screen, (20, 230), 'Bradley Hand ITC', 30, f'Health = {HEALTH}', '#92000a')
        write_some(screen, (20, 260), 'Bradley Hand ITC', 30, f'Things {THINGS}', '#92000a')


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    for_final_window(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
