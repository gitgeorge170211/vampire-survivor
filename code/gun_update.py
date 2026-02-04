from settings import *
from sprites import Bullet

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, all_sprites, screen, groups):
        super().__init__(groups)
        self.original_image = pygame.image.load(join(GAME_ROOT, "images", "gun", "pistol", "0.png")).convert_alpha()
        self.original_image = pygame.transform.scale_by(self.original_image, 0.9)
        self.image = self.original_image #temporary 
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)) #temporary
        self.player = player
        self.all_sprites = all_sprites
        self.screen = screen
        self.shooting_sound = pygame.mixer.Sound(join(GAME_ROOT, "audio", "shoot.wav"))
        self.shooting_sound.set_volume(0.4)
        self.fov = 150 # field of view
        self.gun_offset = (17.0, 34.0)
        #self.gun_offset = [(17.0, 34.0),(40.0, 82.0)]
        self.player_angles = {"left":180, "right":0, "up":90, "down":270}
        self.shooting_state = False
        self.gun_movement_cooldown = 220
        self.shooting_cooldown = 250

    def get_angle(self, hand_pos):
        mouse_pos = pygame.mouse.get_pos()

        dx = (mouse_pos[0] - hand_pos[0])
        dy = (mouse_pos[1] - hand_pos[1])
        mouse_angle = atan2(dx, dy)
        mouse_angle = degrees(mouse_angle)

        return mouse_angle

    # def place_gun(self, mouse_angle):

    #     # calculation of the position where the gun is placed on the player's hand
    #     self.hand_offset = self.player.hand_offsets[self.player.state][int(self.player.frame_index) % len(self.player.frames[self.player.state])]
    #     hand_pos = pygame.math.Vector2(self.player.rect.topleft) + pygame.math.Vector2(self.hand_offset)
    #     image_topleft = hand_pos - pygame.math.Vector2((self.gun_offset[0], self.gun_offset[1]))
        
    #     return image_topleft

    def update(self, dt):
        if pygame.mouse.get_just_pressed()[0]:
            # calculation of the position where the gun is placed on the player's hand
            self.hand_offset = self.player.hand_offsets[self.player.state][int(self.player.frame_index) % len(self.player.frames[self.player.state])]
            hand_pos = pygame.math.Vector2(self.player.rect.topleft) + pygame.math.Vector2(self.hand_offset)
            image_topleft = hand_pos - pygame.math.Vector2((self.gun_offset[0], self.gun_offset[1]))
            # image rotation
            mouse_angle = self.get_angle(hand_pos)
            self.image = pygame.transform.rotate(self.original_image, mouse_angle)
            self.rect = self.image.get_frect(topleft = (image_topleft))
        
        else:
            self.hand_offset = self.player.hand_offsets[self.player.state][int(self.player.frame_index) % len(self.player.frames[self.player.state])]
            hand_pos = pygame.math.Vector2(self.player.rect.topleft) + pygame.math.Vector2(self.hand_offset)
            image_topleft = hand_pos - pygame.math.Vector2((self.gun_offset[0], self.gun_offset[1]))

            self.image = self.original_image
            self.rect = self.image.get_frect(topleft = (image_topleft))

        

            
                    