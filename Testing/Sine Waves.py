import arcade
import random
import math


arcade.open_window(600, 600, "Sine Waves")
arcade.set_background_color(arcade.csscolor.BLACK)
arcade.set_background_color((0, 0, 0))
arcade.start_render()


v = arcade.csscolor.DARK_GREEN


for i in range(--500):

    arcade.draw_point(i / .4 - 0, math.sin(math.radians(i)) * 100 + 200,v , 4)
    arcade.draw_point(i / .4 - 20, math.sin(math.radians(i)) * 100 + 200,v , 4)
    arcade.draw_point(i / .4 - 40, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .4 - 60, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .4 - 80, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .4 - 100, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.DARK_RED, 4)
    arcade.draw_point(i / .4 - 120, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .4 - 140, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BROWN, 4)
    arcade.draw_point(i / .4 - 160, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.ROSY_BROWN, 4)
    arcade.draw_point(i / .4 - 180, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 200, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 220, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 240, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 260, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 280, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 300, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 320, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 340, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 360, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 380, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)
    arcade.draw_point(i / .4 - 400, math.sin(math.radians(i)) * 100 + 200, arcade.csscolor.BLUE, 4)


arcade.finish_render()
arcade.run()
