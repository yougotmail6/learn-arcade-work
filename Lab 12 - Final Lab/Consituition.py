# The Osprey Cannot Fire Full Phasers


import random


def Consituition():
    print("You hear a warping noise as a massive warship appears off the starboard side of your ship ")
    print("The Constituition was a ship of the old war, a large powerhouse of a ship, considered to be the best ship the federation has ever made." )

    done = False
    hp = 900
    pdamage = 0
    cdamage = 0
    player_hp = 450
    beam_coils = 6

    while done == False:
        print("""
        A. Attack
        B. Regenerate Shield
        C. Regenrate Health
        D. Full Power to Phasers
        E. Check Ship Systems""")

        user_choice = input("Please pick one! ")

        if user_choice.upper() == "B":
            print("You replensish your Beam Coils")
            beam_coils = 6
            print("You know have " + str(beam_coils), "Beam Coils to use")


        if user_choice.upper() == "C":
            print("You regenerate hull plating ")
            player_hp = player_hp + 450
            print("You now have " +str(player_hp))

        if user_choice.upper() == "D":
            print("All Power to Foreward Faceing Weapons and Fire! ")
            pdamage = pdamage + random.randrange(80, 320)
            print("the Consituition now has " + str(hp - pdamage), "hit points left")
            cdamage = cdamage + random.randrange(90, 150)
            print("You have " + str(player_hp - cdamage), "hit points left")
            beam_coils = beam_coils - random.randrange(2,4)


        elif user_choice.upper() == "A":
            print("You attack with your weapons")
            pdamage = pdamage + random.randrange(40, 160)
            print("The Consituition now has " + str(hp - pdamage), "hit points left")
            cdamage = cdamage + random.randrange(90, 150)
            print("You have " + str(player_hp - cdamage), "Hit Points Left")
            beam_coils = beam_coils - int(1)

        elif user_choice.upper() == "E":
            print("Current HP: " + str(player_hp))
            print("Beam Coils Left: " + str(beam_coils))


        if hp - pdamage < 0:
            print("The Consituition has been destroyed")
            done = True

        if player_hp - cdamage < 0:
            print("Your ship has been destroyed")
            done = True


Consituition()
