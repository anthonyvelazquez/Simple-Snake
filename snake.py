import pygame
import random

SCREENX = 800
SCREENY = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SnakeBlockWidth = 15
SnakeBlockHeight = 15
SnakeBlockSpacing = 3
WindowPadding = 30
 
x_change = SnakeBlockWidth + SnakeBlockSpacing
y_change = 0

def GenerateAppleLocation():
    return random.randrange(0, SCREENX - WindowPadding, SnakeBlockWidth) + SnakeBlockSpacing, random.randrange(0, SCREENY - WindowPadding, SnakeBlockHeight) + 3

def AppleCollision(SnakeBody, Apple):
    if SnakeBody[0].rect.colliderect(Apple.rect):
        return True
    else:
        return False


class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y, snake):
        super().__init__()
        self.image = pygame.Surface([SnakeBlockWidth, SnakeBlockHeight])
        if snake: 
            self.image.fill(WHITE)
        else:
            self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
pygame.init()
screen = pygame.display.set_mode([SCREENX, SCREENY])
pygame.display.set_caption('Simple Snake Example')
 
SnakeSpriteGroup = pygame.sprite.Group()
AppleSpriteGroup = pygame.sprite.Group()
 
SnakeBodySegments = []
for i in range(3):
    x = 250 - (SnakeBlockWidth + SnakeBlockSpacing) * i
    y = 30
    segment = Segment(x, y, True)
    SnakeBodySegments.append(segment)
    SnakeSpriteGroup.add(segment)
 
clock = pygame.time.Clock()
done = False

AppleX, AppleY = GenerateAppleLocation()
AppleSegment = Segment(AppleX, AppleY, False)
AppleSpriteGroup.add(AppleSegment)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (SnakeBlockWidth + SnakeBlockSpacing) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (SnakeBlockWidth + SnakeBlockSpacing)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (SnakeBlockHeight + SnakeBlockSpacing) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (SnakeBlockHeight + SnakeBlockSpacing)
 
    SnakeX = SnakeBodySegments[0].rect.x + x_change
    SnakeY = SnakeBodySegments[0].rect.y + y_change
    segment = Segment(SnakeX, SnakeY, True)

    if not AppleCollision(SnakeBodySegments, AppleSegment):
        old_segment = SnakeBodySegments.pop()
        SnakeSpriteGroup.remove(old_segment)
    else:
        AppleX, AppleY = GenerateAppleLocation()
        AppleSegment = Segment(AppleX, AppleY, False)
        AppleSpriteGroup.empty()
        AppleSpriteGroup.add(AppleSegment)
 
    SnakeBodySegments.insert(0, segment)
    SnakeSpriteGroup.add(segment)
 
    screen.fill(BLACK)
 
    SnakeSpriteGroup.draw(screen)
    AppleSpriteGroup.draw(screen)
    pygame.display.flip()
 
    clock.tick(5)
 
pygame.quit()