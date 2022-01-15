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



window = display.set_mode((700,500))
back = transform.scale(image.load("background.jpg"), (700,500))
hero = OurSprite("hero.png", 200, 200, 10)
enemy = OurSprite("cyborg.png", 500, 200, 10)


clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

game = True
while game:
    keys_pressed = key.get_pressed()
    window.blit(back, (0,0))
    hero.reset()
    enemy.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False
    if keys_pressed[K_UP] and hero.rect.y > 4:
        hero.rect.y -= 5
    if keys_pressed[K_DOWN] and hero.rect.y < 396:
        hero.rect.y += 5
    if keys_pressed[K_RIGHT] and hero.rect.x < 596:
        hero.rect.x += 5
    if keys_pressed[K_LEFT] and hero.rect.x > 4:
        hero.rect.x -= 5
    
    clock.tick(FPS)
    display.update()