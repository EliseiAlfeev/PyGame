import pygame
import time
import requests,json
import socket
import threading
pygame.init()
screen =pygame.display.set_mode((1000,1000))
api_key="f5ea1444ac76d17489d97833763c006c"
url = "https://api.openweathermap.org/data/2.5/weather?q="
city="Moscow"
full = url+city+"&appid="+api_key
res = requests.get(full)
data = res.json()
print(data)
hero = pygame.image.load("1.png").convert_alpha()
hero = pygame.transform.scale(hero,(100,150))
x = 0
y = 0
anim = 0
now = "stay"
now1 ="RIGHT"
clock=pygame.time.Clock()
bg = pygame.image.load("bg.jpg").convert_alpha()
bg = pygame.transform.scale(bg,(1000,1000))
iam = "rb"
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost="192.168.21.149"
port=1488
client.connect((localhost,port))
def listen():
    while True:
        r = client.recv(4096).decode().split("z")
        v = r[0]
        r = v.split()
        print(r)
def otprav():
    while True:
        client.sendall(bytes(iam+" "+str(x)+" "+str(y)+"z","UTF-8"))
        time.sleep(0.02)
        print(iam+" "+str(x)+" "+str(y))

t1 = threading.Thread(target=otprav)
t1.start()
t2 = threading.Thread(target=listen)
t2.start()
print(111111111111111111111111111111111111111)
while True:
    pygame.display.update()
    screen.blit(bg,(0-x,0))
    screen.blit(hero,(500,500))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
        now = "LEFT"
        if anim == 23:
            anim = 0
        else:
            anim += 1
    elif keys[pygame.K_RIGHT]:
        x += 5
        now = "RIGHT"
        if anim == 23:
            anim = 0
        else:
            anim += 1
    else:
        if now == "RIGHT":
            now = "stay"
        else:
            now = "stay_left"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(60)