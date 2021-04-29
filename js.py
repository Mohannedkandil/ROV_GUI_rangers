import pygame
import serial
import math
import os
import time


# Enter your COM port in the below line
ser = serial.Serial('COM3', 9600)

pygame.init()
pygame.joystick.init()
if pygame.joystick.init() == True:
    print('Working')
else:
    pass
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
mx = 688 / 2
my = 394 / 2
screen = pygame.display.set_mode((800, 500))
done = False
is_blue = True
x = 30
y = 30
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = '#2ecc71'
# pygame.draw.rect(screen,(0,128,255),pygame.Rect(30,30,60,60))
pygame.display.set_caption('Immortals ROV')
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
transparent = (0, 0, 0, 0)



#font = pygame.font.Font('freesansbold.ttf', 25)
font = pygame.font.SysFont('arial', 25)
''' UP, DOWN,RIGHT, & LEFT IDLE State '''
img_up = pygame.image.load("arrow_up_red.png")
img_down = pygame.image.load("arrow_up_red.png")
img_left = pygame.image.load("arrow_up_red.png")
img_right = pygame.image.load("arrow_up_red.png")
up = pygame.image.load("up2.png")
down = pygame.image.load("up2_active.png")
#background = pygame.image.load("2.jpg")
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
    screen.fill((44, 62, 80))
    '''SHOW GRAPHICS'''
    #screen.blit(background, (0, 0))
    #bar(10, 0, 10, 50, [52, 152, 219], [231, 76, 60], 150, 200)


    #screen.blit(rect, (mx, 90))

    screen.blit(img_up, (mx, 130))
    screen.blit(img_down, (mx, 220))
    screen.blit(img_right, (mx - 50, 175))
    screen.blit(img_left, (mx + 50, 175))
    #screen.blit(GOpen, (xc, yc))
    #screen.blit(GClose, (xc, yc))
    #screen.blit(GOpen2, (xc2, yc2))
    #screen.blit(GClose2, (xc2, yc2))
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

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    # pressed = pygame.key.get_pressed()
    axis = joystick.get_axis(1)
    print("F&B: {}".format(axis))
    axisRL = joystick.get_axis(0)
    slider = joystick.get_axis(2)
    # print("RL: {}".format(axisRL))
    z = joystick.get_axis(3)
    sliderr = slider * 100
    axiss= axis * 100
    textsurface = font.render('F & B', False, (255, 255, 255))
    screen.blit(textsurface, (40, 50))
    #pygame.draw.rect(screen, red, (130, 130, 30, 100))

    #pygame.draw.rect(screen, black, (130, 130, 30, result))
    pygame.draw.rect(screen, red, (40, 200, 30, -100)) # forward
    pygame.draw.rect(screen, red, (100, 100, 30, 100)) # backward
    #slider
    pygame.draw.rect(screen, red, (40, 350, 30, -100))  # forward
    pygame.draw.rect(screen, red, (100, 250, 30, 100))  # backward
    if axis<=-0.070 and axis>=-1.00: #forwad

        pygame.draw.rect(screen, black, (40, 200, 30, axiss))

    if axis<=1.00 and axis>=0.30: #backward

        pygame.draw.rect(screen, black, (100, 100, 30, axiss))

    if slider<=-0.10 and slider>=-1.00: # UP
        pygame.draw.rect(screen, black, (40, 350, 30, sliderr))  # forward

    if slider>0.10 and slider<=1.00: # UP
        pygame.draw.rect(screen, black, (100, 250, 30, sliderr))  # forward

    # if -0.40<axis<-0.20:
    if axis <= -0.070 and axis > -0.40:
        print('stop')
        ser.write(b's')
    if axis <= -0.40 and axis >= -0.50:
        screen.blit(img_up_active, (mx, 130))
        textsurface = font.render('Forward Speed 1', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        print('forward 1')
        ser.write(b'g')
    if axis <= -0.50 and axis >= -0.60:
        screen.blit(img_up_active, (mx, 130))
        textsurface = font.render('Forward Speed 2', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'h')
        print('forward 2')
    if axis <= -0.60 and axis >= -0.80:
        ser.write(b'j')
        screen.blit(img_up_active, (mx, 130))
        textsurface = font.render('Forward Speed 3', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        print('Forward 3')
    if axis <= -0.80 and axis >= -1.00:
        ser.write(b'k')
        screen.blit(img_up_active, (mx, 130))
        textsurface = font.render('Forward Speed 4', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        print('Forward 4')

    if axis <= -0.070 and axis >= -0.30:
        print('stop Backward')
        ser.write(b's')
    if axis <= 0.40 and axis >= 0.30:
        print('Backward 1')
        screen.blit(img_down_active, (mx, 220))
        textsurface = font.render('Backward Speed 1', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'b')
    if axis <= 0.60 and axis >= 0.40:
        screen.blit(img_down_active, (mx, 220))
        textsurface = font.render('Backward Speed 2', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'n')
        print('Backward 2')
    if axis <= 0.80 and axis >= 0.60:
        screen.blit(img_down_active, (mx, 220))
        textsurface = font.render('Backward Speed 3', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'm')
        print('Backward 3')
    if axis <= 1.00 and axis >= 0.80:
        screen.blit(img_down_active, (mx, 220))
        textsurface = font.render('Backward Speed 4', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'l')
        print('Backward 4')

    if -0.5 <= axisRL <= -0.50:
        ser.write(b's')
        print('Stop glowing')
    if axisRL >= -0.60 and axisRL <= -0.50:
        screen.blit(img_right_active, (mx - 50, 175))
        textsurface = font.render('Left Speed 1', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'y')
        print("Left 1")
    if -0.60 <= axisRL <= -0.40:
        screen.blit(img_right_active, (mx - 50, 175))
        textsurface = font.render('Left Speed 2', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'u')
        print("Left 2")
    if -0.80 <= axisRL <= -0.60:
        screen.blit(img_right_active, (mx - 50, 175))
        textsurface = font.render('Left Speed 3', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'i')
        print("Left 3")
    if -1.00 <= axisRL <= -0.81:
        screen.blit(img_right_active, (mx - 50, 175))
        textsurface = font.render('Left Speed 4', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'o')
        print("Left 4")

    if 0.20 <= axisRL <= 0.5:
        ser.write(b's')
        print('Stop glowing')
    if axisRL >= 0.50 and axisRL <= 0.60:
        screen.blit(img_left_active, (mx + 50, 175))
        textsurface = font.render('Right Speed 1', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'q')
        print("Right 1")
    if axisRL >= 0.60 and axisRL <= 0.80:
        screen.blit(img_left_active, (mx + 50, 175))
        textsurface = font.render('Right Speed 2', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'e')
        print("Right 2")
    if axisRL >= 0.80 and axis <= 0.89:
        screen.blit(img_left_active, (mx + 50, 175))
        textsurface = font.render('Right Speed 3', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'r')
        print("Right 3")

    if slider >= 0.45 and slider <= 0.75:
        # textsurface = font.render('STOP UP & DOWN', False, (255, 255, 255))
        # screen.blit(textsurface,(mx-100,350))
        ser.write(b'D')
        print('STOP U & D STOPPED')
    if -0.40 <= slider <= -0.20:
        #textsurface = font.render('Slider UP Speed 1', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'a')
        print("STOP U & D 1")
    if -0.60 <= slider <= -0.40:
        #textsurface = font.render('Slider UP Speed 2', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'w')
        print("Up 2")
    if -0.80 <= slider <= -0.60:
        #textsurface = font.render('Slider UP Speed 3', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'd')
        print("Up 3")
    if -1.00 <= slider <= -0.80:
        #textsurface = font.render('Slider UP Speed 4', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'f')
        print('Up 2')
    if 0.20 < slider <= 0.40:
        #textsurface = font.render('STOP', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'D')
    if 0.20 < slider < 0.40:
        #textsurface = font.render('Slider Down Speed 1', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'z')
        print("DOWN 1")
    if 0.40 < slider < 0.60:
        #textsurface = font.render('Slider Down Speed 2', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'x')
        print("DOWN 2")
    if 0.60 < slider < 0.80:
        #textsurface = font.render('Slider Down Speed 3', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'c')
        print("DOWN 3")
    if 0.80 < slider <= 1.00:
        #textsurface = font.render('Slider Down Speed 4', False, (255, 255, 255))
        #screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'v')
        print("DOWN 4")

    # print(joystick.get_axis(2)) #deubging
    if joystick.get_button(0):
        textsurface = font.render('Z-axis', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        if z <= -0.070 and z >= -0.60:
            textsurface = font.render('STOP  Rotation', False, (255, 255, 255))
            screen.blit(textsurface, (mx - 100, 350))
            ser.write(b'G')
        if -0.50 <= z <= -0.60:
            textsurface = font.render('Rotate Left Speed 1', False, (255, 255, 255))
            screen.blit(textsurface, (mx - 100, 350))
            ser.write(b'5')
            print("Rotate Left 1")
        if -0.80 <= z <= -0.60:
            textsurface = font.render('Rotate Left Speed 2', False, (255, 255, 255))
            screen.blit(textsurface, (mx - 100, 350))
            ser.write(b'6')
            print("Rotate Left 2")
        if -0.90 <= z <= -0.80:
            textsurface = font.render('Rotate Left Speed 3', False, (255, 255, 255))
            screen.blit(textsurface, (mx - 100, 350))
            ser.write(b'7')
            print("Rotate Left 3")
        '''    
        if -1.00<=z<=-0.90:
            textsurface = font.render('Rotate Left Speed 4', False, (255, 255, 255))
            screen.blit(textsurface,(mx-100,350))
            #ser.write(b'8')
            print("Rotate Left 4")
        '''

        if z <= 0.40 and z >= 0.07:
            textsurface = font.render('STOP Rotation', False, (255, 255, 255))
            screen.blit(textsurface, (mx - 100, 300))
            ser.write(b'G')
        if 0.40 <= z <= 0.50:
            textsurface = font.render('Rotate Right Speed 1', False, (255, 255, 255))
            screen.blit(textsurface, (mx - 100, 350))
            ser.write(b'1')
            print("Rotate Right 1")
        if 0.50 <= z <= 0.70:
            textsurface = font.render('Rotate Right Speed 2', False, (255, 255, 255))
            screen.blit(textsurface, (mx - 100, 350))
            ser.write(b'2')
            print("Rotate Right 2")
        if 0.70 <= z <= 0.80:
            textsurface = font.render('Rotate Right Speed 3', False, (255, 255, 255))
            screen.blit(textsurface, (mx - 100, 350))
            ser.write(b'3')
            print("Rotate Right 3")

    if (joystick.get_axis(2) > 0.20):
        upp.fill(transparent)
        screen.blit(down, (600, 280))

    if (joystick.get_axis(2) < -0.35):
        down.fill(transparent)
        screen.blit(upp, (600, 280))

    if joystick.get_button(1) == 1:
        ser.write(b's')

    if joystick.get_button(1) == 1:
        # print(":(")
        textsurface = font.render('Servo Close', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'B')

    if joystick.get_button(2) == 1:
        # go.fill(transparent)
        textsurface = font.render('Close Gripper 1', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        print("CLOSE GRIPPER1")
        ser.write(b'C')
        # screen.blit(gc,(xc,yc))
        # screen.blit(GClose,(xc,yc))
    GClose.fill(transparent)
    GClose2.fill(transparent)

    if joystick.get_button(3) == 1:
        go2.fill(transparent)
        textsurface = font.render('Close Gripper 2', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        print("CLOSE GRIPPER2")
        ser.write(b'W')

    if joystick.get_button(4) == 1:
        textsurface = font.render('Open Gripper 1', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        print("OPEN GRIPPER1")

        ser.write(b'O')
        # screen.blit(go,(xc,yc))

    if joystick.get_button(5) == 1:
        gc2.fill(transparent)
        textsurface = font.render('Open Gripper 2', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        print("OPEN GRIPPER2")
        ser.write(b'A')

        screen.blit(go2, (xc2, yc2))

    if joystick.get_button(6) == 1:
        textsurface = font.render('Servo Open', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'8')

    if joystick.get_button(7) == 1:
        textsurface = font.render('Servo Close', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'4')

    if joystick.get_button(8) == 1:
        textsurface = font.render('Stop', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b's')

    if joystick.get_button(9) == 1:
        textsurface = font.render('Light On', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'8')

    if joystick.get_button(10) == 1:
        textsurface = font.render('Light On', False, (255, 255, 255))
        screen.blit(textsurface, (mx - 100, 350))
        ser.write(b'4')
    if joystick.get_button(11) == 1:
        ser.write(b's')
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