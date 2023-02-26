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

