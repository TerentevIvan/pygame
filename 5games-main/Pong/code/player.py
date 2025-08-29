from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # setup
        self.surf = pygame.Surface((20, 80))
        self.surf.fill('red')
        self.rect = self.surf.get_frect(center=pos)

        # movment
        self.direction = pygame.Vector2()
        self.speed = 200

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])

        self.direction = self.direction.normalize() if self.direction else self.direction
        print(self.direction)

    def move(self, dt):
        self.rect.y += self.direction.x * self.speed * dt
        #self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        #self.collision('vertical')

    def update(self, dt):
        self.input()
        self.move(dt)
