import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Scream Bouncing')
clock = pygame.time.Clock()
FPS = 60

class Screams:
    def __init__(self):
        self.images = [
            pygame.transform.scale(pygame.image.load('scream1.jpg'), (167, 200)),
            pygame.transform.scale(pygame.image.load('scream2.jpg'), (162, 164)),
            pygame.transform.scale(pygame.image.load('scream3.jpg'), (175, 200)),
            pygame.transform.scale(pygame.image.load('scream4.jpg'), (162, 162))
        ]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed_x = random.choice([-1, 1]) * random.randint(3, 6)
        self.speed_y = random.choice([-1, 1]) * random.randint(3, 6)
        self.bounce_count = 0  # New: Track bounces

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0:
            self.rect.left = -self.rect.left
            self.speed_x *= -1
            self.change_image()

        elif self.rect.right > WIDTH:
            overflow = self.rect.right - WIDTH
            self.rect.right = WIDTH - overflow
            self.speed_x *= -1
            self.change_image()

        if self.rect.top < 0:
            self.rect.top = -self.rect.top
            self.speed_y *= -1
            self.change_image()

        elif self.rect.bottom > HEIGHT:
            overflow = self.rect.bottom - HEIGHT
            self.rect.bottom = HEIGHT - overflow
            self.speed_y *= -1
            self.change_image()

    def change_image(self):
        self.bounce_count += 1

        self.image = random.choice(self.images)
        if self.bounce_count % 3 == 0:
            angle = random.choice([90, 180, 270])
            self.image = pygame.transform.rotate(self.image, angle)

        # Recalculate rect and maintain current position
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)

        # Change speed
        self.speed_x = random.choice([-1, 1]) * random.randint(3, 6)
        self.speed_y = random.choice([-1, 1]) * random.randint(3, 6)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Main game loop
scream = Screams()
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scream.update()

    screen.fill((255, 255, 255))
    scream.draw(screen)

    pygame.display.flip()

pygame.quit()
