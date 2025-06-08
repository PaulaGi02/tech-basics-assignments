import pygame
import sys
import random
from pygame.math import Vector2

pygame.init()

TITLE_FONT = pygame.font.Font(None, 72)
SCORE_FONT = pygame.font.Font(None, 48)
INSTR_FONT = pygame.font.Font(None, 32)
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
WHITE = (255, 255, 255)
BUTTON_COLOR = (255, 215, 0)

CELL_SIZE = 44
NUM_CELLS = 14
OFFSET = 75
SCREEN_SIZE = 2 * OFFSET + CELL_SIZE * NUM_CELLS
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Duck Parade")
clock = pygame.time.Clock()

# images
duck_img = pygame.image.load("duck.png").convert_alpha()
duck_img = pygame.transform.scale(duck_img, (CELL_SIZE, CELL_SIZE))
# Entity Class
class Entity:
    def __init__(self, position):
        self._position = Vector2(position)

    @property
    def pos(self) -> Vector2:
        return self._position

    @pos.setter
    def pos(self, pos: Vector2) -> None:
        self._position = Vector2(pos)
#subclass
class Duckling(Entity):
    def __init__(self, snake_body):
        super().__init__(self._generate_random_pos(snake_body))

    def draw(self):
        rect = pygame.Rect(
            OFFSET + self._position.x * CELL_SIZE,
            OFFSET + self._position.y * CELL_SIZE,
            CELL_SIZE, CELL_SIZE)
        screen.blit(duck_img, rect)

    @staticmethod
    def _generate_random_cell():
        return Vector2(random.randint(0, NUM_CELLS - 1),
                       random.randint(0, NUM_CELLS - 1))

    def _generate_random_pos(self, snake_body):
        pos = self._generate_random_cell()
        while pos in snake_body:
            pos = self._generate_random_cell()
        return pos

    def reset_position(self, snake_body):
        self.pos = self._generate_random_pos(snake_body)

class Duck(Entity):
    def __init__(self):
        super().__init__((6, 7))
        self._body = [Vector2(6, 7), Vector2(5, 7), Vector2(4, 7)]
        self._direction = Vector2(1, 0)
        self._add_segment = False
        self._score = 0

    @property
    def body(self) -> list:
        return self._body

    @body.setter
    def body(self, body: list) -> None:
        self._body = body

    @property
    def direction(self) -> Vector2:
        return self._direction

    @direction.setter
    def direction(self, new_dir: Vector2) -> None:
        if new_dir + self._direction != Vector2(0, 0):
            self._direction = new_dir

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        self._score = value

    def draw(self):
        for i, segment in enumerate(self._body):
            rect = (OFFSET + segment.x * CELL_SIZE, OFFSET + segment.y * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE)
            if i == 0:
                screen.blit(duck_img, rect)
            else:
                screen.blit(duck_img, rect)

    def update(self):
        self._body.insert(0, self._body[0] + self._direction)
        if not self._add_segment:
            self._body.pop()
        else:
            self._add_segment = False

    def grow(self):
        self._add_segment = True

    def reset(self):
        self._body = [Vector2(6, 7), Vector2(5, 7), Vector2(4, 7)]
        self._direction = Vector2(1, 0)
        self._add_segment = False
        self._score = 0

#Game class
class Game:
    pass

#Game loop
game = Game()
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 170)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Drawing
    screen.fill(GREEN)
    pygame.draw.rect(screen, DARK_GREEN,
                        (OFFSET - 5, OFFSET - 5,
                        CELL_SIZE * NUM_CELLS + 10,
                        CELL_SIZE * NUM_CELLS + 10), 6)

    pygame.display.update()
    clock.tick(60)
