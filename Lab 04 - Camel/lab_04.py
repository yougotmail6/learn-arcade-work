import random

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the natives.\n")

    done = False
    miles_traveled = 0
    thirst = 0
    Camel_Tiredness = 0
    natives = -20
    drinks = 3
    oasis = 7

    while done==False:
        print("""A. Drink from your canteen.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop and rest.
        E. Status check.
        Q. Quit.\n""")

        user_choice = input("Please pick one! ")


        if user_choice.upper() == "Q":
            print("You have Alt-Fd'd")
            break

        elif user_choice.upper() == "E":
            print("Trip so far " + str(miles_traveled) + " Miles ")
            print("You have " + str(drinks) + " Drinks Left ")
            print("Natives Are " + str(miles_traveled - natives) + (" Miles Behind you "))
            

        elif user_choice.upper() == "D":
            Camel_Tiredness = 0
            print(" Your Camel is rested and very Happy! ")
            natives = natives+random.randrange(7,14)
            print("Natives are " + str(miles_traveled - natives) + (" miles behind you "))


        elif user_choice.upper() == "C":
            print("Your Camel is very fast!")
            miles_traveled=miles_traveled+random.randrange(10,20)
            thirst=thirst+1
            Camel_Tiredness=Camel_Tiredness+random.randrange(1,3)
            natives = natives+random.randrange(7,14)
            print("Natives are " + str(miles_traveled - natives) + (" miles behind you "))


        elif user_choice.upper() == "B":
            print("Your Camel has some good pace, but it is Capable of going Faster!")
            miles_traveled=miles_traveled+random.randrange(5,12)
            thirst=thirst+1
            Camel_Tiredness=Camel_Tiredness+1
            natives = natives+random.randrange(7,14)
            print("Natives are " + str(miles_traveled - natives) + (" miles behind you "))

        elif user_choice.upper() == "A":
            if drinks>0:
                thirst=0
                drinks=drinks-1
                print(" Oh that's good ")
            else: 
                print(" You are dry ")

        


        if thirst>6:
            print("You died from dehydration!")
            done=True
            break

        elif thirst>4:
            print("You are dehydrated!")

        if Camel_Tiredness>8:
            print("You know you not only stole a Camel, but also killed one to? Yeah I know, such a perfect example of Animal Abuse in the Wild! I'm just disappointed really. ")
            done=True
            break

        elif Camel_Tiredness>5:
            print(" The Camel is starting to slow down. ")


        if natives<15:
            print("The Natives are locating your position")
            

            if natives>0:
                print(" The Natives shot you with a posion tipped arrow, Game Over!!")
                done=True
                break


        if miles_traveled>200:
            print("Congratulations you just commited a Felony!!")
            done=True



main()



