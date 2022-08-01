"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    started = False
    lives = NUM_LIVES
    graphics = BreakoutGraphics()
    while lives > 0 and started is False:
        graphics.new_start()
        while True:
            pause(FRAME_RATE)
            if graphics.get_y_speed() != 0:
                vx = graphics.get_x_speed()
                vy = graphics.get_y_speed()
                break
        # Add animation loop here!
        while True:
            pause(FRAME_RATE)
            graphics.ball.move(vx, vy)
            # Check bottom
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                started = False
                break
            # Check border
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                vx *= -1
            if graphics.ball.y <= 0:
                vy *= -1
            # Check brick or paddle
            if graphics.rebound():  # 有碰撞
                if graphics.obj_1 is not None:  # 碰到 paddle 或是 brick
                    vy *= -1
                    if graphics.obj_1 is graphics.paddle:
                        if vy > 0:
                            vy *= -1
                    else:
                        graphics.window.remove(graphics.obj_1)
                        graphics.total_bricks -= 1
                elif graphics.obj_2 is not None:
                    vy *= -1
                    if graphics.obj_2 is graphics.paddle:
                        if vy > 0:
                            vy *= -1
                    else:
                        graphics.window.remove(graphics.obj_2)
                        graphics.total_bricks -= 1
                elif graphics.obj_3 is not None:
                    vy *= -1
                    if graphics.obj_3 is graphics.paddle:
                        if vy > 0:
                            vy *= -1
                    else:
                        graphics.window.remove(graphics.obj_3)
                        graphics.total_bricks -= 1
                elif graphics.obj_4 is not None:
                    vy *= -1
                    if graphics.obj_4 is graphics.paddle:
                        if vy > 0:
                            vy *= -1
                    else:
                        graphics.window.remove(graphics.obj_4)
                        graphics.total_bricks -= 1
            # Check all bricks
            if graphics.total_bricks == 0:
                lives = 0
                break
    graphics.new_start()

if __name__ == '__main__':
    main()
