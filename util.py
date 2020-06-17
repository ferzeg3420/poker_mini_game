from os import system
import sys

def clear_screen():
	is_windows = hasattr(sys, 'getwindowsversion')
	if is_windows:
		system('cls')
	else:
		system('clear')

def print_rankings():
	clear_screen()
		
	print()
	print("     ♤ ♡ ♢ ♧ Hand Rankings ♠ ♥ ♦ ♣")
	print()
	
	print(" Royal Flush")
	print(" | A♠  | | K♠  | | Q♠  | | J♠  | | 10♠ |")
	print()
	
	print(" Straight Flush")
	print(" | 9♢  | | 8♢  | | 7♢  | | 6♢  | | 5♢  |")
	print()
	
	print(" Four of a Kind")
	print(" | A♣  | | A♡  | | A♠  | | A♢  | | 10♠ |")
	print()
	
	print(" Full House")
	print(" | Q♡  | | Q♠  | | Q♢  | | J♣  | | J♢  |")
	print()
	
	print(" Flush")
	print(" | A♡  | | J♡  | | 9♡  | | 6♡  | | 3♡  |")
	print()
	
	print(" Straight")
	print(" | 9♣  | | 8♢  | | 7♠  | | 6♢  | | 5♠  |")
	print()
	
	print(" Three of a Kind")
	print(" | 5♢  | | Q♣  | | 2♡  | | 2♠  | | 2♢  |")
	print()
	
	print(" Two Pair")
	print(" | A♡  | | A♣  | | Q♡  | | Q♠  | | 9♢  |")
	print()
	
	print(" One Pair")
	print(" | 4♡  | | 5♠  | | 8♣  | | A♢  | | A♠  |")
	print()
	
	print(" High Card")
	print(" | 5♠  | | 6♢  | | J♣  | | Q♢  | | A♠  |")
	print()
	
	input()
	clear_screen()

def get_num_players():
	num_players = 0
	while num_players < 1 or num_players > 9:
		print("Select the number of players (1-9). Enter q to exit: ")
		num_players_str = input()
		if num_players_str == "":
			continue
		if len(num_players_str) > 1 or num_players_str not in "123456789":
			continue
		if num_players_str == "q":
			exit()
		num_players = int(num_players_str)
	return num_players

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
			print_rankings()
		else:
			break
		print(state)
	
def print_preflop(board_state):
	print(board_state + "\n\n\n\n\n\n\n\nPre-flop")
