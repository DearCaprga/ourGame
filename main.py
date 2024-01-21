import pygame
from PIL import Image
import random
import os
import datetime
import sys

all_sprites = pygame.sprite.Group()
LIST = ['start', 'loc0', 'loc1']
FIRST_TIME = datetime.datetime.now()
ALL_TIMER = 0
COUNT_LEVEL = 1
HEALTH = 100
THINGS = []
clock = pygame.time.Clock()
now_s = str(datetime.datetime.now().second)
now_m = str(datetime.datetime.now().minute)
code = now_s[0] + now_m[-1] + now_s[-1] + '3'
print(code)
pygame.init()
with open('setings.txt', 'w', encoding='utf-8') as file, open('constants.txt', 'w', encoding='utf-8') as file1:
    file.write('000')
    file1.write(code + ' 0')


# before classes there are functions that help with basic things

# close game
def terminate():
    pygame.quit()
    sys.exit()


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
    # pygame.display.flip()


def write_text(screen, coordinates, style='Bernard MT Condensed', size=25, text='', color='white'):
    kol = text.count(':')
    text = text.split(':')
    for i in range(kol + 1):
        write_some(screen, (coordinates[0], coordinates[1] + (size + 2) * i), style, size, text[i], color)
    pygame.display.flip()


def load_image(name, colorkey=None, size=(), turn=0):
    img = Image.open(os.path.join('data', name))
    if size != ():
        img.thumbnail(size=size)
        img = img.rotate(turn)
    img.save('picture.png')
    fullname = os.path.join('picture.png')
    image = pygame.image.load(fullname)
    # image.transform.scale(image, (size1, size2))
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def play_music(state):
    if state:
        pygame.mixer.music.load('background music.mp3')
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.pause()


# it helps change windows
def windows(wind, wall):
    if wind == 'start':
        Start_window()
    elif wind == 'loc0':
        Locations().location0(wall)
    elif wind == 'loc1':
        Locations().location1(wall)


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
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    Settings(screen, wall=0).find_set(x, y, 'start', wall=0)
                    if 190 <= x <= 380 and 175 <= y <= 295:  # clicked on start
                        Locations().perface()
                        return


class Final_window:
    def __init__(self):
        global ALL_TIMER, COUNT_LEVEL, HEALTH, THINGS
        with open('setings.txt', 'r') as file:
            hard = int(file.read()[2])
        sreen = new_window(400, 400)
        sreen.fill((0, 0, 0))
        directory = []
        time_all = str(datetime.datetime.now() - FIRST_TIME).split(':')
        ALL_TIMER = int(time_all[0][-2:]) * 360 + int(time_all[1]) * 60 + int(time_all[-1][:2])
        running = True
        if 'h2o' in THINGS and 'hclo4' in THINGS and 'fe' in THINGS:
            COUNT_LEVEL += 1
            if ALL_TIMER > 60:
                HEALTH //= ALL_TIMER // 60
        if ALL_TIMER >= 780 + 120 * hard:
            directory = [[(150, 10), 'Chiller', 50, 'You fall'],
                         [(30, 60), 'Bradley Hand ITC', 30, 'You thought to long...'],
                         [(30, 100), 'Bradley Hand ITC', 30, 'So you were killed']]
        elif HEALTH == 0:
            directory = [[(150, 10), 'Chiller', 50, 'You fall'],
                         [(30, 60), 'Bradley Hand ITC', 30, 'Your health is...'],
                         [(170, 100), 'Bradley Hand ITC', 30, 'Too small']]
        elif COUNT_LEVEL == 2:
            directory = [[(150, 30), 'Chiller', 45, 'You win'],
                         [(50, 90), 'Bradley Hand ITC', 28, 'You finished this game'],
                         [(90, 120), 'Bradley Hand ITC', 28, 'You are lucky']]

        while running:
            for i in range(3):
                write_some(sreen, directory[i][0], directory[i][1], directory[i][2], directory[i][3], '#92000a')
            write_some(sreen, (0, 140), 'Bradley Hand ITC', 30, '-------------------------------------------',
                       '#92000a')
            directory = [[(50, 170), 'Bradley Hand ITC', 35, f'Time =          {ALL_TIMER}'],
                         [(50, 220), 'Bradley Hand ITC', 35, f'Levels            {COUNT_LEVEL}'],
                         [(50, 270), 'Bradley Hand ITC', 35, f'Health =       {HEALTH}']]
            for i in range(3):
                write_some(sreen, directory[i][0], directory[i][1], directory[i][2], directory[i][3],
                           '#92000a')  # parameters
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()


