import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600




def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.GREEN)


def draw_tree(x, y):
    """ Draw a Tree """



    # Trunk
    arcade.draw_rectangle_filled(x+15, y+175, 50, 275, arcade.csscolor.BROWN)


    # Leaves
    arcade.draw_circle_filled(x + 15, 310 + y, 100, arcade.csscolor.GREEN)
    arcade.draw_circle_filled(x + 15, 310 + y, 100, arcade.make_transparent_color(arcade.color.DARK_GREEN,150))

def draw_sun(x, y):

    arcade.draw_circle_filled(x,y + 175, 100,arcade.csscolor.YELLOW)



    arcade.draw_circle_filled(x,y + 175, 100, arcade.make_transparent_color(arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 150))


    arcade.draw_circle_filled(x,y + 175, 100, arcade.make_transparent_color(arcade.csscolor.ORANGE,600))






def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
    arcade.start_render()

    draw_grass()
    draw_tree(150, 162)
    draw_tree(650, 162)
    draw_sun(420, 400)


    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()