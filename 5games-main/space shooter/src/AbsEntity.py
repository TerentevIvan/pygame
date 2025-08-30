import pygame
from pygame import Vector2


class AbsEntity(pygame.sprite.Sprite):
    def __init__(
        self,
        entity_name: str,
        entity_id: int,
        groups: tuple[pygame.sprite.AbstractGroup],
        img_path: str,
        start_pos_x: float,
        start_pos_y: float,
        collidable: bool
    ) -> None:

        super().__init__(groups)

        self.entity_name = entity_name
        self.entity_id = entity_id

        self.image = pygame.image.load(img_path).convert_alpha()
        self.rectangle = self.image.get_frect(center=(start_pos_x, start_pos_y))

        self.facing_vector2: Vector2 = pygame.math.Vector2(start_pos_x, start_pos_y)
        self.collidable = collidable
