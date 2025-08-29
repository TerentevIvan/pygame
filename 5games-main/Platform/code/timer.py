from settings import *


class Timer:
    def __init__(self, duration, func = None, repeat = None, autostert = False):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.func = func
        self.repeat = repeat

        if autostert:
            self.activate()

    def __bool__(self):
        return self.active

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def update(self):
        if pygame.time.get_ticks() - self.start_time >= self.duration:
            if self.func and self.start_time != 0:
                self.func()
            self.deactivate()
