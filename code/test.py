from os.path import join
from settings import *

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

def get_angle(hand_pos):
    mouse_pos = pygame.mouse.get_pos()

    dx = (mouse_pos[0] - hand_pos[0])
    dy = (mouse_pos[1] - hand_pos[1])
    mouse_angle = atan2(-dy, dx)
    mouse_angle = degrees(mouse_angle)

    return mouse_angle

color = (200, 100, 70)
original_surface = pygame.image.load(join(GAME_ROOT, 'images', 'gun', 'pistol', '0.png')).convert_alpha()

surface = original_surface.copy()
rect = original_surface.get_frect(center = (250, 250))
# surface.set_alpha(145)
running = True
while running:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    mouse_angle = get_angle((250, 250))
    surface = pygame.transform.rotate(original_surface, mouse_angle)
    rect = surface.get_frect(center = (250, 250))

    screen.fill((0,0,0))
    screen.blit(surface, rect)
    pygame.display.update()

pygame.quit()