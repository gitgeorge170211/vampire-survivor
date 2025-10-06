from settings import *

class AllGroups(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def draw(self, offset):
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + pygame.Vector2(offset))