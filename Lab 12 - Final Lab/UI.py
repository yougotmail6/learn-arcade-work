
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
Cursor_Scaling = 1
UI_Scaling = 2.5
class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.UI_List = None
        self.cursor_list = None


        self.score = 30

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)



    def setup(self):
        self.UI_List = arcade.SpriteList()
        self.cursor_list = arcade.SpriteList()


        self.cursor = arcade.Sprite("cursor_pointerFlat.png", Cursor_Scaling)
        self.cursor.center_x = 100
        self.cursor.change_y = 100
        self.cursor_list.append(self.cursor)


        self.UI_Left_Arrow = arcade.Sprite("blue_sliderLeft.png", UI_Scaling)
        self.UI_Left_Arrow.center_x = 60
        self.UI_Left_Arrow.center_y = 50
        self.UI_List.append(self.UI_Left_Arrow)

        self.UI_Right_Arrow  = arcade.Sprite("blue_sliderRight.png", UI_Scaling)
        self.UI_Right_Arrow.center_x  = 540
        self.UI_Right_Arrow.center_y = 50
        self.UI_List.append(self.UI_Right_Arrow)

        self.mid_left_section = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_left_section.center_x = 120
        self.mid_left_section.center_y = 55
        self.UI_List.append(self.mid_left_section)



    def on_draw(self):
        arcade.start_render()
        self.UI_List.draw()
        self.cursor_list.draw()


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.cursor.center_x = x
        self.cursor.center_y = y



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()