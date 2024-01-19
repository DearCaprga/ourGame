import pygame
# import pygame.freetype
from PIL import Image
import random
import os
import datetime

all_sprites = pygame.sprite.Group()
LIST = ['start', 'loc0', 'loc1']
WALL = 0
clock = pygame.time.Clock()
now_s = str(datetime.datetime.now().second)
now_m = str(datetime.datetime.now().minute)
code = now_s[0] + now_m[-1] + now_s[-1] + now_m[0]
print(code)
with open('setings.txt', 'w', encoding='utf-8') as file, open('constants.txt', 'w', encoding='utf-8') as file1:
    file.write('000')
    file1.write(f'right_code {code};')


# write def for back button
# write def for sprite in walls


def new_window(width, height):
    pygame.init()
    size = width, height
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(0, 0, 0))
    return screen


def write_some(screen, coordinates, style='Bernard MT Condensed', size=25, texty='', color='white'):
    font = pygame.font.SysFont(style, size)
    text = font.render(texty, True, color)
    screen.blit(text, coordinates)
    pygame.display.flip()


def write_text(screen, coordinates, style='Bernard MT Condensed', size=25, text='', color='white'):
    kol = text.count(':')
    text = text.split(':')
    for i in range(kol + 1):
        write_some(screen, (coordinates[0], coordinates[1] + (size + 2) * i), style, size, text[i], color)


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
    return image


class Sprites(pygame.sprite.Sprite):
    def __init__(self, *group, screen, colorkey=None, name_file, xy, turn=0, size=(50, 50)):
        super().__init__(*group)
        image = load_image(os.path.join(name_file), turn=turn, size=size, colorkey=colorkey)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = xy[0], xy[1]
        all_sprites.draw(screen)
        clock.tick(1000)


class Start_window:
    def __init__(self):
        screen = new_window(600, 400)
        pygame.font.init()
        running = True
        pygame.draw.rect(screen, '#92000a', pygame.Rect(210, 190, 160, 90), 2, 20)
        [write_some(screen, [(130, 40), (230, 190)][i], 'Chiller', 90 - 20 * i, ['Original name', 'Start!'][i],
                    '#92000a') for i in range(2)]

        Settings(screen, wall=0)

        Sprites(all_sprites, screen=screen, name_file="startovi.jpg", xy=(-40, 150), turn=25, size=(250, 250))
        Sprites(all_sprites, screen=screen, name_file="ladon.jpg", xy=(400, 300), turn=-45, size=(200, 200))

        sec_start = datetime.datetime.now().second
        flag_drop = True

        while running:
            pygame.display.flip()

            if datetime.datetime.now().second == sec_start + 4 and flag_drop:
                flag_drop = False
                random_sprites(screen, 'blood.jpg', (400, 520, 110, 250), (100, 350, 295, 320))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    Settings(screen, wall=0).find_set(x, y, 'start', wall=0)
                    if 190 <= x <= 380 and 175 <= y <= 295:  # clicked on start
                        Locations().perface()
                        return


class Settings:  # in txt will be settings
    def __init__(self, screen, wall, corner=535, winds='start'):
        Sprites(all_sprites, screen=screen, colorkey=-1, name_file='seting.jpg', xy=(corner, 0), size=(70, 70))
        self.screen = screen
        self.corner = corner
        self.winds = winds
        self.wall = wall

    def find_set(self, x, y, wind, wall):
        if x >= self.corner and y <= 70:  # clicked on settings
            print('qwerty')
            Settings(self.screen, winds=wind, wall=wall).settings_view()

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
                    elif 10 <= x <= 50 and 10 <= y <= 35:
                        button_back(screen_set, self.screen, self.winds, self.wall)
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


class Rules:
    def __init__(self, screen, wind, wall, x=690):
        Sprites(all_sprites, colorkey=-1, screen=screen, name_file='book.png', xy=(x, 10), turn=0, size=(50, 50))
        self.screen = screen
        self.winds = wind
        self.wall = wall

    def find_rules(self, x, y, wind):
        if 690 <= x <= 740 and 10 <= y <= 60:  # clicked on settings
            Rules(self.screen, wind=wind, wall=self.wall).rules_view()

    def rules_view(self):
        screen_rules = new_window(600, 400)
        write_some(self.screen, (10, 10), 'Bradley Hand ITC', 25, 'back', 'blue')
        write_some(screen_rules, (180, 20), 'Bradley Hand ITC', 50, 'Rules guide', '#92000a')
        text = ' - Чтобы передвинуть обзор на следующую стену,:нажмите кнопки <-, -> на клавиатуре:' \
               ' - Чтобы узнать больше о предмете, на него надо:"нажать" мышкой или навести курсор и нажать Q:' \
               ' - При длительном общении с непонятными челиками :теряется здоровье:' \
               ' - Если таймер закончится до конца прохождения, :то игра завершится:' \
               ' - Если где-то надо ввести текст, то ничего нажимать: не надо, просто печатайте.'
        write_text(screen_rules, (80, 100), text=text)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 10 <= x <= 50 and 10 <= y <= 35:
                        button_back(screen_rules, self.screen, self.winds, self.wall)
                        return


