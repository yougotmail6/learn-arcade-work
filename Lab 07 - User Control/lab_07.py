import arcade
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
MOVEMENT_SPEED = 3


class Ball:
    def __init__(self, center_x, center_y, change_x, change_y, width, height, color,tilt):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.tilt = tilt

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color,self.tilt)



    def update(self):
        # Move the ball
        self.center_y += self.change_y
        self.center_x += self.change_x

        if self.center_x > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH

        if self.center_x < SCREEN_WIDTH - self.center_x:
            self.center_x = SCREEN_WIDTH - self.center_x

        if self.center_y > SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT

        if self.center_y < SCREEN_HEIGHT - self.center_y:
            self.center_y = SCREEN_HEIGHT - self.center_y

class Cube:

    def __init__(self, center_x, center_y, width, height, color,tilt):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.color = color
        self.tilt = tilt
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color, self.tilt)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)


        # Create our ball
        self.ball = Ball(50,50,1,1,20,20,(arcade.color.AUBURN),0)
        self.Cube = Cube((random.randrange(10, 300)), (random.randrange(10, 300)), 10, 10, (arcade.color.BLACK), 3)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.Cube.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame(1920, 1080, "Drawing Example")
    arcade.run()


main()