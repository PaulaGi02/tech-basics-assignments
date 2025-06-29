import pygame
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

# Create surface
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((135, 206, 250))

# Load and scale images
basket_img = pygame.image.load("baskett.png").convert_alpha()
good_object_img = pygame.image.load("apple.png").convert_alpha()
bad_object_img = pygame.image.load("bomb.png").convert_alpha()
basket_img = pygame.transform.scale(basket_img, (50, 50)).convert_alpha()

basket_img = pygame.transform.scale(basket_img, (100, 50))
good_object_img = pygame.transform.scale(good_object_img, (40, 40))
bad_object_img = pygame.transform.scale(bad_object_img, (40, 40))

# Load sounds
catch_sound = pygame.mixer.Sound("bloop_x.wav")
boom_sound = pygame.mixer.Sound("boom_x.wav")

# Basket
basket_rect = basket_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 30))
basket_speed = 8

# Game variables
falling_objects = []
SPAWN_EVENT = pygame.USEREVENT + 1
initial_spawn_rate = 1000
pygame.time.set_timer(SPAWN_EVENT, initial_spawn_rate)

score = 0
lives = 3
level = 1
font = pygame.font.SysFont(None, 36)
running = True

# Falling object
class FallingObject:
    def __init__(self, x, y, is_good, speed_bonus=0):
        self.is_good = is_good
        self.image = good_object_img if is_good else bad_object_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(4, 8) + speed_bonus

    def update(self):
        self.rect.move_ip(0, self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def start_screen():
    waiting = True
    while waiting:
        screen.fill((135, 206, 250))  # same sky blue background

        title_font = pygame.font.SysFont(None, 60)
        instruction_font = pygame.font.SysFont(None, 36)

        title_surf = title_font.render("Catch the Falling Objects", True, (0, 0, 0))
        instruction_surf1 = instruction_font.render("Move basket with LEFT and RIGHT arrows", True, (0, 0, 0))
        instruction_surf2 = instruction_font.render("Catch the apples, avoid the bombs!", True, (0, 0, 0))
        instruction_surf3 = instruction_font.render("Press SPACE to start", True, (0, 0, 0))

        screen.blit(title_surf, title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 4)))
        screen.blit(instruction_surf1, instruction_surf1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(instruction_surf2, instruction_surf2.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        screen.blit(instruction_surf3, instruction_surf3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
start_screen()

# Game loop
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_EVENT:
            x = random.randint(20, WIDTH - 60)
            is_good = random.choice([True, False, True])
            falling_objects.append(FallingObject(x, 0, is_good, speed_bonus=level))

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_rect.x -= basket_speed
    if keys[pygame.K_RIGHT]:
        basket_rect.x += basket_speed

    basket_rect.clamp_ip(screen.get_rect())

    inflated_basket = basket_rect.inflate(-10, -10)

    # Update and draw falling objects
    for obj in falling_objects[:]:
        obj.update()
        obj.draw(screen)

        if inflated_basket.colliderect(obj.rect):
            if obj.is_good:
                score += 1
                catch_sound.play()
            else:
                lives -= 1
                boom_sound.play()
            falling_objects.remove(obj)

        elif not screen.get_rect().contains(obj.rect):
            falling_objects.remove(obj)

    # Difficulty scaling every 10 points
    new_level = score // 10 + 1
    if new_level != level:
        level = new_level
        new_spawn_rate = max(300, initial_spawn_rate - level * 80)
        pygame.time.set_timer(SPAWN_EVENT, new_spawn_rate)

    # Draw basket
    screen.blit(basket_img, basket_rect)

    # Draw UI
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    level_text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 120, 10))
    screen.blit(level_text, (WIDTH // 2 - 40, 10))

    # Game over
    if lives <= 0:
        game_over_text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