class Settings:  # in txt will be settings
    def __init__(self, screen, wall, corner=535, winds='start'):
        Sprites(all_sprites, screen=screen, colorkey=-1, name_file='seting.jpg', xy=(corner, 0), size=(70, 70))
        self.screen = screen
        self.corner = corner
        self.winds = winds
        self.wall = wall

    def find_set(self, x, y, wind, wall):
        if x >= self.corner and y <= 70:  # clicked on settings
            Settings(self.screen, winds=wind, wall=wall).settings_view()

    def settings_view(self):
        screen_set = new_window(600, 400)
        running = True
        while running:
            file1, line = self.file_open()
            screen_set.fill('black')
            write_some(self.screen, (10, 10), 'Bradley Hand ITC', 25, 'back', 'blue')
            write_some(screen_set, (180, 20), 'Bradley Hand ITC', 50, 'Settings', '#92000a')
            for i in range(3):
                write_some(screen_set, (80, 120 + i * 70), 'Bradley Hand ITC', 40,
                           ['Music', 'Scream', 'Speed'][i], '#92000a')  # 120 190 260
                write_some(screen_set, (300, 120 + i * 70), 'Bradley Hand ITC', 40,
                           ['off / on', 'low / high', 'light / hard'][i], '#92000a')

            time_all = str(datetime.datetime.now() - FIRST_TIME).split(':')
            ALL_TIMER = int(time_all[0][-2:]) * 360 + int(time_all[1]) * 60 + int(time_all[-1][:2])
            write_some(screen_set, (420, 10), 'Arial', 15, 'Seconds have passed:' + str(ALL_TIMER))
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 300 <= x <= 420 and 120 <= y <= 160:
                        if x <= 350:
                            file1.write('0' + str(line[1]) + str(line[2]))
                        elif x >= 380:
                            file1.write('1' + str(line[1]) + str(line[2]))
                        file1.close()
                        file, line = self.file_open()
                        play_music(line[0])
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

    def find_rules(self, x, y, wind, size=690):
        if size <= x <= size + 50 and 10 <= y <= 60:  # clicked on rules
            Rules(self.screen, wind=wind, wall=self.wall).rules_view()

    def rules_view(self):
        screen_rules = new_window(600, 400)
        write_some(self.screen, (10, 10), 'Bradley Hand ITC', 25, 'back', 'blue')
        write_some(screen_rules, (180, 20), 'Bradley Hand ITC', 50, 'Rules guide', '#92000a')
        text = ' - Чтобы передвинуть обзор на следующую стену,:нажмите кнопки <-, -> на клавиатуре:' \
               ' - Чтобы узнать больше о предмете, на него надо:"нажать" мышкой:' \
               ' - Время можно увидеть в настройках:' \
               ' - Если таймер закончится до конца прохождения, :то игра завершится:' \
               ' - Если где-то надо ввести текст, то ничего нажимать: не надо, просто печатайте' \
               ' - Не медлите, чем дольше вы играете, тем меньше у вас здоровья.'
        write_text(screen_rules, (80, 100), text=text)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 10 <= x <= 50 and 10 <= y <= 35:
                        button_back(screen_rules, self.screen, self.winds, self.wall)
                        return


