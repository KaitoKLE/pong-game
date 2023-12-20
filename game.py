import time

import pygame

from character import Player, Ball, AIPlayer
from display import Display, CIRC, RECT

PADDLE_SIZE = (15, 100)

FRAME_RATE = 60


class Game:
    def __init__(self):
        pygame.init()
        self.__display = Display(self)
        self.__active_keys = set()
        self.__clock = pygame.time.Clock()
        self.__running = True
        self.__ball = Ball((self.__display.size[0] / 2, self.__display.size[1] / 2), 10, CIRC)
        self.__player = Player([0, self.__display.size[1] * 0.4], PADDLE_SIZE, RECT)
        self.__ai_player = AIPlayer(
            [self.__display.size[0] - 15, self.__display.size[1] * 0.4], PADDLE_SIZE, RECT, self.__ball
        )
        self.__b_music = pygame.mixer.Sound('bgmusic.ogg')
        self.__bounce_sound = pygame.mixer.Sound('bounce.ogg')
        self.playing = False
        self.round = 1
        self.scores = [0, 0]

    def loop(self):
        self.__b_music.play(-1)
        while self.__running:
            self.events()
            self.update()
            self.__display.draw()
            self.__clock.tick(FRAME_RATE)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            if event.type == pygame.KEYDOWN:
                self.__active_keys.add(event.key)
            if event.type == pygame.KEYUP:
                self.__active_keys.discard(event.key)
        self.key_events()

    def update(self):
        if self.playing:
            self.__player.move()
            self.__ai_player.move()
            self.__player.constraint(self.__display.size)
            self.__ai_player.constraint(self.__display.size)
            self.__ball.move()
            self.__ball.constraint(self.__display.size)
            if self.ball_out():
                self.new_round()
            self.detect_collisions()

    def key_events(self):
        if pygame.K_UP in self.__active_keys:
            self.__player.dy = -self.__player.move_speed
        elif pygame.K_DOWN in self.__active_keys:
            self.__player.dy = self.__player.move_speed
        elif pygame.K_SPACE in self.__active_keys and not self.playing:
            self.__ball.random_move()
            self.playing = True
        else:
            self.__player.dy = 0

    def ball_out(self):
        if self.__ball.x > self.__display.size[0] + self.__ball.size:
            self.scores[0] += 1
            return True
        if self.__ball.x < 0 - self.__ball.size:
            self.scores[1] += 1
            return True

    def new_round(self):
        if self.round == 3:
            self.game_over()
        else:
            self.__ball.x = self.__display.size[0] / 2
            self.__ball.y = self.__display.size[1] / 2
            self.__ball.random_move()
            self.round += 1

    def game_over(self):
        self.playing = False
        self.round = 1
        self.scores = [0, 0]
        self.__ball.restart()
        self.__ai_player.restart()
        self.__player.restart()

    def detect_collisions(self):
        player1 = pygame.Rect(self.__player.x + self.__player.size[0], self.__player.y, self.__player.size[0],
                              self.__player.size[1])
        ai_player = pygame.Rect(self.__ai_player.x, self.__ai_player.y, self.__ai_player.size[0],
                                self.__ai_player.size[1])
        ball = pygame.Rect(self.__ball.x, self.__ball.y, self.__ball.size, self.__ball.size)
        if ball.colliderect(player1) or ball.colliderect(ai_player):
            self.__ball.dx = -self.__ball.dx
            self.__bounce_sound.play()

    def get_objects_to_draw(self):
        return self.__player, self.__ai_player, self.__ball


# ----------------------------------------------------------------------------------------------------------------------
Game().loop()
