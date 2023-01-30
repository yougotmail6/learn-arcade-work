import  arcade
import math

arcade.open_window(600,600, "Test")
arcade.set_background_color(arcade.csscolor.BLACK)
arcade.start_render()

for i in range(360):
    arcade.draw_point(i / .5 + 0, math.sin(math.radians(i)) * 100 + 400, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .5 + 0, math.sin(math.radians(i)) * 100 + 395, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .5 + 0, math.sin(math.radians(i)) * 100 + 390, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .5 + 0, math.sin(math.radians(i)) * 100 + 385, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .4 + 0, math.sin(math.radians(i)) * 100 + 380, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .4 + 0, math.sin(math.radians(i)) * 100 + 375, arcade.csscolor.RED, 4)
    arcade.draw_point(i / .4 + 0, math.sin(math.radians(i)) * 100 + 370, arcade.csscolor.RED, 4)


arcade.finish_render()
arcade.run()