class Locations:
    def perface(self):
        flag5 = 1
        flag10 = 1
        screen = new_window(600, 400)
        sec_start = datetime.datetime.now().second

        write_some(screen, (200, 150), texty='Как я тут оказался?')
        write_some(screen, (130, 177), texty='Голова болит, кажется сильный ушиб…')

        running = True
        while running:
            pygame.display.flip()
            if datetime.datetime.now().second == sec_start + 4 and flag5:
                screen.fill(pygame.Color("black"))
                text = 'Я точно помню, как мы решили пойти вместе в ту заброшку :' \
                       'про которую говорил весь город. Вроде когда-то тут жила :' \
                       'счастливая семья, но они неожиданно уехали. Никто так и :' \
                       'не знает истинной причины, но каждый старался придумать :' \
                       'свою легенду. '
                write_text(screen, coordinates=(40, 130), text=text)
                flag5 = 0

            elif datetime.datetime.now().second == sec_start + 9 and flag10:
                screen.fill(pygame.Color('black'))
                text = 'Ничего… больше ничего не помню, почему я здесь:' \
                       'один, кто меня ударил и как отсюда выбраться?:' \
                       'Нельзя медлить, иначе будет хуже.'
                write_text(screen, coordinates=(80, 150), text=text)
                flag10 = 0
            elif datetime.datetime.now().second == sec_start + 11:
                self.location0(0)
                return

    def location0(self, wall):
        clock = pygame.time.Clock()
        clock.tick(4000)
        start_time = datetime.datetime.now()
        print(start_time)
        screen0 = new_window(800, 560)
        running = True
        text_input = ''
        while running:
            pygame.display.flip()
            Sprites(all_sprites, screen=screen0, name_file='wall0.png', xy=(0, 0), size=(800, 600))
            Rules(screen0, 'loc0', wall=wall)
            Settings(screen0, wall, 735, 'loc0')
            with open('setings.txt', 'r') as file, open('constants.txt', 'r') as f:
                file_scr = f.read().split()
                file = file.read()
            if file_scr[1] == '1':
                print('scream')
                Sprites(all_sprites, screen=screen0, name_file='pursuing_screamer.png', xy=(50, 400),
                        size=(400, 400), colorkey=-1)
            # I don`t think there will be def because of different parameters
            if wall == 0:
                text_input = ''
                answer = ''
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
                answer = ''
                Sprites(all_sprites, screen=screen0, name_file='frame_pic0.png', xy=(60, 60),
                        size=(250, 250), colorkey=-1)
                random_sprites(screen0, 'eyes.png', (90, 240, 90, 180), kol=(5, 15), size1=10, size2=70, footsize=5)
                Sprites(all_sprites, screen=screen0, name_file='firewood.png', xy=(300, 300),
                        size=(400, 400), colorkey=-1)
            elif wall == 3:
                answer = ''
                Sprites(all_sprites, screen=screen0, name_file='tv.png', xy=(450, 300),
                        size=(200, 200))
                Sprites(all_sprites, screen=screen0, name_file='door.png', xy=(80, 20),
                        size=(400, 400), colorkey=-1)
                Sprites(all_sprites, screen=screen0, name_file='frame.png', xy=(280, 180),
                        size=(120, 120), colorkey=-1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    Settings(screen0, wall, 735, 'loc0').find_set(x, y, 'loc0', wall=wall)
                    Rules(screen0, 'loc0', wall=wall).find_rules(x, y, 'loc0')
                    print(wall)
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
                        elif 375 <= x <= 440 and 319 <= y <= 398:
                            text = f'Возмите число {code[2]} на заметку: : : : :' \
                                   f'Еще 2 ящика закрыты простым смертным'
                            print('left table')
                            sp = [('box0.png',), ((0, 0),), ((600, 450),)]
                            click_thing(screen0, wall, name_file=sp[0], xyspr=sp[1], size=sp[2], kolspr=1,
                                        text=text, xytxt=(150, 210), colortxt='#92000a')
                            return
                        elif 599 <= x <= 689 and 345 <= y <= 438:
                            print('right table')
                            if file[1] == '1':
                                text = 'Запомни число, сколько :раз к тебе будут стучаться:' \
                                       'каждый раз, поделенное :на 5.'
                            else:
                                text = 'Кажется, число 3 может :где-то пригодиться.'

                            click_thing(screen0, wall, name_file=('box0.png', 'paper_list.png'),
                                        xyspr=((0, 0), (160, 130)), size=((600, 450), (250, 250)), kolspr=2,
                                        text=text, xytxt=(170, 170), colortxt='SaddleBrown')
                            return
                    elif wall == 1:
                        if 64 <= x <= 328 and 69 <= y <= 416:
                            print('wardrobe hi')
                            sp = [('wardrobe_open.png', 'kotik_screamer_clothes_13.png', 'text_input.png'),
                                  ((0, 0), (100, 170), (200, 200)), ((600, 450), (170, 170), (150, 150))]
                            if file[1] == '1':
                                text = 'Было 16 ног — я посчитал. :Проспал две недели — :десяток пропал. :Кто я?'
                            else:
                                text = 'Ты видишь меня только: с одной стороны. :Я меняюсь каждый день.' \
                                       ':Иногда большая, :иногда едва заметная. :Кто я?'
                            click_thing(screen0, wall, name_file=sp[0], xyspr=sp[1], size=sp[2], kolspr=3,
                                        text=text, xytxt=(120, 50))
                            return
                        elif 429 <= x <= 670 and 230 <= y <= 408:
                            print('oy armchair')
                            sp = [('sledgehammer.png',), ((100, 150),),
                                  ((300, 300),)]
                            if file_scr[1] == '1':
                                text = 'Ура вы нашли кувалду и убили монстрика.'
                                with open('constants.txt', 'r+') as file:
                                    print(file_scr[1])
                                    file_scr[1] = '0'
                                    file.write(file_scr[0] + ' ' + file_scr[1])
                            else:
                                text = 'Вы нашли кувалду, но она вам не нужна, :поэтому оставили на своем месте.'
                            click_thing(screen0, wall, name_file=sp[0], xyspr=sp[1], size=sp[2], kolspr=1,
                                        text=text, xytxt=(150, 120))
                            return
                    elif wall == 2:
                        if 64 <= x <= 328 and 69 <= y <= 416:
                            print('picture')
                            with open('constants.txt', 'r+') as file:
                                print(file_scr[1])
                                file_scr[1] = '1'
                                file.write(file_scr[0] + ' ' + file_scr[1])
                            Sprites(all_sprites, screen=screen0, name_file='pursuing_screamer.png', xy=(50, 400),
                                    size=(400, 400), colorkey=-1)
                            text = 'На вас выскочил скример, так что: избавьтесь от него или останьтесь с ним навсегда'
                            click_thing(screen0, wall, text=text, xytxt=(150, 120))
                            return
                        else:
                            print('wood')
                            sp = [('wood.png',), ((0, 0),), ((600, 450),)]
                            text = 'Количество кучек поленьев пригодится потом.:Если ничего нет, так и запомни'
                            click_thing(screen0, wall, name_file=sp[0], text=text, xytxt=(0, 350), rand=1)
                            return
                    elif wall == 3:
                        if 450 <= x <= 640 and 300 <= y <= 440:
                            print('tv')
                            text = ' - Первым возьми число от загадки:' \
                                   ' - Потом допиши число, котрое встретилось рядом с картиной:' \
                                   ' - Последними двумя числами будут из левого и правого ящиков:'
                            click_thing(screen0, wall, text=text, xytxt=(20, 120))
                            return

                if event.type == pygame.KEYDOWN:
                    if wall == 3:  # input code
                        inp = event.unicode
                        if len(text_input) < 4 and inp.isdigit():
                            text_input += inp
                        print(text_input)
                    wall = move_poin(event, wall)

            write_some(screen0, (300, 200), texty=' '.join(list(text_input)), size=40)

            if text_input == code and file_scr[1] == '0':
                print('OK')
                animation(17, 1, 50, "image_anima.jpg", (0, 0))
                return

    def location1(self, wall):
        global ALL_TIMER, FIRST_TIME, THINGS
        image_now = 'im21.jpg'
        wall = wall
        book_list = 0
        screen = new_window(500, 500)
        images = ['im21.jpg', 'im22.jpg', '23.jpg', '24.jpg']
        name_images = images.index(wall)
        image = load_image(images[name_images % 4], size=(500, 500))
        image = pygame.transform.scale(image, (500, 500))
        arrow = pygame.sprite.Sprite(all_sprites)
        arrow.image = image
        arrow.rect = arrow.image.get_rect()
        running = True
        while running:
            Settings(screen, wall=wall, corner=435, winds='loc1')
            Rules(screen, wind='loc1', wall=wall, x=380)
            with open('setings.txt', 'r') as file:
                hard = (int(file.read()[2]) - 1) * -1
            if ALL_TIMER >= 780 + 120 * hard or len(THINGS) == 3:
                # если HARD = 1, то 15 мин, если 0 - 13 мин
                arrow.kill()
                running = False
                screen.fill(pygame.Color(0, 0, 0))
                Final_window()
                # final()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    Settings(screen, wall, corner=435, winds='loc1').find_set(x, y, 'loc1', wall)
                    Rules(screen, 'loc1', wall=wall, x=380).find_rules(x, y, 'loc1', size=380)
                    if 96 < x < 194 and 32 < y < 105 and image_now == 'im21.jpg':
                        arrow, image_now = things_closer(arrow, 'image_stol.jpg')

                    if 237 < x < 277 and 113 < y < 172 and image_now == 'im21.jpg':
                        arrow, image_now = things_closer(arrow, '24.jpg')

                    if 154 < x < 180 and 172 < y < 202 and image_now == '24.jpg':
                        arrow, image_now = things_closer(arrow, 'imbook.PNG')

                    if 267 < x < 302 and 102 < y < 152 and image_now == '24.jpg':
                        arrow, image_now = things_closer(arrow, 'book0.jpg')
                        book_list = 0

                    if 63 < x < 456 and 79 < y < 429 and image_now == f'book0.jpg':
                        arrow, image_now = things_closer(arrow, f'book{book_list % 8}.jpg')
                        image_now = 'book0.jpg'
                        if 250 < x < 500:
                            book_list += 1
                        else:
                            book_list -= 1
                    if 90 < x < 191 and 139 < y < 220 and image_now == 'im21.jpg':
                        arrow, image_now = things_closer(arrow, 'im_lek1.jpg')

                    if len(THINGS) < 3:
                        if image_now == 'im_lek1.jpg':
                            if 118 < x < 138 and 62 < y < 134:
                                THINGS.append('h2o')
                            elif 71 < x < 95 and 410 < y < 457:
                                THINGS.append('fe')
                            elif 352 < x < 395 and 29 < y < 160:
                                THINGS.append('hclo4')
                            elif 180 < x < 196 and 107 < y < 137:
                                THINGS.append('cu')
                            elif 207 < x < 224 and 80 < y < 142:
                                THINGS.append('zn')
                            elif 229 < x < 245 and 123 < y < 145:
                                THINGS.append('be')
                            elif 49 < x < 90 and 309 < y < 385:
                                THINGS.append('кровь человеческая')
                            elif 94 < x < 111 and 425 < y < 460:
                                THINGS.append('cl')
                            elif 29 < x < 57 and 377 < y < 461:
                                THINGS.append('cm')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        images, name_images, image_now, arrow = next_wind(images, name_images, arrow)
                    if event.key == pygame.K_LEFT:
                        name_images += 1
                        images, name_images, image_now, arrow = next_wind(images, name_images, arrow)
                    elif event.key == pygame.K_RIGHT:
                        name_images -= 1
                        images, name_images, image_now, arrow = next_wind(images, name_images, arrow)
                screen.fill(pygame.Color(0, 0, 0))
                all_sprites.draw(screen)
                pygame.display.flip()


# this 4 def help in locations
def things_closer(arrow, name_im):
    arrow.kill()
    image = load_image(name_im)
    if name_im == '24.jpg':
        size = (470, 470)
    else:
        size = (500, 500)
    image = pygame.transform.scale(image, size)
    arrow = pygame.sprite.Sprite(all_sprites)
    arrow.image = image
    arrow.rect = arrow.image.get_rect()
    image_now = name_im
    return arrow, image_now


def next_wind(images, name_images, arrow):
    arrow.kill()
    image_now = images[name_images % 4]
    image = load_image(images[name_images % 4])
    image = pygame.transform.scale(image, (500, 500))
    arrow = pygame.sprite.Sprite(all_sprites)
    arrow.image = image
    arrow.rect = arrow.image.get_rect()
    return images, name_images, image_now, arrow


# bring the pressed item closer
def click_thing(screen, wall, name_file=(), xyspr=(), size=(), kolspr=1, text='', xytxt=(0, 0),
                wind='loc0', colortxt='white', rand=0):
    answer = ''
    screen_th = new_window(600, 390)
    screen.fill(pygame.Color("black"))
    screen_th.fill(pygame.Color("black"))
    with open('setings.txt', 'r') as file:
        file = file.read()
    if rand:
        for i in range(int(code[1])):
            x = random.randrange(50, 450, 10)
            y = random.randrange(100, 250, 10)
            Sprites(all_sprites, screen=screen_th, name_file=name_file[0], xy=(x, y), size=(100, 100), colorkey=-1)
    else:
        if name_file and xyspr and size:
            for i in range(kolspr):
                name = name_file[i]
                print(name)
                if (name[-6:-4] == '13' and file[1] == '1') or name[-6:-4] != '13':
                    Sprites(all_sprites, screen=screen_th, name_file=name, xy=xyspr[i], size=size[i], colorkey=-1)
    write_some(screen_th, (10, 10), 'Bradley Hand ITC', 25, 'back', 'blue')
    write_text(screen_th, xytxt, text=text, color=colortxt)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 10 <= x <= 50 and 10 <= y <= 35:
                    print(file[0])
                    if text.split()[0] == 'Окно':
                        play_music(int(file[0]))
                    button_back(screen_th, screen, wind, wall)
                    return
            if event.type == pygame.KEYDOWN:
                if wall == 1:
                    inp = event.unicode
                    if len(answer) < 9:
                        answer += inp
                    print(answer)

        write_some(screen_th, (220, 220), texty=answer, size=30)
        if (file[1] == '1' and answer == 'бабочка') or (file[1] == '0' and answer == 'луна'):
            write_some(screen_th, (210, 250), texty=f'Помни число {code[0]}')
        pygame.display.flip()


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


# after levels
def animation(width_pic, height_pic, fps, name_pic, position=(0, 0)):
    all_shot = width_pic * height_pic
    timer = pygame.time.Clock()
    frames = []
    screen = pygame.display.set_mode((500, 500))
    image = pygame.image.load(os.path.join('data', name_pic))
    width, height = image.get_size()
    w_each, h_each = width / width_pic, height / height_pic
    shot = 0
    print('anima')
    for j in range(int(height / h_each)):
        for i in range(int(width / w_each)):
            frames.append(image.subsurface(pygame.Rect(w_each * i, shot, w_each, h_each)))
        shot += int(h_each)
    number = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 0))
                something(2)
                return
        screen.fill((0, 0, 0))
        number += 1
        number %= all_shot
        screen.blit(frames[number], position)
        pygame.display.update()
        timer.tick(fps)


