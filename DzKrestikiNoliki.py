board_size = 3
board = [1,2,3,4,5,6,7,8,9]


def draw_board():
	print (('_' * 4 * board_size ))
	for i in range(board_size):
		print ((' ' * 3 + '|') * 3)
		print ('',board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
		print (('_' * 3 + '|') * 3)

def check_win():
	win = False

	win_combination = (
		(0,1,2), (3,4,5), (6,7,8),
		(0,3,6), (1,4,7), (2,5,8),
		(0,4,8), (2,4,6)
	)

	for pos in win_combination:
		if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X','O')):
			win = board[pos[0]]

	return win

def game_step(index, char):
	if (index > 10 or index < 1 or board[index-1] in ('X','O')):
		return False

	board[index-1] = char
	return True

def start_game():
	current_player = 'X'
	step = 1

	draw_board()

	while (step < 9) and (check_win() == False):
		index = input('Ходит ' + current_player + '. Введите номер поля (0 - выход):')

		if (int(index) == 0):
			break

		if (game_step(int(index), current_player)):
			print('Удачный ход')

			if (current_player == 'X'):
				current_player = 'O'
			else:
				current_player = 'X'

			draw_board()
			step += 1
		else:
			print('Неверный номер! Повторите!')

	if (step == 9):
		print('Игра оконцена. Ничья!')
	else:
		print('Выиграл ' + check_win())

print('Добро пожаловать в игру!')
start_game()