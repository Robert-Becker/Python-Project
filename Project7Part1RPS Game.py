"""
Original Code Written By Robert Becker
Created on July 17, 2019
Last Modified on July 17, 2019
Program was designed to play RPS
Project7 Part1
"""

import random


def game_rps():
    nums = [x for x in range(1, 4)]
    random.shuffle(nums)
    print("\nWELCOME TO ROCK PAPER SCISSORS!!!")
    print("To Play, Enter the number next to the move you wish to make!")
    selection = float(input("What's your move!? Rock(1) Paper(2) or Scissors(3): "))

    if selection == 1:
        if nums[0] is 1:
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print(" <> <> <> <> <>  ROCK vs ROCK <> YOU TIED! <> <> <> <> <> ")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            game_rps()
        elif nums[0] is 2:
            print(">< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< ")
            print("  >< X >< X ><  ROCK vs PAPER >< YOU LOSE!  >< X >< X >< ")
            print(">< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< ")
            game_rps()
        elif nums[0] is 3:
            print("<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3")
            print(" <3 <3 <3 <3   ROCK vs SCISSORS <3 YOU WIN!  <3 <3 <3 <3")
            print("<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3")
            game_rps()
    elif selection == 2:
        if nums[0] is 1:
            print("<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3")
            print(" <3 <3 <3 <3  PAPER vs ROCK <3 YOU WIN!  <3 <3 <3 <3 <3 ")
            print("<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3")
            game_rps()
        elif nums[0] is 2:
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print(" <> <> <> <>     PAPER vs PAPER <> YOU TIED!    <> <> <> <> ")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            game_rps()
        elif nums[0] is 3:
            print(">< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X")
            print(">< X >< X ><   PAPER vs SCISSORS >< YOU LOSE!   X >< X >< X")
            print(">< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X")
            game_rps()
    elif selection == 3:
        if nums[0] is 1:
            print(">< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X")
            print("  X >< X >< X    SCISSORS vs ROCK >< YOU LOSE!   X >< X >< ")
            print(">< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X >< X")
            game_rps()
        elif nums[0] is 2:
            print("<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3")
            print(" <3 <3 <3 <3   SCISSORS vs PAPER <3 YOU WIN!   <3 <3 <3")
            print("<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3")
            game_rps()
        elif nums[0] is 3:
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print(" <> <> <>   SCISSORS vs SCISSORS <> YOU TIED!  <> <> <> ")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            game_rps()
    else:
        print(" <(-_-)> <(-_-)> <(-_-)> <(-_-)> <(-_-)> <(-_-)>")
        print("  <(-_-)> <(-_-)> Illegal Move! <(-_-)> <(-_-)>")
        print(" <(-_-)> <(-_-)> <(-_-)> <(-_-)> <(-_-)> <(-_-)>")
        game_rps()


game_rps()
