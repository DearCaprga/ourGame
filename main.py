import pygame


def restart():
    screen.fill(pygame.Color(0, 0, 0))
    Start_window()
    ALL_TIMER = 0
    HEALTH = 100
    COUNT_LEVEL = 0
    THINGS = 0


def for_final_window(screen):
    if ALL_TIMER > 30 or HEALTH == 0 or COUNT_LEVEL == 3:
        open_window = Final_window(screen)
        return True
    return False


def write_some(screen, coordinates, style, sizi, texty, color):
    font = pygame.font.SysFont(style, sizi)
    text = font.render(texty, True, pygame.Color(color))
    screen.blit(text, coordinates)


class Final_window:
    def __init__(self, screen):
        directory = []
        if ALL_TIMER > 30:
            directory = [[(90, 10), 'Chiller', 50, 'You fall'],
                         [(30, 60), 'Bradley Hand ITC', 'You thought to long...'],
                         [(30, 100), 'Bradley Hand ITC', 30, 'So you were killed']]
        elif HEALTH == 0:
            directory = [[(90, 10), 'Chiller', 50, 'You fall'],
                         [(30, 60), 'Bradley Hand ITC', 30, 'Your health is...'],
                         [(170, 100), 'Bradley Hand ITC', 30, 'Too small']]
        elif COUNT_LEVEL == 3:
            directory = [[(150, 30), 'Chiller', 45, 'You win'],
                         [(50, 90), 'Bradley Hand ITC', 28, 'You finished this game'],
                         [(90, 120), 'Bradley Hand ITC', 28, 'You are lucky']]
        for i in range(3):
            write_some(screen, directory[i][0], directory[i][1], directory[i][2], directory[i][3], '#92000a')
        write_some(screen, (0, 140), 'Bradley Hand ITC', 30, '-------------------------------------------', '#92000a')
        directory = [[(50, 170), 'Bradley Hand ITC', 35, f'Time =          {ALL_TIMER}'],
                     [(50, 220), 'Bradley Hand ITC', 35, f'Levels            {COUNT_LEVEL}'],
                     [(50, 270), 'Bradley Hand ITC', 35, f'Health =       {HEALTH}'],
                     [(50, 320), 'Bradley Hand ITC', 35, f'Things          {THINGS}']]
        for i in range(4):
            write_some(screen, directory[i][0], directory[i][1], directory[i][2], directory[i][3],
                       '#92000a')  # parameters


if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    restart()

    for_final_window(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
