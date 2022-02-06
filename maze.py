from pygame import *
from time import sleep
#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
class OurSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(OurSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
class Enemy(OurSprite):
    def move(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 615:
            self.direction = "left"
class Wall(sprite.Sprite):
    def __init__(self, width, height, x, y, R, G, B):
        super().__init__()
        # self.R = R
        # self.G = G
        # self.B = B
        self.width = width
        self.height = height
        self.wall = Surface((self.width, self.height))
        self.wall.fill((R,G,B))
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw_wall(self):
        window.blit(self.wall, (self.rect.x, self.rect.y))

window = display.set_mode((700,500))
back = transform.scale(image.load("background.jpg"), (700,500))
hero = Player("hero.png", 200, 200, 4)
enemy = Enemy("cyborg.png", 614, 300, 2)
enemy.direction = "left"
finish = OurSprite("treasure.png", 600, 400, 0)
w1 = Wall(170, 20, 200, 400, 154, 205, 50)
w2 = Wall(20, 450, 450, 75, 154, 205, 50)
w3 = Wall(20, 400, 350, 0, 154, 205, 50)

clock = time.Clock()
FPS = 60
mixer.init()
font.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

game = True
while game:
    window.blit(back, (0,0))
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    hero.reset()
    enemy.reset()
    finish.reset()
    hero.move()
    enemy.move()
    clock.tick(FPS)
    if sprite.collide_rect(hero, finish):
        mixer.music.load("money.ogg")
        mixer.music.play()
        fnt = font.Font(None, 70)
        text = fnt.render("YOU WIN!", True, [215, 215, 0])
        window.blit(text, (300, 170))
        display.update()
        sleep(1)
        game=False
    if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3):
        mixer.music.load("kick.ogg")
        mixer.music.play()
        fnt = font.Font(None, 70)
        text = fnt.render("YOU LOSE!", True, [254, 88, 32])
        window.blit(text, (300, 170))
        display.update()
        sleep(1)
        game=False
    display.update()