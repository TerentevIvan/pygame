import pygame

from AbsEntity import AbsEntity


class Entity(AbsEntity):
    def __init__(
        self,
        entity_name: str,
        entity_id: int,
        groups: tuple[pygame.sprite.AbstractGroup],
        img_path: str,
        start_pos_x: float,
        start_pos_y: float,
        collidable: bool,
        max_hp: float | None = None,
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

        self.facing_vector2 = self.facing_vector2
        self.max_hp = max_hp
        self.hp = hp
        self.max_speed = max_speed
        self.mass = mass
        self.volume = volume

    def movements(self):
        pass

    def collision(self):
        pass

    def animation(self, delta_time):
        pass

    def update(self, delta_time):
        self.movements()
        self.collision()
        self.animation(delta_time)
