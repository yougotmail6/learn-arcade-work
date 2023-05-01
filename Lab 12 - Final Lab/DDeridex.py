# The Osprey Cannot Fire Full Phasers


import random


def dderidex():
    print("A Ship Decloaks infront of you ")
    print("The D'deridex is a warbird, it takes half damage, however is a tank, but has low DPS ")

    done = False
    hp = 1000
    pdamage = 0
    ddamage = 0
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
            pdamage = pdamage + random.randrange(40, 160)
            print("the D'deridex now has " + str(hp - pdamage), "hit points left")
            ddamage = ddamage + random.randrange(15, 100)
            print("You have " + str(player_hp - ddamage), "hit points left")
            beam_coils = beam_coils - random.randrange(2,4)


        elif user_choice.upper() == "A":
            print("You attack with your weapons")
            pdamage = pdamage + random.randrange(20, 80)
            print("The D;deridex now has " + str(hp - pdamage), "hit points left")
            ddamage = ddamage + random.randrange(15, 100)
            print("You have " + str(player_hp - ddamage), "Hit Points Left")
            beam_coils = beam_coils - int(1)

        elif user_choice.upper() == "E":
            print("Current HP: " + str(player_hp))
            print("Beam Coils Left: " + str(beam_coils))


        if hp - pdamage < 0:
            print("The D'deridex has been destroyed")
            done = True

        if player_hp - ddamage < 0:
            print("Your ship has been destroyed")
            done = True


dderidex()
