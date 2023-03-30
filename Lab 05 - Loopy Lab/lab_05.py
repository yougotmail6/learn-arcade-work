# Im completly lost on this, however I believe I somewhat pulled this off.


import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(13):
        for column in range(33):
            x = column * 18.4  # Instead of zero, calculate the proper x location using 'column'
            y = row * 24 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(40):
        for column in range(50):
            y = column * 6.1  # Instead of zero, calculate the proper x location using 'column'
            x = row * 8 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    for row in range(12):
        for column in range(33):
            x = column * 18
            y = row * 23
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

def draw_section_3():
    for row in range(14):
        for column in range(50):
            x = column * 18
            y = row * 23
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

    for row in range(14):
        for column in range(48):
            y = column * 18
            x = row * 23
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    pass


def draw_section_5():
    for row in range(50):
        for column in range(row + 48):
            x = row * 6.1  # Instead of zero, calculate the proper x location using 'column'
            y = column * 8 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(50):
        for column in range(48 - row):
            x = row * 6.1  # Instead of zero, calculate the proper x location using 'column'
            y = column * 8 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    pass


def draw_section_8():
    pass


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
