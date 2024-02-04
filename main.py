import pygame
import time
import requests,json
import socket
import threading
import random
import urllib.request
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(external_ip)
pygame.init()
respounse=requests.get(url=f'http://ip-api.com/json/{external_ip}').json()
print(respounse['city'])
screen =pygame.display.set_mode()
api_key="2d916a7afb2c4270b74154631240302"
city=respounse['city']
url = "https://api.weatherapi.com/v1/current.json?key=ed18ed1795e04bde816155729240302&q="+city

full = url+city+"&appid="+api_key
res = requests.get(url)
data = res.json()
print(data['current']['condition']['text'])
d1 = pygame.image.load("Дождь1.png").convert_alpha()
d2 = pygame.image.load("Дождь2.png").convert_alpha()
d3 = pygame.image.load("Дождь3.png").convert_alpha()
d4 = pygame.image.load("Дождь4.png").convert_alpha()
d5 = pygame.image.load("Дождь5.png").convert_alpha()
d6 = pygame.image.load("Дождь6.png").convert_alpha()
d7 = pygame.image.load("Дождь7.png").convert_alpha()
d8 = pygame.image.load("Дождь8.png").convert_alpha()
d9 = pygame.image.load("Дождь9.png").convert_alpha()
d10 = pygame.image.load("Дождь10.png").convert_alpha()
d11 = pygame.image.load("Дождь11.png").convert_alpha()
d12 = pygame.image.load("Дождь12.png").convert_alpha()
d13 = pygame.image.load("Дождь13.png").convert_alpha()
d14 = pygame.image.load("Дождь14.png").convert_alpha()
d15 = pygame.image.load("Дождь15.png").convert_alpha()
d16 = pygame.image.load("Дождь16.png").convert_alpha()
d17 = pygame.image.load("Дождь17.png").convert_alpha()
d18 = pygame.image.load("Дождь18.png").convert_alpha()
d19 = pygame.image.load("Дождь19.png").convert_alpha()
d20 = pygame.image.load("Дождь20.png").convert_alpha()
d21 = pygame.image.load("Дождь21.png").convert_alpha()
d22 = pygame.image.load("Дождь22.png").convert_alpha()
d23 = pygame.image.load("Дождь23.png").convert_alpha()
d24 = pygame.image.load("Дождь24.png").convert_alpha()

dojd=[d4,d4,d4,d5,d5,d5,d6,d6,d6,d7,d7,d7,d10,d10,d10,d11,d11,d11,d12,d12,d12,d13,d13,d13,d14,d14,d14,d15,d15,d15,d16,d16,d16,d17,d17,d17,d18,d18,d18,d19,d19,d19,d20,d20,d20,d21,d21,d21,d22,d22,d22,d23,d23,d23,d24,d24,d24]

d1 = pygame.image.load("Snow1.png").convert_alpha()
d2 = pygame.image.load("Snow2.png").convert_alpha()
d3 = pygame.image.load("Snow3.png").convert_alpha()
d4 = pygame.image.load("Snow4.png").convert_alpha()
d5 = pygame.image.load("Snow5.png").convert_alpha()
d6 = pygame.image.load("Snow6.png").convert_alpha()
d7 = pygame.image.load("Snow7.png").convert_alpha()
d8 = pygame.image.load("Snow8.png").convert_alpha()
d9 = pygame.image.load("Snow9.png").convert_alpha()
d10 = pygame.image.load("Snow10.png").convert_alpha()
d11 = pygame.image.load("Snow11.png").convert_alpha()
d12 = pygame.image.load("Snow12.png").convert_alpha()
d13 = pygame.image.load("Snow13.png").convert_alpha()
d14 = pygame.image.load("Snow14.png").convert_alpha()
d15 = pygame.image.load("Snow15.png").convert_alpha()
d16 = pygame.image.load("Snow16.png").convert_alpha()
d17 = pygame.image.load("Snow17.png").convert_alpha()
d18 = pygame.image.load("Snow18.png").convert_alpha()
d19 = pygame.image.load("Snow19.png").convert_alpha()
d20 = pygame.image.load("Snow20.png").convert_alpha()
d21 = pygame.image.load("Snow21.png").convert_alpha()

