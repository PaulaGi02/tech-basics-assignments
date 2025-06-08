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
def draw_game_over():
    overlay = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))
    screen.blit(overlay, (0, 0))
    go_txt1 = TITLE_FONT.render("Game Over!", True, WHITE)
    go_txt2 = INSTR_FONT.render("Press SPACE or click START to play again.", True, WHITE)
    screen.blit(go_txt1, (OFFSET+20, SCREEN_SIZE//2 - 80))
    screen.blit(go_txt2, (OFFSET-10, SCREEN_SIZE//2 - 24))

class Game:
    def __init__(self):
        self.duck = Duck()
        self.duckling = Duckling(self.duck.body)
        self._state = "INSTRUCTION"
        self._button_rect = pygame.Rect(
            SCREEN_SIZE // 2 - 80, SCREEN_SIZE // 2 + 40, 160, 48)

    def draw(self):
        self.duck.draw()
        self.duckling.draw()

    def update(self):
        if self._state == "RUNNING":
            self.duck.update()
            self._check_collisions()

    def _check_collisions(self):
        if self.duck.body[0] == self.duckling.pos:
            self.duck.grow()
            self.duck.score += 1
            self.duckling.reset_position(self.duck.body)

        if self.duck.body[0] in self.duck.body[1:]:
            self._game_over()

        x, y = self.duck.body[0]
        if x < 0 or y < 0 or x >= NUM_CELLS or y >= NUM_CELLS:
            self._game_over()

    def _game_over(self):
        self.duck.reset()
        self.duckling.reset_position(self.duck.body)
        self._state = "STOPPED"

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, v):
        self._state = v

    @property
    def button_rect(self):
        return self._button_rect

    def draw_instruction_screen(self):
        screen.fill(GREEN)
        # Title
        start_title_surface = TITLE_FONT.render("Duck Parade", True, DARK_GREEN)
        screen.blit(start_title_surface, (OFFSET, OFFSET - 40))
        # Instructions
        instr_lines = [
            "Help the duck parade collect as many other ducks as possible!",
            "Use the arrow keys to move the duck.",
            "Avoid crashing into the edges or yourself.",
            "",
            "Click the yellow button below or press SPACE to start!"
        ]
        for idx, line in enumerate(instr_lines):
            instr_surf = INSTR_FONT.render(line, True, DARK_GREEN)
            screen.blit(instr_surf, (OFFSET, OFFSET + 60 + idx * 36))
        # Start Button
        pygame.draw.rect(screen, BUTTON_COLOR, self._button_rect)
        start_btn_txt = INSTR_FONT.render("START", True, DARK_GREEN)
        start_txt_rect = start_btn_txt.get_rect(center=self._button_rect.center)
        screen.blit(start_btn_txt, start_txt_rect)

#Game loop
game = Game()
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 170)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game.state == "INSTRUCTION":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.button_rect.collidepoint(event.pos):
                    game.state = "RUNNING"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.state = "RUNNING"

        elif game.state == "RUNNING":
            if event.type == SNAKE_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.duck.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    game.duck.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    game.duck.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    game.duck.direction = Vector2(1, 0)

        elif game.state == "STOPPED":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.button_rect.collidepoint(event.pos):
                    game.state = "RUNNING"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.state = "RUNNING"

    #Drawing
    screen.fill(GREEN)
    pygame.draw.rect(screen, DARK_GREEN,
                     (OFFSET - 5, OFFSET - 5,
                      CELL_SIZE * NUM_CELLS + 10,
                      CELL_SIZE * NUM_CELLS + 10), 6)

    if game.state == "INSTRUCTION":
        game.draw_instruction_screen()
    else:
        game.draw()
        # UI Text
        title_surface = TITLE_FONT.render("Duck Parade", True, DARK_GREEN)
        score_surface = SCORE_FONT.render(f"Score: {game.duck.score}", True, DARK_GREEN)
        screen.blit(title_surface, (OFFSET - 5, 20))
        screen.blit(score_surface, (OFFSET - 5, OFFSET + CELL_SIZE * NUM_CELLS + 14))
        if game.state == "STOPPED":
            draw_game_over()
            # Draw start button on top
            pygame.draw.rect(screen, BUTTON_COLOR, game.button_rect)
            stopped_btn_txt = INSTR_FONT.render("START", True, DARK_GREEN)
            stopped_txt_rect = stopped_btn_txt.get_rect(center = game.button_rect.center)
            screen.blit(stopped_btn_txt, stopped_txt_rect)

    pygame.display.update()
    clock.tick(60)
