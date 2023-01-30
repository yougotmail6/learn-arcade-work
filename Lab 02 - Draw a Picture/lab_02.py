import arcade
import math


#Arcade Settings

arcade.open_window(600,600, "Mario Tube with Mountains.")
arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
arcade.start_render()

# box draw

arcade.draw_rectangle_filled(300,200,700,400, arcade.color.GRAY)


#Draw Mountains

for i in range(360):
    arcade.draw_point(i / .4 + 0, math.sin(math.radians(i)) * 100 + 400, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 5, math.sin(math.radians(i)) * 100 + 398, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 10, math.sin(math.radians(i)) * 100 + 396, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 15, math.sin(math.radians(i)) * 100 + 394, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 20, math.sin(math.radians(i)) * 100 + 392, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 25, math.sin(math.radians(i)) * 100 + 390, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 30, math.sin(math.radians(i)) * 100 + 388, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 35, math.sin(math.radians(i)) * 100 + 386, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 40, math.sin(math.radians(i)) * 100 + 384, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 45, math.sin(math.radians(i)) * 100 + 382, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 50, math.sin(math.radians(i)) * 100 + 380, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 55, math.sin(math.radians(i)) * 100 + 378, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 60, math.sin(math.radians(i)) * 100 + 376, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 65, math.sin(math.radians(i)) * 100 + 374, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 70, math.sin(math.radians(i)) * 100 + 372, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 75, math.sin(math.radians(i)) * 100 + 370, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 80, math.sin(math.radians(i)) * 100 + 368, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 85, math.sin(math.radians(i)) * 100 + 366, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 90, math.sin(math.radians(i)) * 100 + 364, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 95, math.sin(math.radians(i)) * 100 + 362, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 100, math.sin(math.radians(i)) * 100 + 360, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 105, math.sin(math.radians(i)) * 100 + 358, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 110, math.sin(math.radians(i)) * 100 + 356, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 115, math.sin(math.radians(i)) * 100 + 354, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 120, math.sin(math.radians(i)) * 100 + 352, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 125, math.sin(math.radians(i)) * 100 + 350, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 130, math.sin(math.radians(i)) * 100 + 348, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 135, math.sin(math.radians(i)) * 100 + 346, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 140, math.sin(math.radians(i)) * 100 + 344, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 145, math.sin(math.radians(i)) * 100 + 342, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 150, math.sin(math.radians(i)) * 100 + 340, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 155, math.sin(math.radians(i)) * 100 + 338, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 160, math.sin(math.radians(i)) * 100 + 336, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 165, math.sin(math.radians(i)) * 100 + 334, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 170, math.sin(math.radians(i)) * 100 + 332, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 175, math.sin(math.radians(i)) * 100 + 330, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 180, math.sin(math.radians(i)) * 100 + 328, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 185, math.sin(math.radians(i)) * 100 + 326, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 190, math.sin(math.radians(i)) * 100 + 324, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 195, math.sin(math.radians(i)) * 100 + 322, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 200, math.sin(math.radians(i)) * 100 + 320, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 205, math.sin(math.radians(i)) * 100 + 318, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 210, math.sin(math.radians(i)) * 100 + 316, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 215, math.sin(math.radians(i)) * 100 + 314, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 220, math.sin(math.radians(i)) * 100 + 312, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 225, math.sin(math.radians(i)) * 100 + 310, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 230, math.sin(math.radians(i)) * 100 + 308, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 235, math.sin(math.radians(i)) * 100 + 306, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 240, math.sin(math.radians(i)) * 100 + 304, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 245, math.sin(math.radians(i)) * 100 + 302, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 250, math.sin(math.radians(i)) * 100 + 300, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 255, math.sin(math.radians(i)) * 100 + 298, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 260, math.sin(math.radians(i)) * 100 + 296, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 265, math.sin(math.radians(i)) * 100 + 294, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 270, math.sin(math.radians(i)) * 100 + 292, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 275, math.sin(math.radians(i)) * 100 + 290, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 280, math.sin(math.radians(i)) * 100 + 288, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 285, math.sin(math.radians(i)) * 100 + 286, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 290, math.sin(math.radians(i)) * 100 + 284, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 295, math.sin(math.radians(i)) * 100 + 282, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 300, math.sin(math.radians(i)) * 100 + 280, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 305, math.sin(math.radians(i)) * 100 + 278, arcade.csscolor.GRAY, 4)
    arcade.draw_point(i / .4 + 310, math.sin(math.radians(i)) * 100 + 276, arcade.csscolor.GRAY, 4)






#Draw Pipe and Sun
arcade.draw_rectangle_filled(300,200,200,400, arcade.color.GREEN)
arcade.draw_ellipse_filled(515,500,100,100, arcade.color.YELLOW)

arcade.finish_render()
arcade.run()
