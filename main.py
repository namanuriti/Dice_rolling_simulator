#imports
from random import randint
#Sides dictionary
Dice_sides = {1 : '\n\n   *   \n\n', 2 : '\n*    \n\n    *\n', 3 : '\n*    \n  *  \n    *\n', 4 : '\n*   *\n\n*   *\n', 5 : '\n*   *\n  *  \n*   *\n', 6 : '\n*   *\n*   *\n*   *\n'}
#Code
print('                                                            Dice Rolling Simulator')#60 spaces to get in middle
while True:
    Entry = input("Press 'Enter' key to Roll the dice\n(OR)enter 'q' key to quit:- ")
    if Entry == '':
        print(f"{Dice_sides[randint(1, 6)]}")
    elif Entry == 'q':
        break
    else:
        print(f"{Dice_sides[randint(1, 6)]}")