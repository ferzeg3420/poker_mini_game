from os import system
import ascii
import sys
is_windows = hasattr(sys, 'getwindowsversion')

def clear_screen():
	if is_windows:
		system('cls')
	else:
		system('clear')

def lives_2_hearts(lives):
	hearts_str = ""
	if is_windows:
		for i in range(lives):
			hearts_str += "♥"
		for i in range(lives):
			hearts_str += " "
	else:
		for i in range(lives):
			hearts_str += "♥"
		for i in range(3 - lives):
			hearts_str += "♡"
	return hearts_str	

def get_num_players_from_user(): # deprecated?
	num_players = 0
	while num_players < 1 or num_players > 9:
		print("Select the number of players (1-9). Enter q to exit: ")
		num_players_str = input()
		if num_players_str == "q":
			exit()
		if num_players_str == "":
			continue
		if len(num_players_str) > 1 or num_players_str not in "123456789":
			continue
		num_players = int(num_players_str)
	return num_players

def is_tutorial_mode(): 
	answer = 'x'
	while answer != 'y' and answer != 'n':
		print("Would you like to play in tutorial mode? (y/n) q to exit")
		answer = input()
		if answer == "":
			continue
		if answer == "q":
			exit()
	return answer == 'y'

def clear_player_hands(players):
	for player in players:
		player.fold()

def process_continuation_input(state):
	while True:
		user_input = input("")
		if user_input == 'q':
			clear_screen()
			exit()
		elif user_input == 'r':
			ascii.show_rankings()
		else:
			break
		print(state)
	
def print_preflop(board_state):
	print(board_state + "\n\n\n\n\n\n\n\nPre-flop")
