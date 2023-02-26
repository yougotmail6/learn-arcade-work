import arcade

arcade.open_window(600,600, "H")
arcade.set_background_color(arcade.csscolor.BROWN)
arcade.start_render()


h = arcade.draw_rectangle_filled(4,4,4,4,arcade.csscolor.WHITE)

for h in range(4):
    for row in range(4):
        for column in range(row-1):
            print(column, end="")




arcade.finish_render()
arcade.run()