sten = pygame.image.load("sten.png").convert_alpha()
sten_scorost=0
sneg=[d4,d4,d4,d4,d4,d4,d4,d5,d5,d5,d5,d5,d5,d5,d6,d6,d6,d6,d6,d6,d6,d7,d7,d7,d7,d7,d7,d8,d8,d8,d8,d8,d8,d8,d9,d9,d9,d9,d9,d9,d9,d10,d10,d10,d10,d10,d10,d10,d11,d11,d11,d11,d11,d11,d11,d12,d12,d12,d12,d12,d12,d12,d13,d13,d13,d13,d13,d13,d13,d14,d14,d14,d14,d14,d14,d14,d15,d15,d15,d15,d15,d15,d15,d16,d16,d16,d16,d16,d17,d17,d17,d17,d17,d18,d18,d18,d18,d18,d18,d19,d19,d19,d19,d19,d19,d20,d20,d20,d20,d20,d20,d21,d21,d21,d21,d21,d21]
sneg_anim=0


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
bg = pygame.image.load("night.png").convert_alpha()
iam = "ryb"
jump=False
jump_size=25
jumptext=pygame.image.load("jump.png").convert_alpha()
jumptext=pygame.transform.scale(jumptext,(60,80))
jamptext_left= pygame.transform.flip(jumptext,True,False)
sugrob=pygame.image.load("sugrob.png").convert_alpha()
ship = pygame.image.load("ship.png").convert_alpha()
ship = pygame.transform.scale(ship,(75,75))
ships =[ship,ship,ship]
hp=500
platform = pygame.image.load("platform.png").convert_alpha()
platform = pygame.transform.scale(platform,(400,200))
zdf=0
dojg_anim=0
pogod=''
earth=pygame.image.load("earth.png").convert_alpha()
z = 1920
timeday=0
def pogoda():
    global data,res,pogod,timeday
    while True:
        res = requests.get(url)
        data = res.json()
        pogod = data['current']['condition']['text']
        print(data['current']['condition']['text'])
        timeday=int(data['location']['localtime'][-5:-3])
t1=threading.Thread(target=pogoda)
t1.start()
mainmenu = pygame.image.load("mainmenuaafterclick.png").convert_alpha()
die = False
deth = pygame.image.load("retyrn1.png").convert_alpha()
mouse=pygame.image.load("mouse.png").convert_alpha()
mouse=pygame.transform.scale(mouse,(20,20))
kd = 1
sunday=pygame.image.load("sunday.png").convert_alpha()
pasmurno = pygame.image.load("posmurno.png").convert_alpha()
def kdd():
    global kd
    time.sleep(2)
    kd = 0
