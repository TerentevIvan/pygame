from settings import *


class Game:
    def __init__(
        self,
        window_width: int = 1280,
        window_height: int = 720,
        title: str = 'my_game',
        fps_target: int = 60
    ) -> None:

        pygame.init()

        self.clock = pygame.time.Clock()
        self.delta_time: float = 0.0

        self.window_width = window_width
        self.window_height = window_height
        self.title = title
        self.fps_target = fps_target

        self.main_surface = pygame.display.set_mode((self.window_width, self.window_height))

        self.running: bool = True
        self.groups()



    def main_loop(self) -> None:
        while self.running:
            self.delta_time = self.clock.tick(self.fps_target) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == meteor_event:
                x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)
                # Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))

    def groups(self):
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

    def update(self, dtime):
        pass




if __name__ == '__main__':
    game: Game = Game()
    game.run()

