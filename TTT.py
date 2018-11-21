def print_board(board_list):
	print("\n " + str(board_list[0]) + " | " + str(board_list[1]) + " | " + str(board_list[2]))
	print("----------")
	print(" " + str(board_list[3]) + " | " + str(board_list[4]) + " | " + str(board_list[5]))
	print("----------")
	print(" " + str(board_list[6]) + " | " + str(board_list[7]) + " | " + str(board_list[8]))

def winner(b):
	#check horizontally
	if ( (b[0] == b[1]) and (b[1] == b[2]) ): 
		return 1
	if ( (b[3] == b[4]) and (b[4] == b[5]) ):
		return 1
	if ( (b[6] == b[7]) and (b[7] == b[8]) ):
		return 1
	#check vertically
	if ( (b[0] == b[3]) and (b[3] == b[6]) ):
		return 1
	if ( (b[1] == b[4]) and (b[4] == b[7]) ):
		return 1
	if ( (b[2] == b[5]) and (b[5] == b[8]) ):
		return 1
	#check diagonally
	if ( (b[0] == b[4]) and (b[4] == b[8]) ):
		return 1
	if ( (b[2] == b[4]) and (b[4] == b[6]) ):
		return 1
	#no winner
	return 0

def check_input(inp, bint):
	inputset = {"1","2","3","4","5","6","7","8","9"}

	if (inp not in inputset):
		return 0
	if ( (bint[int(inp)-1] == "X") or (bint[int(inp)-1] == "O") ):
		return 0
	return 1



board = ["1","2","3","4","5","6","7","8","9"]

while winner(board) == 0:
	print_board(board)
	print("\nX: Please enter cell number")
	user_input = input()
	
	while check_input(user_input, board) == 0:
		print("Invalide input, please try again")
		user_input = input()
	
	board[int(user_input) - 1] = "X"

	if winner(board) == 1:
		print_board(board)
		print("\nX wins!\n")
		break

	print_board(board)
	print("\nO: Please enter cell number")
	user_input = input()
	
	while check_input(user_input, board) == 0:
		print("Invalide input, please try again")
		user_input = input()
	
	board[int(user_input) - 1] = "O"

	if winner(board) == 1:
		print_board(board)
		print("\nO wins!\n")
		break