t2=threading.Thread(target=kdd)
t2.start()
rn1 = 600
rn2 = 600
rn3 = 900
while True:
    pygame.display.update()
    if not die:
        print(y)
        screen.fill("blue")
        if timeday>18 or timeday<6:
            screen.blit(bg, (0 , -200 - y))
            screen.blit(bg, (0, -1080 - y))

        if timeday>=6 and timeday <=18:
            screen.blit(sunday, (0, -1080 - y))
            screen.blit(sunday, (0, -200 - y))
        if dojg_anim == 57:
            dojg_anim = 0
        if "Overcast" in pogod or "overcast" in pogod or "rain" in pogod or "Rain" in pogod:
            screen.blit(pasmurno, (0, -1080 - y))
            screen.blit(pasmurno, (0, -200 - y))

        if "rain" in pogod or "Rain" in pogod:
            screen.blit(dojd[dojg_anim], (0, 0 - y))
            dojg_anim += 1
        if sneg_anim == len(sneg):
            sneg_anim = 0
        if "snow" in pogod or "Snow" in pogod or "Blizzard" in pogod or "blizzard" in pogod:
            screen.blit(sneg[sneg_anim], (0, 0 - y))
            sneg_anim += 1
        if "sleet" in pogod or "Sleet" in pogod:
            screen.blit(sneg[sneg_anim], (0, 0 - y))
            sneg_anim += 1
            screen.blit(dojd[dojg_anim], (0, 0 - y))
            dojg_anim += 1

        screen.blit(earth, (0 - x + z - 1920, 850 - y))
        screen.blit(earth, (0 - x + z, 850 - y))
        if x % 1920 == 0 and x != 0:
            z += 1920
            rn3
            rn1=ran1
            rn2=ran2
            rn3 = ran3
            ran1 = random.choice([600, 400, 200])
            ran2 = random.choice([600, 400, 200])
            ran3 = random.choice([900,840,950])
        if x == 0:
            ran1 = random.choice([600, 500, 400])
            ran2 = random.choice([600, 500, 400])
            ran3 = random.choice([900,840,950])

        screen.blit(platform, (0 - x + z - 1920, 600 - y))
        screen.blit(platform, (300 - x + z - 1920, 600 - y))
        screen.blit(platform, (800 - x + z - 1920, rn1 - y))
        screen.blit(platform, (1300 - x + z - 1920, rn2- y))
        screen.blit(platform, (1800 - x + z - 1920, rn1 - y))
        screen.blit(ship, (rn3 - x+z-1920, rn1-75 - y))
        screen.blit(ship, (ran3 - x+z, ran1 - 75 - y))
        screen.blit(platform, (0 - x + z, 600 - y))
        screen.blit(platform, (300 - x + z, 600 - y))
        screen.blit(platform, (800 - x + z , ran1 - y))
        screen.blit(platform, (1300 - x + z, ran2 - y))
        screen.blit(platform, (1800 - x + z, ran1 - y))

        screen.blit(platform, (-300 - x + z - 1920, 600 - y))

        rec_smert = [ship.get_rect(topleft=(rn3 - x+z-1920, rn1-75 - y)),]
        rec = [platform.get_rect(topleft=(0 - x + z - 1920, 600 - y)),
               platform.get_rect(topleft=(300 - x + z - 1920, 600 - y)),
               platform.get_rect(topleft=(800 - x + z - 1920, rn1 - y)),
               platform.get_rect(topleft=(1300 - x + z - 1920, rn2 - y)),
               platform.get_rect(topleft=(1800 - x + z - 1920, rn1 - y)),
               platform.get_rect(topleft=(0 - x + z, 600 - y)), platform.get_rect(topleft=(300 - x + z, 600 - y)),
               platform.get_rect(topleft=(-300 - x + z - 1920, 600 - y))]
        screen.blit(sten,(-600-x+sten_scorost,0-y))
        sten_rec = sten.get_rect(topleft=(-600-x+sten_scorost,300-y))

        if kd == 0:
            sten_scorost+=7.9
        if anim >= 14:
            anim = 0
        if jump:
            if now == "RIGHT" or now == "stay":
                screen.blit(jumptext, (500, 500))
                col = jumptext.get_rect(topleft=(500, 500))
            if now == "LEFT" or now == "stay_left":
                screen.blit(jamptext_left, (500, 500))
                col = jumptext.get_rect(topleft=(500, 500))
        else:
            if now == "RIGHT":
                screen.blit(hero_RIGHT[anim], (500, 500))
                col = hero_RIGHT[anim].get_rect(topleft=(500, 500))
            if now == "LEFT":
                screen.blit(hero_LEFT[anim], (500, 500))
                col = hero_LEFT[anim].get_rect(topleft=(500, 500))
            if now == "stay":
                screen.blit(hero_RIGHT[7], (500, 500))
                col = hero_RIGHT[anim].get_rect(topleft=(500, 500))
            if now == "stay_left":
                screen.blit(hero_LEFT[7], (500, 500))
                col = hero_LEFT[anim].get_rect(topleft=(500, 500))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 8
            now = "LEFT"
            if anim >= 14:
                anim = 0
            else:
                anim += 1
        elif keys[pygame.K_RIGHT]:
            x += 8
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
        if not jump and zdf == 0:
            if keys[pygame.K_SPACE]:
                jump = True
                zdf = 1
        if jump and zdf == 1:
            if jump_size > 0:
                y -= jump_size
                jump_size -= 1
            else:
                zdf = 2
        if sten_rec.colliderect(col):
            x = 0
            y = -100
            die = True
        zx = 0
        fgh = 0
        for i in rec:
            if col.colliderect(i):
                zx = 1
                zdf = 0
                jump = False
                jump_size = 25
                if y >= 60:
                    jump = True
                    if now == "RIGHT":
                        x -= 8
                    if now == "LEFT":
                        x += 8
                        print(111111111111111111111111111111111111111111111111111111111111111111111111111)
                    fgh = 1

        for i in rec_smert:
            if col.colliderect(i):
                x = 0
                y = -100
                zdf = 0
                z = 1920
                jump_size = 16
                jump = False
                die = True

        if y - 100 >= 0:
            zdf = 2

        if y > 450:
            x = 0
            y = -100
            z = 1920
            jump = False
            jump_size = 16
            die = True
        if (zx == 0 and zdf == 2) or (zdf == 0 and zx == 0) or fgh == 1:
            y += jump_size
            jump_size += 1
    else:
        screen.fill("black")
        pygame.mouse.set_visible(False)
        screen.blit(deth,(600,550))
        det_col=deth.get_rect(topleft=(600,500))
        screen.blit(mainmenu,(590,340))
        menu_col=mainmenu.get_rect(topleft=(590,340))
        koordx,koordy=pygame.mouse.get_pos()
        screen.blit(mouse,(koordx,koordy))
        mouse_col =mouse.get_rect(topleft=(koordx,koordy))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                koordx,koordy=pygame.mouse.get_pos()
                print(11233333333333333333333333333333333333333333333333333333)
                if die:
                    if mouse_col.colliderect(det_col):
                        t2 = threading.Thread(target=kdd)
                        t2.start()
                        kd=1
                        jump_size = 25
                        jump = False
                        zdf=0

                        sten_scorost=0
                        print(1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
                        die=False

    clock.tick(60)