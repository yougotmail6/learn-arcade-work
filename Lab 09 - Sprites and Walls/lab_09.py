"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling

Your Computer May have isssues running this
"""

import random
import arcade
from pyglet.math import Vec2
SPRITE_SCALING_BOX = .7
SPRITE_BARRACK_BOX = .7
SPRITE_COIN_SCALING_BOX = 1

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 260

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 3


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None


        # Set up the player
        self.player_sprite = None
        self.score = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False


        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0
        self.good_music = arcade.load_sound("Bell Ding Sound Effect (download).wav")


        # Set up the player
        self.player_sprite = arcade.Sprite("scifiUnit_09.png",
                                           scale=.8)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 390
        self.player_sprite.change_x = 1
        self.player_sprite.change_y = 1
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls

        # --- Place walls with a list
        # Place boxes inside a loop
        for x in range(100, 2000, 32):
            wall = arcade.Sprite("scifiTile_41.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)
        #self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # --- Place walls with a list

        for x in range(100, 2000, 300):
            barracks = arcade.Sprite("scifiStructure_03.png", SPRITE_BARRACK_BOX)
            barracks.center_x = x
            barracks.center_y = 390
            self.wall_list.append(barracks)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        for x in range(100, 2000, 32):
            top_floor = arcade.Sprite("scifiTile_41.png", SPRITE_SCALING_BOX)
            top_floor.center_x = x
            top_floor.center_y = 475
            self.wall_list.append(top_floor)

        for y in range(390,500, 32):
            end_barrier = arcade.Sprite("scifiTile_41.png", SPRITE_SCALING_BOX)
            end_barrier.center_x = 1980
            end_barrier.center_y = y
            self.wall_list.append(end_barrier)

        # --- Place walls with a list
        coordinate_list = [[300, 420],
                           [600, 420],
                           [1000, 420],
                           [1100, 420],
                           [450, 420],
                           [545, 380],
                           [780, 420],
                           [860, 420],
                           [940, 420],
                           [1350, 380],
                           [630, 380],
                           [1400, 420],
                           [1540, 380],
                           [1700, 420],
                           [800, 380],
                           [750, 380],
                           [900, 380],
                           [950,380]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            coin = arcade.Sprite("tile_0029.png", SPRITE_COIN_SCALING_BOX)
            coin.center_x = coordinate[0]
            coin.center_y = coordinate[1]
            self.coin_list.append(coin)



        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()


        # Select the camera we'll use to draw all our sprites

        self.camera_sprites.use()


        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()



        # Select the (unscrolled) camera for our GUI

        self.camera_gui.use()


        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        arcade.draw_text("The Left arrow key does not work, it does not work for a reason", 0, 50, (arcade.color.BLACK_BEAN), 16)


        arcade.draw_rectangle_filled(10,508,200,40,arcade.color.ALMOND,0)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 500, arcade.color.BLACK_BEAN, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
            self.up_pressed = self.player_sprite.angle = 90

        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.right_pressed = self.player_sprite.angle = 360

        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.down_pressed = self.player_sprite.angle = 270


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


        # Scroll the screen to the player

        self.scroll_to_player()



    def scroll_to_player(self):

        """

        Scroll the window to the player.



        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.

        Anything between 0 and 1 will have the camera move to the location with a smoother

        pan.

        """



        position = Vec2(self.player_sprite.center_x - self.width / 5,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)



    def on_resize(self, width, height):

        """

        Resize window

        Handle the user grabbing the edge and resizing the window.

        """

        self.camera_sprites.resize(int(width), int(height))

        self.camera_gui.resize(int(width), int(height))

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()


        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)


        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.good_music.play()

def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()