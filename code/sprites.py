from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, is_background=False):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.is_background = is_background

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, is_background=False):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.is_background = is_background
