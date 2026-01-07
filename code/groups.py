from settings import *

class AllGroups(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def draw(self, target_pos):
        self.ground_sprites = [sprite for sprite in self if hasattr(sprite, "ground")]
        self.objects_sprites = sorted([sprite for sprite in self if not hasattr(sprite, "ground")], key=lambda x: x.rect.bottom)
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH/2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT/2)
        for layer in [self.ground_sprites, self.object_sprites]:
            for sprite in layer:
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)