from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame

from random import randint

class Game():

    def __init__(self):
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("survivor")
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        # sprites
        self.player = Player((500,300), self.all_sprites, self.collision_sprites)

    def setup(self):
        map = load_pygame(join("data", "maps", "world.tmx"))

        for x, y, image in map.get_layer_by_name("Ground").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name("Objects"):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

    def run(self):
        while self.running:
            self.dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update(self.dt)
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
