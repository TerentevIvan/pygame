import pygame

from Entity import Entity


class NPC(Entity):
    def __init__(
        self,
        entity_name: str,
        entity_id: int,
        groups: tuple[pygame.sprite.AbstractGroup],
        img_path: str,
        start_pos_x: float,
        start_pos_y: float,
        collidable: bool,
        hp: float | None = None,
        max_speed: float | None = None,
        mass: float | None = None,
        volume: float | None = None
    ) -> None:

        super().__init__(
            entity_name,
            entity_id,
            groups,
            img_path,
            start_pos_x,
            start_pos_y,
            collidable
        )

        self.hp = hp
        self.max_speed = max_speed
        self.mass = mass
        self.volume = volume
