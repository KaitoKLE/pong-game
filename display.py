import pygame

# DISPLAY SETTINGS
SCREEN_SIZE = (900, 600)

# BASE COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
R = (
    (255, 255, 255),
    (200, 200, 200),
    (150, 150, 150),
    (100, 100, 100),
    (50, 50, 50),
)

# SHAPES
RECT = 1
CIRC = 2


class Display:
    def __init__(self, game):
        self.game = game
        self.size = SCREEN_SIZE
        pygame.display.set_caption('Pong Game')
        self.font = pygame.font.Font('cour.ttf', 64)
        self.scores = self.font.render(f'0 - 0', True, WHITE)
        self.canvas = pygame.display.set_mode(self.size)

    def draw(self):
        objs = self.game.get_objects_to_draw()
        self.canvas.fill(BLACK)
        pygame.draw.line(self.canvas, GRAY, (self.size[0] * 0.5, 0), (self.size[0] * 0.5, self.size[1]))
        pygame.draw.circle(self.canvas, GRAY, (self.size[0] / 2, self.size[1] / 2), 100, 1)
        for obj in objs:
            if obj.shape == CIRC:
                pygame.draw.circle(self.canvas, RED, (obj.x, obj.y), obj.size)
            elif obj.shape == RECT:
                pygame.draw.rect(self.canvas, WHITE, (obj.x, obj.y, obj.size[0], obj.size[1]))
        if self.game.playing:
            self.scores = self.font.render(f'{self.game.scores[0]} {self.game.scores[1]}', True, WHITE)
            self.canvas.blit(
                self.scores,
                (self.size[0] / 2 - self.scores.get_size()[0] / 2, 0)
            )
        else:
            self.scores = self.font.render('press SPACE to start!', True, WHITE)
            self.canvas.blit(
                self.scores,
                (self.size[0] / 2 - self.scores.get_size()[0] / 2, self.size[1] - self.scores.get_size()[1])
            )
        pygame.display.flip()
