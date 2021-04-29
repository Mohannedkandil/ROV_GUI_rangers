import pygame
import time

pygame.init()
pygame.joystick.init()
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
mx = 688 / 2
my = 394 / 2
screen = pygame.display.set_mode((688, 394))
done = False
is_blue = True
x = 30
y = 30
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# pygame.draw.rect(screen,(0,128,255),pygame.Rect(30,30,60,60))
pygame.display.set_caption('Immortals ROV')
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
transparent = (0, 0, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 32)


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((688 / 2), (394 / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    # time.sleep(2)


''' UP, DOWN,RIGHT, & LEFT IDLE State '''
img_up = pygame.image.load("arrow_up_red.png")
img_down = pygame.image.load("arrow_up_red.png")
img_left = pygame.image.load("arrow_up_red.png")
img_right = pygame.image.load("arrow_up_red.png")
up = pygame.image.load("up2.png")
down = pygame.image.load("up2_active.png")
background = pygame.image.load("2.jpg")
GOpen = pygame.image.load("GOpen.png")
GClose = pygame.image.load("GClose.png")
GOpen2 = pygame.image.load("GOpen.png")
GClose2 = pygame.image.load("GClose.png")
off = pygame.image.load("off_button.png")
on = pygame.image.load("on_button.png")
'''Transform Pictures IDLE'''
img_down = pygame.transform.rotate(img_down, 180)
img_right = pygame.transform.rotate(img_right, 90)
img_left = pygame.transform.rotate(img_left, -90)
up = pygame.transform.rotate(up, 90)
''' UP, DOWN,RIGHT, & LEFT ACTIVE State '''
img_up_active = pygame.image.load("arrow_up_green.png")
img_down_active = pygame.image.load("arrow_up_green.png")
img_left_active = pygame.image.load("arrow_up_green.png")
img_right_active = pygame.image.load("arrow_up_green.png")
up_active = pygame.image.load("up2_active.png")

'''Transform Pictures ACTIVE'''
img_up_active = pygame.transform.rotate(img_up_active, 0)
img_down_active = pygame.transform.rotate(img_down_active, 180)
img_right_active = pygame.transform.rotate(img_right_active, 90)
img_left_active = pygame.transform.rotate(img_left_active, -90)
up_active = pygame.transform.rotate(up_active, 90)
down_active = pygame.transform.rotate(up_active, -90)
bon = pygame.transform.scale(on, (75, 75))
boff = pygame.transform.scale(off, (75, 75))
bon2 = pygame.transform.scale(on, (75, 75))
boff2 = pygame.transform.scale(off, (75, 75))
clock = pygame.time.Clock()
pygame.transform.rotate(img_down, 90)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # if is_blue: color = (0,128,255)
    # else: color = (255,100,0)
    xc = 550
    xc2 = 490
    yc = 290
    yc2 = 290
    screen.fill((71, 71, 135))
    '''SHOW GRAPHICS'''
    screen.blit(background, (0, 0))
    screen.blit(img_up, (mx, 130))
    screen.blit(img_down, (mx, 220))
    screen.blit(img_right, (mx - 50, 175))
    screen.blit(img_left, (mx + 50, 175))
    screen.blit(GOpen, (xc, yc))
    screen.blit(GClose, (xc, yc))
    screen.blit(GOpen2, (xc2, yc2))
    screen.blit(GClose2, (xc2, yc2))
    screen.blit(boff, (550, 130))
    screen.blit(bon, (550, 130))
    screen.blit(boff2, (470, 130))
    screen.blit(bon2, (470, 130))

    # screen.blit(up,(550,280))
    # screen.blit(up_active,(550,280))
    down = pygame.transform.rotate(up_active, 180)
    upp = pygame.transform.rotate(up, 0)

    gc = pygame.transform.rotate(GOpen, 360)
    go = pygame.transform.rotate(GClose, 360)

    gc2 = pygame.transform.rotate(GOpen2, 360)
    go2 = pygame.transform.rotate(GClose2, 360)

    ''' ACTIVE BUTTONS '''
    '''
    screen.blit(img_up_active,(550,130))
    screen.blit(img_down_active,(550,215))
    screen.blit(img_right_active,(500,170))
    screen.blit(img_left_active,(595,170)) 
    '''
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    # pressed = pygame.key.get_pressed()
    axis = joystick.get_axis(1)
    # print(axis)
    axisRL = joystick.get_axis(0)
    print(axisRL)

    if -0.40 < axis < -0.20:
        screen.blit(img_up_active, (mx, 130))
        # message_display('Mohanad kandil')
        print("S1")
    elif -0.55 < axis < -0.40:
        screen.blit(img_up_active, (mx, 130))
        print("S2")
    elif -0.65 < axis < -0.55:
        screen.blit(img_up_active, (mx, 130))
        print("S3")
    elif -0.75 < axis < -0.65:
        screen.blit(img_up_active, (mx, 130))
        print("S4")
    elif -0.85 < axis < -0.75:
        screen.blit(img_up_active, (mx, 130))
        print("S5")
    elif -0.90 < axis < -0.85:
        screen.blit(img_up_active, (mx, 130))
        print("S6")
    elif -0.95 < axis < -0.90:
        screen.blit(img_up_active, (mx, 130))
        print("S7")
    elif -0.97 < axis < -0.95:
        screen.blit(img_up_active, (mx, 130))
        print("S8")
    elif -1.0 < axis < -0.97:
        screen.blit(img_up_active, (mx, 130))
        print("S9")

    elif 0.20 < axis < 0.40:
        screen.blit(img_down_active, (mx, 220))
        print("S1 - Backward")
    elif 0.40 < axis < 0.55:
        screen.blit(img_down_active, (mx, 220))
        print("S2 - Backward")
    elif 0.55 < axis < 0.65:
        screen.blit(img_down_active, (mx, 220))
        print("S3 - Backward")
    elif 0.65 < axis < 0.75:
        screen.blit(img_down_active, (mx, 220))
        print("S4 - Backward")
    elif 0.75 < axis < 0.85:
        screen.blit(img_down_active, (mx, 220))
        print("S5 - Backward")
    elif 0.85 < axis < 0.90:
        screen.blit(img_down_active, (mx, 220))
        print("S6 - Backward")
    elif 0.90 < axis < 0.95:
        screen.blit(img_down_active, (mx, 220))
        print("S7 - Backward")
    elif 0.95 < axis < 0.97:
        screen.blit(img_down_active, (mx, 220))
        print("S8 - Backward")
    elif 0.97 < axis < 1.00:
        screen.blit(img_down_active, (mx, 220))
        print("S9 - Backward")

    ''' ROTATE '''
    if -0.40 < axisRL < -0.20:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L1")
    elif -0.55 < axisRL < -0.40:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L2")
    elif -0.65 < axisRL < -0.55:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L3")
    elif -0.75 < axisRL < -0.65:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L4")
    elif -0.85 < axisRL < -0.75:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L5")
    elif -0.90 < axisRL < -0.85:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L6")
    elif -0.95 < axisRL < -0.90:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L7")
    elif -0.97 < axisRL < -0.95:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L8")
    elif -1.00 < axisRL < -0.97:
        screen.blit(img_right_active, (mx - 50, 175))
        print("L9")
    # if pressed[pygame.K_RIGHT]:screen.blit(img_left_active,(595,170))
    elif 0.20 < axisRL < 0.40:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R1")
    elif 0.40 < axisRL < 0.55:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R2")
    elif 0.55 < axisRL < 0.65:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R3")
    elif 0.65 < axisRL < 0.75:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R4")
    elif 0.75 < axisRL < 0.85:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R5")
    elif 0.85 < axisRL < 0.90:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R6")
    elif 0.90 < axisRL < 0.95:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R7")
    elif 0.95 < axisRL < 0.97:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R8")
    elif 0.97 < axisRL < 1.00:
        screen.blit(img_left_active, (mx + 50, 175))
        print("R9")
    # print(joystick.get_axis(2)) #deubging

    if (joystick.get_axis(2) > 0.20):
        upp.fill(transparent)
        screen.blit(down, (600, 280))

    if (joystick.get_axis(2) < -0.35):
        down.fill(transparent)
        screen.blit(upp, (600, 280))

    if joystick.get_button(0) == 1:
        print("Ow")

    if joystick.get_button(1) == 1:
        print(":(")

    if joystick.get_button(2) == 1:
        # go.fill(transparent)
        print("CLOSE GRIPPER1")
        # screen.blit(gc,(xc,yc))
        # screen.blit(GClose,(xc,yc))
    GClose.fill(transparent)
    GClose2.fill(transparent)

    if joystick.get_button(3) == 1:
        go2.fill(transparent)
        print("CLOSE GRIPPER2")

    if joystick.get_button(4) == 1:
        print("OPEN GRIPPER1")
        # screen.blit(go,(xc,yc))

    if joystick.get_button(5) == 1:
        gc2.fill(transparent)
        print("OPEN GRIPPER2")
        screen.blit(go2, (xc2, yc2))

    if joystick.get_button(6) == 1:
        print("6")

    if joystick.get_button(7) == 1:
        print("Button 7 pressed")

    if joystick.get_button(8) == 1:
        print("Button 8 pressed")

    if joystick.get_button(9) == 1:
        print("Button 9 pressed")

    if joystick.get_button(10) == 1:
        print("Button 10 pressed")

    if joystick.get_button(11) == 1:
        print("Button 11 pressed")

    # x = joystick.get_axis(5)
    # print(x)

    #   pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
'''
0 - trigger
1 - btn2
4 - 5
2 - 3
3 - 4
5 - 6
-----
axis = joystick.get_axis(1) - Stick

joystick.get_axis(2) - slider

joystick.get_axis(3) - Z-axis
'''