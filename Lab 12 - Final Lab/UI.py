import random
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
Cursor_Scaling = 1
UI_Scaling = 2.5
Attack_Icon_Scaling = .856
Player_Ship_Scaling = .5
HP_Size = .1






class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.UI_List = None
        self.cursor_list = None
        self.Attack_Icon_list = None
        self.Attack_Icon_list_Second = None
        self.Player_Ship_List = None
        self.HP_List = None


        self.score = 30

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)



    def setup(self):
        self.UI_List = arcade.SpriteList()
        self.cursor_list = arcade.SpriteList()
        self.Attack_Icon_list =arcade.SpriteList()
        self.Attack_Icon_list_Second = arcade.SpriteList()
        self.Player_Ship_List = arcade.SpriteList()
        self.HP_List = arcade.SpriteList()

        self.UI_Left_Arrow = arcade.Sprite("blue_sliderLeft.png", UI_Scaling)
        self.UI_Left_Arrow.center_x = 60
        self.UI_Left_Arrow.center_y = 50
        self.UI_List.append(self.UI_Left_Arrow)

        self.UI_Right_Arrow  = arcade.Sprite("blue_sliderRight.png", UI_Scaling)
        self.UI_Right_Arrow.center_x  = 540
        self.UI_Right_Arrow.center_y = 50
        self.UI_List.append(self.UI_Right_Arrow)

        #left mid section
        self.mid_left_section = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_left_section.center_x = 120
        self.mid_left_section.center_y = 55
        self.UI_List.append(self.mid_left_section)

        self.mid_left_section_2 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_left_section_2.center_x = 150
        self.mid_left_section_2.center_y = 55
        self.UI_List.append(self.mid_left_section_2)

        self.mid_left_section_3 =arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_left_section_3.center_x = 180
        self.mid_left_section_3.center_y = 55
        self.UI_List.append(self.mid_left_section_3)

        self.mid_left_section_4 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_left_section_4.center_x = 210
        self.mid_left_section_4.center_y = 55
        self.UI_List.append(self.mid_left_section_4)

        self.mid_left_section_5 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_left_section_5.center_x = 240
        self.mid_left_section_5.center_y = 55
        self.UI_List.append(self.mid_left_section_5)

        self.mid_left_section_6 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_left_section_6.center_x = 270
        self.mid_left_section_6.center_y = 55
        self.UI_List.append(self.mid_left_section_6)

        #right mid section
        self.mid_right_section = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_right_section.center_x = 300
        self.mid_right_section.center_y = 55
        self.UI_List.append(self.mid_right_section)

        self.mid_right_section_2 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_right_section_2.center_x = 330
        self.mid_right_section_2.center_y = 55
        self.UI_List.append(self.mid_right_section_2)

        self.mid_right_section_3 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_right_section_3.center_x = 360
        self.mid_right_section_3.center_y = 55
        self.UI_List.append(self.mid_right_section_3)

        self.mid_right_section_4 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_right_section_4.center_x = 390
        self.mid_right_section_4.center_y = 55
        self.UI_List.append(self.mid_right_section_4)

        self.mid_right_section_5 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_right_section_5.center_x = 420
        self.mid_right_section_5.center_y = 55
        self.UI_List.append(self.mid_right_section_5)

        self.mid_right_section_6 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_right_section_6.center_x = 450
        self.mid_right_section_6.center_y = 55
        self.UI_List.append(self.mid_right_section_6)

        self.mid_right_section_7 = arcade.Sprite("barHorizontal_blue_mid.png", UI_Scaling)
        self.mid_right_section_7.center_x = 480
        self.mid_right_section_7.center_y = 55
        self.UI_List.append(self.mid_right_section_7)

        self.Attack_Icon_Attack_Base = arcade.Sprite("crossair_black.png", Attack_Icon_Scaling)
        self.Attack_Icon_Attack_Base.center_x = 165
        self.Attack_Icon_Attack_Base.center_y = 55
        self.Attack_Icon_list.append(self.Attack_Icon_Attack_Base)

        #2nd Attack Draw 2
        self.Attack_Icon_Attack_2nd_First_Circle = arcade.Sprite("crossair_redOutline.png", Attack_Icon_Scaling)
        self.Attack_Icon_Attack_2nd_First_Circle.center_x = 435
        self.Attack_Icon_Attack_2nd_First_Circle.center_y = 55
        self.Attack_Icon_list_Second.append(self.Attack_Icon_Attack_2nd_First_Circle)




        # --- Place walls with a list
        coordinate_list = [[300, 40],
                           [300, 50],
                           [300, 60],
                           [300, 70]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            HP = arcade.Sprite("red_button13.png",HP_Size)
            HP.center_x = coordinate[0]
            HP.center_y = coordinate[1]
            HP.angle = 90
            self.HP_List.append(HP)



        #Player Ship

        self.Player_Ship = arcade.Sprite("Player.png", Player_Ship_Scaling)
        self.Player_Ship.center_x = 150
        self.Player_Ship.center_y = 200
        self.Player_Ship.angle = 45
        self.Player_Ship_List.append(self.Player_Ship)






        self.cursor = arcade.Sprite("cursor_pointerFlat.png", Cursor_Scaling)
        self.cursor.center_x = 100
        self.cursor.change_y = 100
        self.cursor_list.append(self.cursor)



    def on_draw(self):
        arcade.start_render()
        self.UI_List.draw()

        self.Attack_Icon_list.draw()
        self.Attack_Icon_list_Second.draw()
        self.Player_Ship_List.draw()
        arcade.draw_rectangle_filled(300,55,3,45,(arcade.color.BLACK),0)
        self.HP_List.draw()
        self.cursor_list.draw() #keep this last, order matters


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.cursor.center_x = x
        self.cursor.center_y = y


    def base_attack(self):
        self.on_mouse_press()







def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()