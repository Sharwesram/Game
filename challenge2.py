import random

board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():

   for row in board:

     print("| " + " | ".join(row) + " |")

while True:

   print_board()

   co = int(input("Enter the column (1-3): ")) - 1

   r = int(input("Enter the row (1-3): ")) - 1

   xo = input("Do you want X or O: ").upper()

   if xo not in ["X", "O"]:

     print("Enter only X or O!")

     break

   if board[r][co] == " ":

     board[r][co] = xo

   else:

    print("That spot is already taken!")

    continue

   com = "O" if xo == "X" else "X"

   while True:

     move_row = random.randint(0, 2)

     move_col = random.randint(0, 2)

     if board[move_row][move_col] == " ":

        board[move_row][move_col] = com

        break

cg=random.randint(1,200)
nog=0
print("You should Guess numbers between 1 - 200 !")
while True:
    if cg % 2==0:
        print("Clue : THE NUMBER THAT COMPUTER THINKS IS AN EVEN NUMBER ! ")
    else:
        print("Clue : THE NUMBER THAT COMPUTER THINKS IS AN ODD NUMBER ! ")
    yg=int(input("Guess a Number : "))
    if yg == cg :
        nog += 1
        print(f"You Guessed It Correctly in your attempt {nog} !")
        print(f"Computer'S Number = {cg}")
        quit()
    elif yg > cg :
        nog += 1
        print("The number you guessed is higher than the number that the computer guessed.")
    elif yg < cg :
        nog += 1
        print("The number you guessed is lesser than the number that the computer guessed.")
    h=0

    if nog > 10:
        quit()
