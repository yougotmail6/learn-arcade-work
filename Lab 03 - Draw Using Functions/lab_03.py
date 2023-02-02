import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

v = arcade.csscolor.GREEN
q = arcade.csscolor.SKY_BLUE
b = arcade.csscolor.BROWN
p = arcade.csscolor.LIGHT_GOLDENROD_YELLOW
j = arcade.make_transparent_color(p, 150)
k = arcade.csscolor.YELLOW
m = arcade.csscolor.ORANGE
w = arcade.make_transparent_color(m,600)



def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, v)


def draw_tree(x, y):
    """ Draw a snow person """



    # Trunk
    arcade.draw_rectangle_filled(x+15, y+175, 50, 275, b)


    # Leaves
    arcade.draw_circle_filled(x + 15, 310 + y, 100, v)
    arcade.draw_circle_filled(x + 15, 310 + y, 100, arcade.make_transparent_color(arcade.color.DARK_GREEN,150))

def draw_sun(x, y):

    arcade.draw_circle_filled(x,y + 175, 100,k)



    arcade.draw_circle_filled(x,y + 175, 100, j)


    arcade.draw_circle_filled(x,y + 175, 100, w)




def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(q)
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