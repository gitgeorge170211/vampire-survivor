from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)

class Bullet(pygame.sprite.Sprite):
    pass

# class Line(pygame.sprite.Sprite):
#     def __init__(self, starting_point, screen, groups):
#         super().__init__(groups) # fix
#         self.image = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
#         line_color = (255, 255, 255, 128)  # white, 50% alpha
#         end_point = pygame.math.Vector2(starting_point) *  5
#         pygame.draw.aaline(self.image, line_color, starting_point, (end_point[0], end_point[1]), width=2)
#         self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    def update(self, dt):
        self.kill()
