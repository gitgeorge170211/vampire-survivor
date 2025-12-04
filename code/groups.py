from settings import *

class AllGroups(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def draw(self, target_pos):
        self.background_sprites = [sprite for sprite in list(self) if sprite.is_background]
        # nb is short for non-background
        self.nb_sprites = sorted([sprite for sprite in list(self) if not sprite.is_background], key=lambda x: x.rect.y, reverse=True)
        self.sprite_list = self.background_sprites + self.nb_sprites
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH/2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT/2)
        for sprite in self.sprite_list:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)