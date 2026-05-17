import pygame
import sys
import datetime
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
cs1=400
cs2=400
R=350

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(color=(250, 248, 240))
    pygame.draw.circle(screen,(180,180,180),(400,400),R+5,10)
    for i in range(1,13):
        angle=math.radians(i*30)
        x1 = cs1+math.cos(angle)*R
        y1 = cs2+math.sin(angle)*R
        x2 = cs1+math.cos(angle)*(R-30)
        y2 = cs2+math.sin(angle)*(R-30)
        pygame.draw.line(screen,(60, 60, 60),(x1,y1),(x2,y2),8)

    for j in range(1,13):
        angle = math.radians(j * 30-90)
        myfont=pygame.font.Font(None, 50)
        text = myfont.render(str(j), True, (60,60,60))
        x3 = cs1+math.cos(angle)*(R-40)-text.get_width()/2
        y3 = cs2-18+math.sin(angle)*(R-50)
        screen.blit(text, (x3,y3))

    now=datetime.datetime.now()
    angle = math.radians(now.hour*30+now.minute*0.5-90)
    x_hour_end = cs1 + math.cos(angle) * (R - 250)
    y_hour_end = cs2 + math.sin(angle) * (R - 250)
    pygame.draw.line(screen, (40,40,40), (400,400), (x_hour_end,y_hour_end), 11)

    angle = math.radians(now.minute*6 - 90)
    x_hour_end = cs1 + math.cos(angle) * (R - 130)
    y_hour_end = cs2 + math.sin(angle) * (R - 130)
    pygame.draw.line(screen, (0,102,204), (400, 400), (x_hour_end, y_hour_end), 11)

    angle = math.radians(now.second*6- 90)
    x_hour_end = cs1 + math.cos(angle) * (R - 40)
    y_hour_end = cs2 + math.sin(angle) * (R - 40)
    pygame.draw.line(screen, (220,20,60), (400, 400), (x_hour_end, y_hour_end), 11)

    pygame.draw.circle(screen, (100, 100, 100), (400, 400), 11, 0)

    pygame.display.update()
