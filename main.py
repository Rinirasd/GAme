import pygame

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
BG_COLOR = (255,127,127)

W = 1068
H = 600
LEN = 40

FPS = 60

pygame.init()

screen = pygame.display.set_mode((W, H))
background = pygame.image.load("image/фон.jpg")
background1 = pygame.image.load("image/умер.jpg")
pygame.display.set_caption("Test Столкновение спрайтов")
pygame.display.flip()
music = pygame.mixer.Sound("music/the-epic-2-by-rafael-krux(chosic.com).mp3")
music.play()
musicym = pygame.mixer.Sound("music/zvuk-iz-mema-smert-v-gta-5-gta-v---wasted-3380.mp3")
clock = pygame.time.Clock()

sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.image.load("image/персонаж.png").convert_alpha()

sprite1.rect = sprite1.image.get_rect(center = (100, 100))

sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.image.load("image/персонаж 2.png").convert_alpha()
sprite2.rect = sprite2.image.get_rect(center = (200, 200))

all_sprites_group = pygame.sprite.Group([sprite1, sprite2])



running = True
dx = 0
dy = 0
dx1 = 0
dy1 = 0

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx = -5
    if keys[pygame.K_RIGHT]:
        dx = 5
    if keys[pygame.K_UP]:
        dy = -5
    if keys[pygame.K_DOWN]:
        dy = 5
    sprite1.rect.x += dx
    sprite1.rect.y += dy
    dx = dy = 0

    if keys[pygame.K_a]:
        dx1 = -5
    if keys[pygame.K_d]:
        dx1 = 5
    if keys[pygame.K_w]:
        dy1 = -5
    if keys[pygame.K_s]:
        dy1 = 5
    sprite2.rect.x += dx1
    sprite2.rect.y += dy1
    dx1 = dy1 = 0

    hit = pygame.sprite.collide_rect(sprite1, sprite2)
    if hit:
        bg_color = background1
        musicym.play()
    else:
        bg_color = background



    screen.blit(bg_color,(0,0))
    all_sprites_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()