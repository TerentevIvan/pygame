import pygame


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

        self.keys: tuple[bool, ...] = ()

        self.main_loop()

    def main_loop(self):
        while self.running:
            self.delta_time = self.clock.tick(self.fps_target) / 1000

            self.event_loop()
            self.get_input()
            self.draw_calls()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # custom events

    def get_input(self):
        self.keys = pygame.key.get_pressed()

    def draw_calls(self):
        pygame.display.set_caption(f"{self.title} - {self.clock.get_fps()}")

        self.main_surface.fill('black')

        # draw all sprites
        # all_sprites.draw(display_surface)

        # draw all texts
        # display_surface.blit(text_surf, (0, 0))

        # draw all extra
        # pygame.draw.aacircle(display_surface, 'red', (500, 500), 50, 5)

        pygame.display.update()


if __name__ == '__main__':
    try:
        Game()
    except KeyboardInterrupt:
        pass
    finally:
        pass
