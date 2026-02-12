# # import random
# # a=("| | | |")
# # b=("| | | |")
# # c=("| | | |")


# # while True :
# #     co=int(input("Enter the column 1 or 2 or 3:"))
# #     r=int(input("Enter the row 1 or 2 or 3:"))
# #     xo=str(input("Do you want x or o:")).upper()
# #     you=xo
# #     com=""
# #     if xo == "o".upper():
# #         com += "X"
# #     elif xo == "x".upper():
# #         com += "O".lower()
# #     else:
# #         print("Enter only X or O !")
# #         quit()
# #     move=random.randint(0,3)
# #     move2=random.randint(0,3)

# #     if co==1:
# #         t=list(a)
# #         t[r]=xo
# #         print(tuple(t))
# #         print(b)
# #         print(c)

    

# # import random

# board = [[" " for _ in range(3)] for _ in range(3)]

# # def print_board():

# for row in board:

#     print("| " + " | ".join(row) + " |")

# print(board)

# #   print_board()

# #   co = int(input("Enter the column (1-3): ")) - 1

# #   r = int(input("Enter the row (1-3): ")) - 1

# #   xo = input("Do you want X or O: ").upper()

# #   if xo not in ["X", "O"]:

# #     print("Enter only X or O!")

# #     break

# #   if board[r][co] == " ":

# #    board[r][co] = xo

# #   else:

# #    print("That spot is already taken!")
# #    continue

# #   com = "O" if xo == "X" else "X"

# #   while True:

# #    move_row = random.randint(0, 2)

# #    move_col = random.randint(0, 2)

# #    if board[move_row][move_col] == " ":

# #      board[move_row][move_col] = com

# #      break
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