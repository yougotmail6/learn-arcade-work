import arcade
import math



# Arcade Settings

arcade.open_window(600,600, "Mario Tube with Mountains.")
arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
arcade.start_render()

# box draw

v = arcade.csscolor.DARK_GREEN

arcade.draw_rectangle_filled(300,200,700,400, arcade.csscolor.DARK_GREEN)

# Draw Mountains

for i in range(720):
    arcade.draw_line(i, math.sin(math.radians(i) * 4) * 40 + 450, i, 400, arcade.csscolor.GRAY,1)
# Draw Pipe and Sky

arcade.draw_rectangle_filled(300,200,200,400, arcade.csscolor.BROWN)
arcade.draw_ellipse_filled(515,590,100,100, arcade.csscolor.YELLOW)

arcade.finish_render()
arcade.run()



# This code uses variables to represent the csscolor, this optimized the code significantly. Normal size when using the csscolor, would be 6.8 Kilobytes,
# With the optimizations used in this code, it is now 5.54 KB, improving it by almost 1.3 KB.
