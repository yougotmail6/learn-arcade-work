
import random





def Gorilla():

    
    
    print \
        (" The sounds of Monkeys appraching sparks your intrest. The Gorrila is a foremidable opponent, capable of prolonging battle and dealing as much damage as possible.")


    done = False
    hp = 800
    pdamage = 0
    gdamage = 20
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
            pdamage =pdamage +random.randrange(80 ,320)
            print("the Gorrilla now has " + str(hp -pdamage), "hit points left")
            print("You have " + str(player_hp -gdamage), "hit points left")

        elif user_choice.upper() == "A":
            print("You attack with your weapons")
            pdamage =pdamage +random.randrange(40 ,160)
            print("The Gorrila now has " + str(hp -pdamage), "hit points left")
            print("You have " + str(player_hp -gdamage), "Hit Points Left")


        if hp -pdamage <0:
            print("Gorrila has been destroyed")
            done = True

        if player_hp -gdamage <0:
            print("Your ship has been destroyed")
            done = True


Gorilla()
