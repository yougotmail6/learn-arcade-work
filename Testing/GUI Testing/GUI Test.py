import arcade
import random

SPRITE_SCALING_PLAYER = .75
SPRITE_SCALING_UI = 1.2
SPRITE_SCALING_Dummy = 2
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
Dummy_Count = 45
class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.check_list = None
        self.player_sprite = None
        self.dummy_list = None

        self.score = 30

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)



    def setup(self):
        self.player_list = arcade.SpriteList()
        self.check_list = arcade.SpriteList()
        self.dummy_list = arcade.SpriteList()


        self.player_sprite = arcade.Sprite("crossair_red.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)


        self.check_sprite = arcade.Sprite("blue_boxCheckmark.png", SPRITE_SCALING_UI)
        self.check_sprite.center_x = 300
        self.check_sprite.center_y = 300
        self.check_list.append(self.check_sprite)

        for i in range(Dummy_Count):
        # Create the coin instance
        # Coin image from kenney.nl
            coin = arcade.Sprite("scifiUnit_13.png", SPRITE_SCALING_Dummy)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.dummy_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.check_list.draw()
        self.dummy_list.draw()

        output = f"Ammo: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)



    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        #Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        arcade.MOUSE_BUTTON_RIGHT



    def update(self, delta_time):
        self.dummy_list.update()


        dummy_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.dummy_list)
        for coin in dummy_hit_list:
            coin.remove_from_sprite_lists()
            self.score -= 1

        


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()