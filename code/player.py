from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.dir = pygame.math.Vector2()
        self.speed = 250
        self.collision_sprites = collision_sprites
        self.hitbox_rect = self.rect.inflate(-60, 0)
        self.hitbox_rect.center = self.rect.center

    def update(self, dt):
        # input
        keys = pygame.key.get_pressed()
        self.dir.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.dir.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.dir = self.dir.normalize() if self.dir else self.dir

        # movement
        self.hitbox_rect.x += self.dir.x * self.speed * dt
        self.collision("horizontal")
        self.hitbox_rect.y += self.dir.y * self.speed * dt
        self.collision("vertical")
        self.rect.center = self.hitbox_rect.center

    def collision(self, axis: str):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if axis == "horizontal":
                    if self.dir.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.dir.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.dir.y > 0: self.hitbox_rect.bottom = sprite.rect.top
                    if self.dir.y < 0: self.hitbox_rect.top = sprite.rect.bottom