import random


def Baron():  # High Damage however low Health
    print("The Baron has got you in his sights! ")
    print("The Baron a legdendary merceinary in the Federation war of 2077 ")

    done = False
    hp = 350
    pdamage = 0
    badamage = 0
    player_hp = 450
    beam_coils = 6

    while done == False:
        print("""
        A. Attack
        B. Regenerate Beam Coils
        C. Regen Health
        D. Full Power to Phasers
        E. Check Ship Systems""")

        user_choice = input("Please pick one! ")

        if user_choice.upper() == "B":
            print("You replensish your Beam Coils")
            beam_coils = 6
            print("You know have " + str(beam_coils), "Beam Coils to use")


        elif user_choice.upper() == "D":
            print("All Power to Foreward Faceing Weapons and Fire! ")
            pdamage = pdamage + random.randrange(80, 320)
            print("the Baron now has " + str(hp - pdamage), "hit points left")
            badamage = badamage + random.randrange(120, 210)
            print("You have " + str(player_hp - badamage), "hit points left")
            beam_coils = beam_coils - random.randrange(2, 4)


        elif user_choice.upper() == "C":
            print("You regenerate hull plating ")
            player_hp = 450
            print("You now have: " + str(player_hp))
            


        elif user_choice.upper() == "A":
            print("You attack with your weapons")
            pdamage = pdamage + random.randrange(40, 160)
            print("The Baron now has " + str(hp - pdamage), "hit points left")
            badamage = badamage + random.randrange(60, 150)
            print("You have " + str(player_hp - badamage), "Hit Points Left")
            beam_coils = beam_coils - int(1)

        elif user_choice.upper() == "E":
            print("Current HP: " + str(player_hp))
            print("Beam Coils Left: " + str(beam_coils))

        if hp - pdamage < 0:
            print("Baron has been destroyed")
            done = True

        if player_hp - badamage < 0:
            print("Your ship has been destroyed")
            done = True

        if beam_coils <= 0:
            print("You suffered a beam overload due to lack of charges")
            done = True


Baron()