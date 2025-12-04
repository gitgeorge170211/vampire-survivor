from settings import *

class AllGroups(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.sprite_list = list(self)
        self.sprite_list = sorted(self.sprite_list, key = lambda x: x.rect.y, reverse = True)
    def draw(self, target_pos):
        self.offset.x = target_pos[0] - WINDOW_WIDTH / 2
        self.offset.y = target_pos[1] - WINDOW_HEIGHT / 2
        for sprite in self.sprite_list:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)