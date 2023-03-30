
#This is also very buggy and probably only works 15% of the time


#Class Creation

class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

        

Room

#Rooms

def main():
    room_list = []

    
    hallway_room = Room("You are in are at an etnrance of a large, dark hallway. There is a door on your right, and left. You may also continue further down the hallway if you so choose.", 4, 2,None, 0)
    room_list.append(hallway_room)
    
    hallway_room_2 = Room("You continue down the long, dark hallway. There is a door to your right and left, and also infront of you. You may also head back." , 6,5,1,3)
    room_list.append(hallway_room_2)

    
    kids_bedroom = Room("You open the door, revealing a kids bedroom. The room has a faint musty odor.\n The bed has not been made and their is a thick layer of dust on the Mirror. You cough violently. There is a door leading back to where you came from", None, 1, None, None)
    room_list.append(kids_bedroom)

    master_bedroom = Room("You open the door revealing another bedroom, this one however is much bigger and nicer than the last. However, this one aswell had fallen into disarray. \n The mirror had dirt and a thick layer of dust on it aswell. The bed was falling apart. You have the option to return back to the hallway", None, 4, None, None)
    room_list.append(master_bedroom)

    kitchen = Room("You come to a door way, you can make out black and marble tiling. A scent of burnt toast, Dawn Dish Soap, and Pinesol.The putrid smell coming from the kitchen makes you want to vomit. \n You can exit the kitchen by either walking through the door on the back of the room, or by the door to the west of the room.", None, None, 2, 4)
    room_list.append(kitchen)

    dinning_room = Room("You come to another open door way, the kitchen and the dinning room do connect. The smell from the kitchen is much more subtle now. The table is nicely set with silverware. \n There are a stack of plates on the table, recently cleaned infact.On a chair on the side the latest issue of Un guide du propriétaire pour réparer votre maison abandonnée!. \n There is a china cabinet on the left side of the room.", 5, None, None, 1)
    room_list.append(dinning_room)

    deck = Room("You open up the massive glass doors and step out onto the deck. It is very windy, however, you can see for miles. You can return to the house.", None, None, 4, None)
    room_list.append(deck)

    
    
    current_room = 0



#Game Logic
    


    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        location_char_movement = input("Select Direction, N, S, W, E, Q ").upper()

        if location_char_movement == 'N' or location_char_movement == 'north':
            closest_room = room_list[current_room].north
            if closest_room  is None:
                print("You bang your head into a wall")
            else:
                current_room = closest_room


        elif location_char_movement == 'E' or location_char_movement == 'east':
            closest_room = room_list[current_room].east
            if closest_room is None:
                print("You bang your head into the wall")
            else:
                current_room = closest_room

        elif location_char_movement == 'S' or location_char_movement == 'south':
            closest_room = room_list[current_room].south
            if closest_room is None:
                print("You Bang your head into the wall")
            else:
                current_room = closest_room

        elif location_char_movement == 'W' or location_char_movement == 'west':
            closest_room = room_list[current_room].west
            if closest_room is None:
                print("You bang your head into a wall")
            else:
                current_room = closest_room

        
        elif location_char_movement == 'Q':
            done = True
    

    

main()
