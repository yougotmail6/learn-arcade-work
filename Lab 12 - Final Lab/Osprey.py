# The Osprey Cannot Fire Full Phasers


import random


def osprey():
    print("You hear the call of the Osprey ")
    print("The Osprey is a versitle well made ship, good HP, but low on Damage and cannot do Full Weapons Blast")

    done = False
    hp = 500
    pdamage = 0
    osdamage = 0
    player_hp = 450
    # beam_coils = 6 (Added at a later date)

    while done == False:
        print("""
        A. Attack
        B. Regenerate Shield
        C. Full Power to Phasers""")

        user_choice = input("Please pick one! ")

        # if user_choice.upper() == "B":
        #   print("You attack with your weapons")
        #    shield=shield+random.randrange(10,20)
        # print("You know have " + str (shield), "Shields")

        if user_choice.upper() == "C":
            print("All Power to Foreward Faceing Weapons and Fire! ")
            pdamage = pdamage + random.randrange(80, 320)
            print("the Osprey now has " + str(hp - pdamage), "hit points left")
            osdamage = osdamage + random.randrange(30, 90)
            print("You have " + str(player_hp - osdamage), "hit points left")


        elif user_choice.upper() == "A":
            print("You attack with your weapons")
            pdamage = pdamage + random.randrange(40, 160)
            print("The Osprey now has " + str(hp - pdamage), "hit points left")
            osdamage = osdamage + random.randrange(30, 90)
            print("You have " + str(player_hp - osdamage), "Hit Points Left")

        if hp - pdamage < 0:
            print("Osprey has been destroyed")
            done = True

        if player_hp - osdamage < 0:
            print("Your ship has been destroyed")
            done = True

if __name__ == osprey:
    osprey()