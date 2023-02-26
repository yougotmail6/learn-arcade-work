<<<<<<< HEAD
import random
A = 1
D = 4



def RNG_Gen():
    random.randrange(20)

RNG_Gen()

def Surrender():
    input(D)

Surrender()

def Straight():
    input(A)
    print("Straight", RNG_Gen())
Straight()



def main():
    print("Welcome to A Game called Camel")
    print("A Game that you guessed it involves a Camel!")
    print("In fact you, yes you! Commited a Felony of stealing a Camel. Now you need to get out.")
    print("Using your stolen Camel, need to escape through the desert to the criminal den.")

main()

input()

def The_Getaway():
    print("In order to get out of the stable, you have three options, left, right, and straight")
    A = print("Straight")
    B = print("Right")
    C = print("Left")
    D = print("Surrender to authorities.")

    if input():

        if input(D):
            Surrender()

        if input(A):
            Straight()


The_Getaway()

=======
# This is a WIP,it is very buggy.

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


        if natives>=-15:# Switch to range between 0 to -15. Also add Player Distance.
            print("The Natives are locating your position")
            

        elif natives>=0:# Add in Player Distance
            print(" The Natives shot you with a posion tipped arrow, Game Over!!")
            done=True


        if miles_traveled>200:
            print("Congratulations you just commited a Felony!!")
            done=True



main()



>>>>>>> 200d425c320b33fb6484f49a7e2d5b66c825b9b7
