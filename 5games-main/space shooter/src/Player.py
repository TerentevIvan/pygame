import pygame

from NPC import NPC


class Player(NPC):
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
        entity_type: tuple[str, ...],
        is_alive: bool,
        attack_cooldown: float = 200.0,
        can_attack: bool = True

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
            volume,
            entity_type,
            is_alive
        )

        self.attack_cooldown = attack_cooldown
        self.can_attack = can_attack

    def movements(self):
        pass

    def attack(self):
        pass

    def collision(self):
        pass

    def input(self, delta_time):
        keys = pygame.key.get_pressed()
        self.facing_vector2.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.facing_vector2.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.facing_vector2 = self.facing_vector2.normalize() if self.facing_vector2 else self.facing_vector2
        self.rect.center += self.facing_vector2 * self.max_speed * delta_time

    def animation(self, delta_time):
        pass

    def update(self, delta_time):
        self.movements()
        self.attack()
        self.collision()
        self.input(delta_time)
        self.animation(delta_time)



