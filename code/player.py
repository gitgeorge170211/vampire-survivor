from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        # self.load_files()
        self.frames = self.load_files()
        self.image = self.frames["down"][0]
        self.rect = self.image.get_frect(center = pos)
        self.dir = pygame.math.Vector2()
        self.speed = 250

        self.collision_sprites = collision_sprites
        self.hitbox_rect = pygame.FRect((0, 0), (60, 40))
        self.hitbox_rect.midbottom = pos
        self.state, self.frame_index, self.frame_change = "down", 0, 5
        self.weapon = None
        self.hand_offsets = {
                            'down': [(88.0, 89.0), (83.0, 94.0), (88.0, 89.0), (87.0, 89.0)],
                            'up': [(39.0, 90.0), (39.0, 89.0), (39.0, 89.0), (43.0, 92.0)],
                            'right': [(73.0, 90.0), (69.0, 90.0), (75.0, 90.0), (76.0, 87.0)],
                            'left': [(77.0, 90.0), (71.0, 89.0), (80.0, 89.0), (84.0, 89.0)]
                            }
        
    def set_weapon(self, weapon_obj):
        self.weapon = weapon_obj

    def find_angle(self):
        mouse_pos = pygame.mouse.get_pos()
        self.hand_offset = self.hand_offsets[self.player.state][int(self.player.frame_index) % len(self.player.frames[self.player.state])]
        hand_pos = pygame.math.Vector2(self.player.rect.topleft) + pygame.math.Vector2(self.hand_offset)

        dx = (mouse_pos[0] - hand_pos[0])
        dy = (mouse_pos[1] - hand_pos[1])
        mouse_angle = atan2(dx, dy)
        mouse_angle = degrees(mouse_angle)
            
        return mouse_angle

    def turn_to_shoot(self):
        pass

    def load_files(self):
        self.frames = {"left":[], "right":[], "up":[], "down":[]}
        for state in self.frames.keys():
            for folder_path, subfolders, file_names in walk(join(GAME_ROOT, "images", "player", state)):
                for file_name in sorted(file_names, key = lambda name: int(name.split(".")[0])):
                    full_path = join(folder_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.frames[state].append(surf)
        return self.frames

    def animate(self, dt):
        if self.dir.x != 0:
            self.state = "right" if self.dir.x > 0 else "left"
        if self.dir.y != 0:
            self.state = "down" if self.dir.y > 0 else "up"

        if self.dir.x or self.dir.y:
            self.frame_index += self.frame_change * dt
        else:
             self.frame_index = 0

        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]
        self.rect = self.image.get_frect(midbottom = self.hitbox_rect.midbottom)

    def input(self):
        keys = pygame.key.get_pressed()
        self.dir.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.dir.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.dir = self.dir.normalize() if self.dir else self.dir

    def move(self, dt):
        self.hitbox_rect.x += self.dir.x * self.speed * dt
        self.collision("horizontal")
        self.hitbox_rect.y += self.dir.y * self.speed * dt
        self.collision("vertical")

    def update(self, dt):
        # if self.weapon.shoot_time != None:
        #     current_time = pygame.time.get_ticks()
        #     if (current_time - self.weapon.shoot_time) < self.weapon.gun_movement_cooldown:
        #         return
                
        self.input()
        self.move(dt)
        self.animate(dt)
        
    def collision(self, axis: str):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if axis == "horizontal":
                    if self.dir.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.dir.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.dir.y > 0: self.hitbox_rect.bottom = sprite.rect.top
                    if self.dir.y < 0: self.hitbox_rect.top = sprite.rect.bottom

