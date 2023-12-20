import random


class Character:
    def __init__(self, pos, size, shape):
        self.__pos = list(pos)
        self.__init_pos = list(pos)
        self.size = size
        self.shape = shape
        self.dx = 0
        self.dy = 0

    @property
    def x(self):
        return self.__pos[0]

    @x.setter
    def x(self, new_x):
        self.__pos[0] = new_x

    @property
    def y(self):
        return self.__pos[1]

    @y.setter
    def y(self, new_y):
        self.__pos[1] = new_y

    def move(self):
        self.__pos[0] += self.dx
        self.__pos[1] += self.dy

    def restart(self):
        self.__pos = self.__init_pos

    def constraint(self, display_size):
        pass


class Player(Character):
    def __init__(self, pos, size, shape):
        super().__init__(pos, size, shape)
        self.move_speed = 5

    def constraint(self, display_size):
        if self.x > display_size[0] - self.size[0]:
            self.x = display_size[0] - self.size[0]
        if self.x < 0:
            self.x = 0
        if self.y > display_size[1] - self.size[1]:
            self.y = display_size[1] - self.size[1]
        if self.y < 0:
            self.y = 0


class AIPlayer(Player):
    def __init__(self, pos, size, shape, ball):
        super().__init__(pos, size, shape)
        self.ball = ball
        self.kp = 1

    def move(self):
        if self.ball:
            # Predict ball position
            ball_y = self.ball.y + self.ball.dy * self.estimate_ball_time()
            # Calculate desired movement
            self.dy = self.kp * (ball_y - self.y)
            # Limit speed
            self.dy = max(-self.move_speed, min(self.move_speed, self.dy))
        self.y += self.dy

    def estimate_ball_time(self):
        # Estimate time for ball to reach paddle
        dist_y = abs(self.y - self.ball.y)
        return dist_y / abs(self.ball.dy)


class Ball(Character):
    def __init__(self, pos, size, shape):
        super().__init__(pos, size, shape)
        self.move_speed = 5

    def constraint(self, display_size):
        # if self.x > display_size[0] - self.size:
        #     self.dx = -self.dx
        # if self.x < 0 + self.size:
        #     self.dx = -self.dx
        if self.y > display_size[1] - self.size:
            self.dy = -self.dy
        if self.y < 0 + self.size:
            self.dy = -self.dy

    def random_move(self):
        self.dx = random.choice((-self.move_speed, self.move_speed))
        self.dy = random.choice((-self.move_speed, self.move_speed))