class Locations:
    def __init__(self):
        pass

    def perface(self):
        flag5 = 1
        flag10 = 1
        screen = new_window(600, 400)
        sec_start = datetime.datetime.now().second

        write_some(screen, (200, 150), texty='Как я тут оказался?')
        write_some(screen, (130, 177), texty='Голова болит, кажется сильный ушиб…')

        running = True
        while running:
            if datetime.datetime.now().second == sec_start + 1 and flag5:
                screen.fill(pygame.Color("black"))
                text = 'Я точно помню, как мы решили пойти вместе в ту заброшку :' \
                       'про которую говорил весь город. Вроде когда-то тут жила :' \
                       'счастливая семья, но они неожиданно уехали. Никто так и :' \
                       'не знает истинной причины, но каждый старался придумать :' \
                       'свою легенду. '
                write_text(screen, coordinates=(40, 130), text=text)
                flag5 = 0

            if datetime.datetime.now().second == sec_start + 2 and flag10:
                screen.fill(pygame.Color('black'))
                text = 'Ничего… больше ничего не помню, почему я здесь:' \
                       'один, кто меня ударил и как отсюда выбраться?:' \
                       'Нельзя медлить, иначе будет хуже.'
                write_text(screen, coordinates=(80, 150), text=text)
                flag10 = 0
            if datetime.datetime.now().second == sec_start + 3:
                self.location0(0)
                return

    def location0(self, wall):
        clock = pygame.time.Clock()
        clock.tick(2000)
        start_time = datetime.datetime.now()
        print(start_time)
        with open('constants.txt', 'r') as f:
            code = f.read().split(';')[0].split()[1]

        screen0 = new_window(800, 560)
        running = True
        text_input = ''
        while running:
            pygame.display.flip()
            Sprites(all_sprites, screen=screen0, name_file='wall0.png', xy=(0, 0), size=(800, 600))
            Rules(screen0, 'loc0', wall=wall)
            Settings(screen0, wall, 735, 'loc0')
            with open('setings.txt', 'r') as file:
                file = file.read()
            if wall == 0:
                text_input = ''
                if file[1] == '0':
                    picture = 'broke_window0.png'
                else:
                    picture = 'window_screamer.png'
                Sprites(all_sprites, screen=screen0, name_file=picture, xy=(40, 50),
                        size=(400, 400), colorkey=-1)
                Sprites(all_sprites, screen=screen0, name_file='table.png', xy=(350, 250), size=(400, 400),
                        colorkey=-1)
            elif wall == 1:
                text_input = ''
                Sprites(all_sprites, screen=screen0, name_file='wardrobe0.png', xy=(40, 50),
                        size=(400, 400), colorkey=-1)
                Sprites(all_sprites, screen=screen0, name_file='armchair.png', xy=(400, 260),
                        size=(300, 300), colorkey=-1)
            elif wall == 2:
                text_input = ''
                Sprites(all_sprites, screen=screen0, name_file='frame_pic0.png', xy=(60, 60),
                        size=(250, 250), colorkey=-1)
                random_sprites(screen0, 'eyes.png', (90, 250, 90, 180), kol=(5, 15), size1=10, size2=70, footsize=5)
                Sprites(all_sprites, screen=screen0, name_file='firewood.png', xy=(300, 300),
                        size=(400, 400), colorkey=-1)
            elif wall == 3:
                Sprites(all_sprites, screen=screen0, name_file='tv.png', xy=(450, 300),
                        size=(200, 200), colorkey=-1)
                Sprites(all_sprites, screen=screen0, name_file='door.png', xy=(80, 20),
                        size=(400, 400), colorkey=-1)
                Sprites(all_sprites, screen=screen0, name_file='frame.png', xy=(280, 180),
                        size=(120, 120), colorkey=-1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    Settings(screen0, wall, 735, 'loc0').find_set(x, y, 'loc0', wall=wall)
                    Rules(screen0, 'loc0', wall=wall).find_rules(x, y, 'loc0')
                    if wall == 0:
                        if 168 <= x <= 287 and 129 <= y <= 298:
                            if file[1] == '1':
                                pygame.mixer.music.load('knock on wood.mp3')
                                pygame.mixer.music.play(3)
                            print('reel window')
                            text = 'Окно так заколочено, что :выбраться из него будет невозможно.: : : : : : :' \
                                   'Окно такое смешное, я выпал.'
                            click_thing(screen0, wall, text=text, xytxt=(150, 120))
                            return
                        else:
                            text = 'Магическим обазом 2 ящика стали одним.'
                            if 375 <= x <= 440 and 319 <= y <= 398:
                                print('left table')
                                sp = [('box.png', ''), ((0, 0), ()), ((600, 450),)]
                                click_thing(screen0, wall, name_file=sp[0], xyspr=sp[1], size=sp[2], kolspr=2,
                                            text=text, xytxt=(250, 370))
                                return
                            elif 599 <= x <= 689 and 345 <= y <= 438:
                                print('right table')
                                click_thing(screen0, wall, name_file='box.png', xyspr=(0, 0), size=(600, 450), kolspr=2)
                                return
                    if wall == 1:
                        if 64 <= x <= 328 and 69 <= y <= 416:
                            print('wardrobe hi')
                            sp = [('wardrobe_open.png', 'kotik_screamer_clothes_13.png'), ((0, 0), (100, 170)),
                                  ((600, 450), (170, 170))]
                            click_thing(screen0, wall, name_file=sp[0], xyspr=sp[1], size=sp[2], kolspr=2)
                            return
                        elif 429 <= x <= 670 and 230 <= y <= 408:
                            print('oy armchair')
                            # sp = [('.png', '.png'), ((0, 0), (100, 170)),
                            #       ((600, 450), (170, 170))]
                            # click_thing(screen0, wall, name_file=sp[0], xyspr=sp[1], size=sp[2], kolspr=2)
                            return

                if event.type == pygame.KEYDOWN:
                    if wall == 3:  # input code
                        inp = event.unicode
                        if len(text_input) < 4 and inp.isdigit():
                            text_input += inp
                        print(text_input)
                    wall = move_poin(event, wall)

            write_some(screen0, (300, 200), texty=' '.join(list(text_input)), size=40)

            if text_input == code:
                print('OK')
                pygame.mixer.music.load('door_open.mp3')
                pygame.mixer.music.play(1)
        pygame.quit()


# bring the pressed item closer
def click_thing(screen, wall, name_file=(), xyspr=(), size=(), kolspr=1, text='', xytxt=(0, 0), wind='loc0'):
    screen_th = new_window(600, 390)
    screen_th.fill(pygame.Color("black"))
    with open('setings.txt', 'r') as file:
        file = file.read()
    if name_file and xyspr and size:
        for i in range(kolspr):
            name = name_file[i]
            if (name[-6:-4] == '13' and file[1] == '1') or name[-6:-4] != '13':
                Sprites(all_sprites, screen=screen_th, name_file=name, xy=xyspr[i], size=size[i], colorkey=-1)
    write_some(screen_th, (10, 10), 'Bradley Hand ITC', 25, 'back', 'blue')
    write_text(screen_th, xytxt, text=text)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 10 <= x <= 50 and 10 <= y <= 35:
                    button_back(screen_th, screen, wind, wall)
                    return


# provides 4-sided viewing
def move_poin(event, wall):
    if event.key == pygame.K_LEFT:
        if wall > 0:
            wall -= 1
        else:
            wall = 3
    elif event.key == pygame.K_RIGHT:
        wall = (wall + 1) % 4
    elif event.key == pygame.K_DOWN:
        pass
    return wall


# it helps change windows
def windows(wind, wall):
    if wind == 'start':
        Start_window()
    elif wind == 'loc0':
        Locations().location0(wall)
    # elif wind == 'loc1':
    #     Locations().location1(wall)


# back to the main window
def button_back(screen1, screen2, wind, wall):
    screen1.fill(pygame.Color("black"))
    screen2.fill(pygame.Color("black"))
    windows(wind, wall)


def random_sprites(screen, file_name, sp1=(), sp2=(), kol=(2, 3), size1=50, size2=150, footsize=10):
    for i in range(random.randrange(kol[0], kol[1])):
        turn = random.randrange(1, 70, 5)
        size = random.randrange(size1, size2, footsize)
        if sp2:
            coord = random.choice([(random.randrange(sp1[0], sp1[1], 10), random.randrange(sp1[2], sp1[3], 10)),
                                   (random.randrange(sp2[0], sp2[1], 10), random.randrange(sp2[2], sp2[3], 10))])
        else:
            coord = random.randrange(sp1[0], sp1[1], 10), random.randrange(sp1[2], sp1[3], 10)
        Sprites(all_sprites, screen=screen, name_file=file_name, xy=coord, turn=turn, size=(size, size), colorkey=-1)


if __name__ == '__main__':
    Start_window()
    pygame.display.flip()
    pygame.quit()
