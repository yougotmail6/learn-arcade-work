# Mantis is not capable of using normal phasers, and can only do full power


import random


def Mantis():
    print("You hear the souls praying to the Mantis.")

    done = False
    hp = 350
    pdamage = 0
    mdamage = 0
    player_hp = 450
    beam_coils = 6

    while done == False:
        print("""
        A. Attack
        B. Regenerate Shield
        C. Regenerate Health
        D. Full Power to Phasers
        E. Check Ship Systems""")

        user_choice = input("Please pick one! ")

        if user_choice.upper() == "B":
            print("You replensish your Beam Coils")
            beam_coils = 6
            print("You know have " + str(beam_coils), "Beam Coils to use")

        if user_choice.upper() == "C":
            print("You regenrate Hull Plating ")
            player_hp = 450
            print("You now have " +str(player_hp))

        if user_choice.upper() == "D":
            print("All Power to Foreward Faceing Weapons and Fire! ")
            pdamage = pdamage + random.randrange(80, 320)
            print("the Mantis now has " + str(hp - pdamage), "hit points left")
            mdamage = mdamage + random.randrange(110, 200)
            print("You have " + str(player_hp - mdamage), "hit points left")
            beam_coils = beam_coils - random.randrange(2,4)

        elif user_choice.upper() == "A":
            print("You attack with your weapons")
            pdamage = pdamage + random.randrange(40, 160)
            print("The Mantis now has " + str(hp - pdamage), "hit points left")
            mdamage = mdamage + random.randrange(110, 200)
            print("You have " + str(player_hp - mdamage), "Hit Points Left")
            beam_coils = beam_coils - int(1)

        elif user_choice.upper() == "E":
            print("Current HP: " + str(player_hp))
            print("Beam Coils Left: " + str(beam_coils))

        if hp - pdamage < 0:
            print("Mantis has been destroyed")
            done = True

        if player_hp - mdamage < 0:
            print("Your ship has been destroyed")
            done = True


Mantis()