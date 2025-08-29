from settings import *


class Entity(pygame.sprite.Sprite):
    def __init__(
            self,
            groups: tuple[pygame.sprite.AbstractGroup],
            imge_path: str,
            pos_x: float = WINDOW_WIDTH / 2,
            pos_y: float = WINDOW_HEIGHT / 2

    ) -> None:
        super().__init__(groups)
        self.image = folder_importer(imge_path)
        self.rect = self.image.get_frect(center=(pos_x, pos_y))
        self.direction: list[float] = pygame.math.Vector2()
        self.speed: float = 300


class Player(Entity):
    def keys_update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
