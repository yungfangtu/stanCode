"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 10  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
started = False


class BreakoutGraphics:
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        # Draw bricks
        self.total_bricks = 0
        self.brick_colors = ''
        for i in range(0, brick_cols):
            for j in range(0, brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.x = (brick_width + brick_spacing)*i
                self.brick.y = (brick_height + brick_spacing)*j
                if j <= 1:
                    self.brick_color = 'red'
                elif j <= 3:
                    self.brick_color = 'orange'
                elif j <= 5:
                    self.brick_color = 'yellow'
                elif j <= 7:
                    self.brick_color = 'green'
                elif j <= 9:
                    self.brick_color = 'blue'
                self.brick.color = self.brick_color
                self.brick.filled = True
                self.brick.fill_color = self.brick_color
                self.window.add(self.brick)
                self.total_bricks += 1
        # Get objects
        self.obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.obj_2 = self.window.get_object_at(self.ball.x + 2 * ball_radius, self.ball.y)
        self.obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * ball_radius)
        self.obj_4 = self.window.get_object_at(self.ball.x + 2 * ball_radius, self.ball.y + 2 * ball_radius)
        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0
        self.new_start()
        self.rebound()
        onmousemoved(self.move_paddle)

    def new_start(self):
        self.window.add(self.paddle)
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        global started
        if not started:
            onmouseclicked(self.start_game)
            started = True
        else:
            self._dx = 0
            self._dy = 0

    # Mouse listener
    def start_game(self, mouse):
        if 0 <= mouse.x <= self.window.width and 0 <= mouse.y <= self.window.height:
            self.set_ball_velocity()

    def set_ball_velocity(self):
        self._dx = random.randint(1, MAX_X_SPEED)
        if (random.random()) > 0.5:
            self._dx *= -1
        self._dy = INITIAL_Y_SPEED

    # Mouse listener
    def move_paddle(self, mouse):
        self.paddle.move(mouse.x-self.paddle.x-self.paddle.width/2, 0)
        if self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if self.paddle.x < 0:
            self.paddle.x = 0

    def rebound(self):
        self.obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.obj_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball.height)
        self.obj_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if self.obj_1 is None and self.obj_2 is None and self.obj_3 is None and self.obj_4 is None:
            return False
        else:
            return True

    # Getter
    def get_x_speed(self):
        return self._dx

    def get_y_speed(self):
        return self._dy
