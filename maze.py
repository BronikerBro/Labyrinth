from pygame import *

class OurSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (65,65))
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



window = display.set_mode((700,500))
back = transform.scale(image.load("background.jpg"), (700,500))
hero = Player("hero.png", 200, 200, 4)
enemy = Enemy("cyborg.png", 614, 400, 2)
enemy.direction = "left"


clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

game = True
while game:
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back, (0,0))
    hero.reset()
    enemy.reset()
    hero.move()
    enemy.move()
    clock.tick(FPS)
    display.update()