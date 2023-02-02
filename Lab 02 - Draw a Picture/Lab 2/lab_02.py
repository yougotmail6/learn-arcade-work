import arcade
import math



# Arcade Settings

arcade.open_window(600,600, "Mario Tube with Mountains.")
arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
arcade.start_render()

# box draw

v = arcade.csscolor.DARK_GREEN

arcade.draw_rectangle_filled(300,200,700,400, v)

# Defines Color for  each Sine Wave



# Draw Mountains

for i in range(360):
    arcade.draw_point(i / .4 + 0, math.sin(math.radians(i)) * 100 + 400, v, 4)
    arcade.draw_point(i / .4 + 5, math.sin(math.radians(i)) * 100 + 398, v, 4)
    arcade.draw_point(i / .4 + 10, math.sin(math.radians(i)) * 100 + 396, v, 4)
    arcade.draw_point(i / .4 + 15, math.sin(math.radians(i)) * 100 + 394, v, 4)
    arcade.draw_point(i / .4 + 20, math.sin(math.radians(i)) * 100 + 392, v, 4)
    arcade.draw_point(i / .4 + 25, math.sin(math.radians(i)) * 100 + 390, v, 4)
    arcade.draw_point(i / .4 + 30, math.sin(math.radians(i)) * 100 + 388, v, 4)
    arcade.draw_point(i / .4 + 35, math.sin(math.radians(i)) * 100 + 386, v, 4)
    arcade.draw_point(i / .4 + 40, math.sin(math.radians(i)) * 100 + 384, v, 4)
    arcade.draw_point(i / .4 + 45, math.sin(math.radians(i)) * 100 + 382, v, 4)
    arcade.draw_point(i / .4 + 50, math.sin(math.radians(i)) * 100 + 380, v, 4)
    arcade.draw_point(i / .4 + 55, math.sin(math.radians(i)) * 100 + 378, v, 4)
    arcade.draw_point(i / .4 + 60, math.sin(math.radians(i)) * 100 + 376, v, 4)
    arcade.draw_point(i / .4 + 65, math.sin(math.radians(i)) * 100 + 374, v, 4)
    arcade.draw_point(i / .4 + 70, math.sin(math.radians(i)) * 100 + 372, v, 4)
    arcade.draw_point(i / .4 + 75, math.sin(math.radians(i)) * 100 + 370, v, 4)
    arcade.draw_point(i / .4 + 80, math.sin(math.radians(i)) * 100 + 368, v, 4)
    arcade.draw_point(i / .4 + 85, math.sin(math.radians(i)) * 100 + 366, v, 4)
    arcade.draw_point(i / .4 + 90, math.sin(math.radians(i)) * 100 + 364, v, 4)
    arcade.draw_point(i / .4 + 95, math.sin(math.radians(i)) * 100 + 362, v, 4)
    arcade.draw_point(i / .4 + 100, math.sin(math.radians(i)) * 100 + 360, v, 4)
    arcade.draw_point(i / .4 + 105, math.sin(math.radians(i)) * 100 + 358, v, 4)
    arcade.draw_point(i / .4 + 110, math.sin(math.radians(i)) * 100 + 356, v, 4)
    arcade.draw_point(i / .4 + 115, math.sin(math.radians(i)) * 100 + 354, v, 4)
    arcade.draw_point(i / .4 + 120, math.sin(math.radians(i)) * 100 + 352, v, 4)
    arcade.draw_point(i / .4 + 125, math.sin(math.radians(i)) * 100 + 350, v, 4)
    arcade.draw_point(i / .4 + 130, math.sin(math.radians(i)) * 100 + 348, v, 4)
    arcade.draw_point(i / .4 + 135, math.sin(math.radians(i)) * 100 + 346, v, 4)
    arcade.draw_point(i / .4 + 140, math.sin(math.radians(i)) * 100 + 344, v, 4)
    arcade.draw_point(i / .4 + 145, math.sin(math.radians(i)) * 100 + 342, v, 4)
    arcade.draw_point(i / .4 + 150, math.sin(math.radians(i)) * 100 + 340, v, 4)
    arcade.draw_point(i / .4 + 155, math.sin(math.radians(i)) * 100 + 338, v, 4)
    arcade.draw_point(i / .4 + 160, math.sin(math.radians(i)) * 100 + 336, v, 4)
    arcade.draw_point(i / .4 + 165, math.sin(math.radians(i)) * 100 + 334, v, 4)
    arcade.draw_point(i / .4 + 170, math.sin(math.radians(i)) * 100 + 332, v, 4)
    arcade.draw_point(i / .4 + 175, math.sin(math.radians(i)) * 100 + 330, v, 4)
    arcade.draw_point(i / .4 + 180, math.sin(math.radians(i)) * 100 + 328, v, 4)
    arcade.draw_point(i / .4 + 185, math.sin(math.radians(i)) * 100 + 326, v, 4)
    arcade.draw_point(i / .4 + 190, math.sin(math.radians(i)) * 100 + 324, v, 4)
    arcade.draw_point(i / .4 + 195, math.sin(math.radians(i)) * 100 + 322, v, 4)
    arcade.draw_point(i / .4 + 200, math.sin(math.radians(i)) * 100 + 320, v, 4)
    arcade.draw_point(i / .4 + 205, math.sin(math.radians(i)) * 100 + 318, v, 4)
    arcade.draw_point(i / .4 + 210, math.sin(math.radians(i)) * 100 + 316, v, 4)
    arcade.draw_point(i / .4 + 215, math.sin(math.radians(i)) * 100 + 314, v, 4)
    arcade.draw_point(i / .4 + 220, math.sin(math.radians(i)) * 100 + 312, v, 4)
    arcade.draw_point(i / .4 + 225, math.sin(math.radians(i)) * 100 + 310, v, 4)
    arcade.draw_point(i / .4 + 230, math.sin(math.radians(i)) * 100 + 308, v, 4)
    arcade.draw_point(i / .4 + 235, math.sin(math.radians(i)) * 100 + 306, v, 4)
    arcade.draw_point(i / .4 + 240, math.sin(math.radians(i)) * 100 + 304, v, 4)
    arcade.draw_point(i / .4 + 245, math.sin(math.radians(i)) * 100 + 302, v, 4)
    arcade.draw_point(i / .4 + 250, math.sin(math.radians(i)) * 100 + 300, v, 4)
    arcade.draw_point(i / .4 + 255, math.sin(math.radians(i)) * 100 + 298, v, 4)
    arcade.draw_point(i / .4 + 260, math.sin(math.radians(i)) * 100 + 296, v, 4)
    arcade.draw_point(i / .4 + 265, math.sin(math.radians(i)) * 100 + 294, v, 4)
    arcade.draw_point(i / .4 + 270, math.sin(math.radians(i)) * 100 + 292, v, 4)
    arcade.draw_point(i / .4 + 275, math.sin(math.radians(i)) * 100 + 290, v, 4)
    arcade.draw_point(i / .4 + 280, math.sin(math.radians(i)) * 100 + 288, v, 4)
    arcade.draw_point(i / .4 + 285, math.sin(math.radians(i)) * 100 + 286, v, 4)
    arcade.draw_point(i / .4 + 290, math.sin(math.radians(i)) * 100 + 284, v, 4)
    arcade.draw_point(i / .4 + 295, math.sin(math.radians(i)) * 100 + 282, v, 4)
    arcade.draw_point(i / .4 + 300, math.sin(math.radians(i)) * 100 + 280, v, 4)
    arcade.draw_point(i / .4 + 305, math.sin(math.radians(i)) * 100 + 278, v, 4)
    arcade.draw_point(i / .4 + 310, math.sin(math.radians(i)) * 100 + 276, v, 4)






# Draw Pipe and Sky

f = arcade.csscolor.BROWN
s =  arcade.csscolor.YELLOW


arcade.draw_rectangle_filled(300,200,200,400, f)
arcade.draw_ellipse_filled(515,500,100,100, s)





o = arcade.finish_render()
m = arcade.run()

o
m


# This code uses variables to represent the csscolor, this optimized the code significantly. Normal size when using the csscolor, would be 6.8 Kilobytes,
# With the optimizations used in this code, it is now 5.54 KB, improving it by almost 1.3 KB.
