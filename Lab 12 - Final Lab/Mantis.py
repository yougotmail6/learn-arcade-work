# Mantis is not capable of using normal phasers, and can only do full power


import random


def main():
    print("You hear the souls praying to the Mantis.")

    done = False
    hp = 350
    pdamage = 0
    mdamage = 0
    player_hp = 450

    while done == False:
        print("""
        A. Attack
        B. Regenerate Shield
        C. Full Power to Phasers""")

        user_choice = input("Please pick one! ")

        # if user_choice.upper() == "B":
        ##  shield=shield+random.randrange(10,20)
        # print("You know have " + str (shield), "Shields")

        if user_choice.upper() == "C":
            print("All Power to Foreward Faceing Weapons and Fire! ")
            pdamage = pdamage + random.randrange(80, 320)
            print("the Mantis now has " + str(hp - pdamage), "hit points left")
            mdamage = mdamage + random.randrange(110, 200)
            print("You have " + str(player_hp - mdamage), "hit points left")

        elif user_choice.upper() == "A":
            print("You attack with your weapons")
            pdamage = pdamage + random.randrange(40, 160)
            print("The Mantis now has " + str(hp - pdamage), "hit points left")
            mdamage = mdamage + random.randrange(110, 200)
            print("You have " + str(player_hp - mdamage), "Hit Points Left")

        if hp - pdamage < 0:
            print("Mantis has been destroyed")
            done = True

        if player_hp - mdamage < 0:
            print("Your ship has been destroyed")
            done = True


main()