# info about level
def something(number_of_level):  # preface to the beginning of the level
    screenn = new_window(500, 500)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Landing((random.randint(0, 500), random.randint(0, 300)))
                    print('land')
                    pass
                if event.key == pygame.K_RIGHT:
                    screenn.fill(pygame.Color(0, 0, 0))
                    print('second')
                    Locations().location1(wall='im21.jpg')
                    return

        screen.fill(pygame.Color("black"))
        with open(f'{number_of_level}.txt', 'rt', encoding='utf-8') as f:
            y = 50
            for i in f:
                write_some(screenn, (50, y), 'Bradley Hand ITC', 30, i.rstrip(), '#92000a')
                y += 40
        # pygame.display.flip()
        com_sprites.draw(screen)
        com_sprites.update()
        pygame.display.flip()
        clock.tick(50)


# for beautiful def something
class Mountain(pygame.sprite.Sprite):
    screen = new_window(500, 500)
    image = load_image("стол.png", colorkey=-1, size=(500, 100))
    image = pygame.transform.scale(image, (500, 100))

    def __init__(self):
        super().__init__(com_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 500


screen = new_window(500, 500)
com_sprites = pygame.sprite.Group()
mountain = Mountain()


# it`s also for def something
class Landing(pygame.sprite.Sprite):
    image = load_image("im_camen.jpg", colorkey=-1, size=(100, 100))
    image = pygame.transform.scale(image, (100, 100))

    def __init__(self, pos):
        super().__init__(com_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


if __name__ == '__main__':
    Start_window()
    pygame.display.flip()
    pygame.quit()
