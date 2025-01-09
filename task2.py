"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
def title():
    print("pick a number between 1 and 100, one makes you lose, the rest are fine, if you get it right try again with 50, then 25, then 15, them 10, 9, 8, 7, 6, 5, 4, 3, then finally 2")

def game():
    carolina = int(input("pick a number from 1 to 100 => "))
    bryce = random.randint(1, 100)
    if bryce == carolina:
        print("you are OUT!!!")
    elif carolina >= 101:
        print("really man, that not in the range")
    elif carolina <= 0:
        print("really man, that not in the range")
    else:
        detroit = int(input("pick a number from 1 to 50 => "))
        tua = random.randint(1, 50)
        if detroit == tua:
            print("you are OUT!!!")
        elif detroit >= 51:
            print("really man, that not in the range")
        elif detroit <= 0:
            print("really man, that not in the range")
        else:
            viking = int(input("pick a number from 1 to 25 => "))
            sanders = random.randint(1, 25)
            if viking == sanders:
                print("you are OUT!!!")
            elif viking >= 26:
                print("really man, that not in the range")
            elif viking <= 0:
                print("really man, that not in the range")
            else:
                falcon = int(input("pick a number from 1 to 15 => "))
                miles = random.randint(1, 15)
                if falcon == miles:
                    print("you are OUT!!!")
                elif falcon >= 16:
                    print("really man, that not in the range")
                elif falcon <= 0:
                    print("really man, that not in the range")
                else:
                    chiefs = int(input("pick a number from 1 to 10 => "))
                    mahomie = random.randint(1, 10)
                    if chiefs == mahomie:
                        print("you are OUT!!!")
                    elif chiefs >= 11:
                        print("really man, that not in the range")
                    elif chiefs <= 0:
                        print("really man, that not in the range")
                    else:
                        bills = int(input("pick a number from 1 to 9 => "))
                        allen = random.randint(1, 9)
                        if bills == allen:
                            print("you are OUT!!!")
                        elif bills >= 10:
                            print("really man, that not in the range")
                        elif bills <= 0:
                            print("really man, that not in the range")
                        else:
                            eagles = int(input("pick a number from 1 to 8 => "))
                            saquon = random.randint(1, 8)
                            if eagles == saquon:
                                print("you are OUT!!!")
                            elif eagles >= 9:
                                print("really man, that not in the range")
                            elif eagles <= 0:
                                print("really man, that not in the range")
                            else:
                                chargers = int(input("pick a number from 1 to 7 => "))
                                texans = random.randint(1, 7)
                                if chargers == texans:
                                    print("you are OUT!!!")
                                elif chargers >= 8:
                                    print("really man, that not in the range")
                                elif chargers <= 0:
                                    print("really man, that not in the range")
                                else:
                                    joe = int(input("pick a number from 1 to 6 => "))
                                    alt = random.randint(1, 6)
                                    if joe == alt:
                                        print("you are OUT!!!")
                                    elif joe >= 7:
                                        print("really man, that not in the range")
                                    elif joe <= 0:
                                        print("really man, that not in the range")
                                    else:
                                        james = int(input("pick a number from 1 to 5 => "))
                                        cook = random.randint(1, 5)
                                        if james == cook:
                                            print("you are OUT!!!")
                                        elif james >= 6:
                                            print("really man, that not in the range")
                                        elif james <= 0:
                                            print("really man, that not in the range")
                                        else:
                                            lebron = int(input("pick a number from 1 to 4 => "))
                                            curry = random.randint(1, 4)
                                            if lebron == curry:
                                                print("you are OUT!!!")
                                            elif lebron >= 5:
                                                print("really man, that not in the range")
                                            elif lebron <= 0:
                                                print("really man, that not in the range")
                                            else:
                                                denver = int(input("pick a number from 1 to 3 => "))
                                                nuggets = random.randint(1, 3)
                                                if denver == nuggets:
                                                    print("you are OUT!!!")
                                                elif denver >= 4:
                                                    print("really man, that not in the range")
                                                elif denver <= 0:
                                                    print("really man, that not in the range")
                                                else:
                                                    boobiemileshotasthesummer = int(input("pick a final number from 1 to 2, if you get it right you win!!! => "))
                                                    hekeepatreat = random.randint(1, 2)
                                                    if boobiemileshotasthesummer == hekeepatreat:
                                                        print("YOU ARE OOOUUUUUUTTTTTT!!!!")
                                                    elif boobiemileshotasthesummer >= 3:
                                                        print("really man, that not in the range")
                                                    elif boobiemileshotasthesummer <= 0:
                                                        print("really man, that not in the range")
                                                    else:
                                                        print(" you win, the odds of this happening was around 8.6%. CONGRATULATIONS!!!!")

bigmac = "t"
while bigmac != "S":
    bigmac = input("press I for instructions or S to start the game => ")
    if bigmac == "I":
        title()

game()

