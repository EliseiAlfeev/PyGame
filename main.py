import pygame
import time
import requests,json
import socket
import threading

import urllib.request
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(external_ip)
pygame.init()
respounse=requests.get(url=f'http://ip-api.com/json/{external_ip}').json()
print(respounse['city'])
screen =pygame.display.set_mode((1000,1000))
api_key="2d916a7afb2c4270b74154631240302"
city="new york"
url = "http://api.weatherapi.com/v1/current.json/?key="+api_key+"&q="+city

full = url+city+"&appid="+api_key
res = requests.get(url)
data = res.json()
print(data)


c = pygame.image.load("1.png").convert_alpha()
b = pygame.image.load("2.png").convert_alpha()
c = pygame.transform.scale(c,(40,80))
b = pygame.transform.scale(b,(40,80))
hero_RIGHT=[
    c,c,c,c,c,c,c,
    b,b,b,b,b,b,b
]

c = pygame.transform.flip(c, True, False)
b = pygame.transform.flip(b, True, False)
hero_LEFT=[
    c,c,c,c,c,c,c,
    b,b,b,b,b,b,b
]


x = 0
y = 0
anim = 0
now = "stay"
now1 ="RIGHT"
clock=pygame.time.Clock()
bg = pygame.image.load("bg.jpg").convert_alpha()
bg = pygame.transform.scale(bg,(10000,10000))
iam = "ryb"
jump=False
jump_size=16
jumptext=pygame.image.load("jump.png")
jumptext=pygame.transform.scale(jumptext,(60,80))
jamptext_left= pygame.transform.flip(jumptext,True,False)

ship = pygame.image.load("ship.png")
ship = pygame.transform.scale(ship,(75,75))
ships =[ship,ship,ship]
hp=500
platform = pygame.image.load("platform.png")
platform = pygame.transform.scale(platform,(400,80))
zdf=0
while True:
    pygame.display.update()
    screen.blit(bg,(0-x,0-y))
    screen.blit(platform,(300-x,600-y))
    screen.blit(platform, (800- x, 600 - y))
    screen.blit(platform, (1300 - x, 600 - y))
    rec=[platform.get_rect(topleft=(300-x,600-y)),platform.get_rect(topleft=(800-x,600-y)),platform.get_rect(topleft=(1300-x,600-y))]
    if anim >=14:
        anim=0
    if jump:
        if now == "RIGHT" or now == "stay":
            screen.blit(jumptext,(500,500))
            col = jumptext.get_rect(topleft=(500,500))
        if now == "LEFT" or now == "stay_left":
            screen.blit(jamptext_left, (500, 500))
            col = jumptext.get_rect(topleft=(500, 500))
    else:
        if now == "RIGHT":
            screen.blit(hero_RIGHT[anim], (500, 500))
            col = hero_RIGHT[anim].get_rect(topleft=(500,500))
        if now == "LEFT":
            screen.blit(hero_LEFT[anim], (500, 500))
            col = hero_LEFT[anim].get_rect(topleft=(500,500))
        if now == "stay":
            screen.blit(hero_RIGHT[7], (500, 500))
            col = hero_RIGHT[anim].get_rect(topleft=(500,500))
        if now == "stay_left":
            screen.blit(hero_LEFT[7], (500, 500))
            col = hero_LEFT[anim].get_rect(topleft=(500,500))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
        now = "LEFT"
        if anim >= 14:
            anim = 0
        else:
            anim += 1
    elif keys[pygame.K_RIGHT]:
        x += 5
        now = "RIGHT"
        if anim >= 14:
            anim = 0
        else:
            anim += 1
    else:
        if now == "RIGHT":
            now = "stay"
        if now == "LEFT":
            now = "stay_left"
    if not jump and zdf ==0:
        if keys[pygame.K_SPACE]:
            jump=True
            zdf=1
    if jump and zdf ==1:
        if jump_size > 0:
            y-=jump_size
            jump_size-=1
        else:
            zdf=2

    zx = 0
    fgh=0
    for i in rec:
        if col.colliderect(i):
            zx=1
            if jump_size >= 16:
                zdf = 0
                jump=False
                jump_size=16
            if y-34>=0:
                jump = True
                if now == "RIGHT":
                    x-=5
                if now == "LEFT":
                    x+=5
                    print(111111111111111111111111111111111111111111111111111111111111111111111111111)
                fgh =1

    if y - 34 >= 0:
        zdf = 2

    if y > 1000:
        x = 0
        y = -20

    if (zx == 0 and zdf == 2) or (zdf == 0 and zx == 0) or fgh == 1:
        y+=jump_size
        jump_size+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(60)