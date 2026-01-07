from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Bullet(pygame.sprite.Sprite):
    pass

class Line(pygame.sprite.Sprite):
    def __init__(self, starting_point, groups):
        super().__init__(groups) # fix
        self.image = pygame.Surface((600, 600), flags = pygame.SRCALPHA)
        end_point = pygame.math.Vector2(starting_point) *  5
        pygame.draw.aaline(self.image, "orange", starting_point, (end_point[0], end_point[1]))
        self.image.set_alpha(150)

    def update(self, dt):
        self.kill()
