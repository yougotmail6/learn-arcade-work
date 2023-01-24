import arcade
# background settings
arcade.open_window(600, 600, "All Aboard the Ugly Bus")
arcade.set_background_color(arcade.csscolor.VIOLET)
arcade.set_background_color((238, 130, 238))
arcade.start_render()
# bus settings
arcade.draw_polygon_filled([(25,345), (50, 400), (350, 400), (375, 345)],arcade.color.BLUE)
arcade.draw_rectangle_filled(200, 320, 350, 50, arcade.color.GREEN)
arcade.draw_ellipse_filled(100, 300, 50, 50, arcade.color.BLACK)
arcade.draw_ellipse_filled(300, 300, 50, 50,arcade.color.BLACK)
arcade.draw_point(56, 45, arcade.color.BLACK, size=20), arcade.color.BLACK

arcade.finish_render()
arcade.run()
