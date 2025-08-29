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
        max_hp: float | None,
        hp: float | None,
        max_speed: float | None,
        mass: float | None,
        volume: float | None,
        entity_type: tuple[str, ...] = ('neutral', 'enemy', 'friendly'),
        is_alive: bool = True

    ) -> None:

        super().__init__(
            entity_name,
            entity_id,
            groups,
            img_path,
            start_pos_x,
            start_pos_y,
            collidable,
            max_hp,
            hp,
            max_speed,
            mass,
            volume
        )

        self.entity_type = entity_type
        self.is_alive = is_alive

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



