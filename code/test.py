import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
color = (200, 100, 70)
surface = pygame.Surface((30, 50))
surface.fill(color)
surface.set_alpha(145)
running = True
while running:
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    screen.blit(surface, (100, 100))
    pygame.display.update()

pygame.quit()