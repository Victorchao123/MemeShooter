
import pygame
import random


WIDTH = 600
HEIGHT = 720
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

bg = pygame.image.load("Things/Pictures/flavourtown.jpeg")

pygame.mixer.init()
pygame.mixer.music.load("Things/Sounds/soviet-anthem.mp3")
pygame.mixer.music.play(-1,0.0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meme Shooter")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((43, 68))
        self.image = pygame.image.load("Things/Pictures/josephstalin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_w]:
            self.speedy = -5
        if keystate[pygame.K_s]:
            self.speedy = 5 
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay: 
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image = pygame.image.load("Things/Pictures/knuckles.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 9)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 9)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = pygame.image.load("Things/Pictures/markiplier.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            self.kill()
        else: 
            center = self.rect.center
            self.image = explosion
            self.rect = self.image.get_rect()
            self.rect.center = center

background = pygame.image.load("Things/Pictures/flavourtown.jpg")

kill_sound = pygame.mixer.Sound("Things/Sounds/Blyat.wav")

shoot_sound = pygame.mixer.Sound("Things/Sounds/gun.wav")

explosion = pygame.image.load("Things/Pictures/Explosion.png")


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(6):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
score = 0

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(shoot_sound)
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        pygame.mixer.Sound.play(kill_sound)
        score += 1
        m = Mob()
        all_sprites.add(m)
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        all_sprites.update()
        mobs.add(m)

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
        


    screen.fill(BLACK)
    screen.blit(background, [0, 0])
    all_sprites.draw(screen)
    draw_text(screen, str(score), 50, WIDTH / 2, 10)

    pygame.display.flip()

pygame.quit()