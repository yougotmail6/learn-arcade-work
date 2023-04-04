import arcade
import random

SPRITE_UI_SCALING = .75

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.User_Interface_list = None

        # Don't show the mouse cursor


        arcade.set_background_color(arcade.color.DARK_GREEN)

    def setup(self):
        self.User_Interface_list = arcade.SpriteList()


        self.User_Interface_Sprite = arcade.Sprite("green_button07.png", SPRITE_UI_SCALING)
        self.User_Interface_Sprite.center_x = 50
        self.User_Interface_Sprite.center_y = 50
        self.User_Interface_list.append(self.User_Interface_Sprite)


    def on_draw(self):
        self.User_Interface_list.draw()




def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()