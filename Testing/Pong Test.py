import arcade


arcade.open_window(1920, 1080, "Pong Test")
arcade.set_background_color(arcade.csscolor.BLACK)
arcade.start_render()

def paddle_1():
    arcade.draw_rectangle_filled(300,300, 12, 100, (arcade.color.WHITE))
paddle_1()

def paddle_2():
    arcade.draw_rectangle_filled(1600, 300, 12, 100, (arcade.color.WHITE))
paddle_2()

def on_draw()




arcade.finish_render()
arcade.run()