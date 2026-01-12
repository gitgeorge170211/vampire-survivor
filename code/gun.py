from settings import *
from sprites import Bullet, Line

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, all_sprites, screen, groups):
        super().__init__(groups)
        self.original_image = pygame.image.load(join(GAME_ROOT, "images", "gun", "pistol", "0.png")).convert_alpha()
        self.original_image = pygame.transform.scale_by(self.original_image, 0.9)
        self.player = player
        self.all_sprites = all_sprites
        self.screen = screen
        self.shooting_sound = pygame.mixer.Sound(join(GAME_ROOT, "audio", "shoot.wav"))
        self.shooting_sound.set_volume(0.4)
        self.fov = 150 # field of view
        self.gun_offset = (17.0, 34.0)
        #self.gun_offset = [(17.0, 34.0),(40.0, 82.0)]
        self.hand_offsets = {'down': [(88.0, 89.0), (83.0, 94.0), (88.0, 89.0), (87.0, 89.0)],
                                    'up': [(39.0, 90.0), (39.0, 89.0), (39.0, 89.0), (43.0, 92.0)],
                                    'right': [(73.0, 90.0), (69.0, 90.0), (75.0, 90.0), (76.0, 87.0)],
                                    'left': [(77.0, 90.0), (71.0, 89.0), (80.0, 89.0), (84.0, 89.0)]
                                    }
        self.player_angles = {"left":180, "right":0, "up":90, "down":270}
        self.shooting_state = False
        self.gun_movement_cooldown = 220
        self.shooting_cooldown = 250

    def update(self, dt):
        self.hand_offset = self.hand_offsets[self.player.state][int(self.player.frame_index) % len(self.player.frames[self.player.state])]
        hand_pos = pygame.math.Vector2(self.player.rect.topleft) + pygame.math.Vector2(self.hand_offset)

        if not self.shooting_state:
            player_angle = self.player_angles[self.player.state]
            mouse_pos = pygame.mouse.get_pos()
            mouse_angle = degrees(atan2(-(mouse_pos[1] - hand_pos[1]), mouse_pos[0] - hand_pos[0]))
            mouse_angle %= 360
            angle_dif = (player_angle - mouse_angle) % 360
            if angle_dif > 180:
                angle_dif = 360 - angle_dif

            if angle_dif <= self.fov / 2:
                #place gun
                self.image = pygame.transform.rotate(self.original_image, mouse_angle)
                image_topleft = hand_pos - pygame.math.Vector2((self.gun_offset[0], self.gun_offset[1]))
                self.rect = self.image.get_frect(topleft = (image_topleft))

                if pygame.mouse.get_just_pressed()[0]: 
                    self.shooting_state = True
                    self.shoot_time = pygame.time.get_ticks()
                    #create bullet
                    Bullet()
                    #play sound
                    self.shooting_sound.play()

                else:
                    Line(self.rect.topleft, self.screen, self.all_sprites)
                    # place indicating line


        else:
            current_time = pygame.time.get_ticks()
            if current_time >= self.shoot_time + self.shooting_cooldown:
                self.shooting_state = False

            
                    