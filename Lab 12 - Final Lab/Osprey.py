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
            player_hp = 450
            print("You now have " +str(player_hp))

        if user_choice.upper() == "D":
            print("All Power to Foreward Faceing Weapons and Fire! ")
            pdamage = pdamage + random.randrange(80, 320)
            print("the Osprey now has " + str(hp - pdamage), "hit points left")
            osdamage = osdamage + random.randrange(30, 90)
            print("You have " + str(player_hp - osdamage), "hit points left")
            beam_coils = beam_coils - random.randrange(2,4)


        elif user_choice.upper() == "A":
            print("You attack with your weapons")
            pdamage = pdamage + random.randrange(40, 160)
            print("The Osprey now has " + str(hp - pdamage), "hit points left")
            osdamage = osdamage + random.randrange(30, 90)
            print("You have " + str(player_hp - osdamage), "Hit Points Left")
            beam_coils = beam_coils - int(1)

        elif user_choice.upper() == "E":
            print("Current HP: " + str(player_hp))
            print("Beam Coils Left: " + str(beam_coils))


        if hp - pdamage < 0:
            print("Osprey has been destroyed")
            done = True

        if player_hp - osdamage < 0:
            print("Your ship has been destroyed")
            done = True


osprey()