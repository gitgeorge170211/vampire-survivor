from settings import *

class AllGroups(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.target_pos = pygame.math.Vector2()

    def draw(self, target_pos):
        self.target_pos.x = -(target_pos[0] - WINDOW_WIDTH/2)
        self.target_pos.y = -(target_pos[1] - WINDOW_WIDTH/2)
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + pygame.Vector2(self.target_pos))