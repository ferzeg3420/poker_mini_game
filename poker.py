#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# Attributions to slideshare for the neat list comprehensions

from card_h import Card, Suit, Blind
from community_cards_h import *
from deck_h import *
from player_h import *
from user_h import *
import util
import ranker

def get_user_state(score, lives):
	return "\t\t\tScore/Level: " + str(score) + " lives: " + str(lives) + "\n"

def preflop(screen):
	util.clear_screen()
	util.print_preflop(screen)
	util.process_continuation_input(screen)

def flop(screen, community_cards, deck):
	community_cards.append(deck.deal_flop_as_list())
	util.clear_screen()
	screen_tmp = screen + community_cards.get_flop()
	print(screen_tmp)
	util.process_continuation_input(screen_tmp)

def turn(screen, community_cards, deck):
	community_cards.append(deck.deal_card())
	util.clear_screen()
	screen_tmp = screen + community_cards.get_flop_turn()
	print(screen_tmp)
	util.process_continuation_input(screen_tmp)

def river(screen, community_cards, deck):
	community_cards.append(deck.deal_card())
	util.clear_screen()
	screen_tmp = screen + community_cards.get_flop_turn_river()
	print(screen_tmp)
	util.process_continuation_input(screen_tmp)

def get_user_guess():
	user_guess = ""
	while user_guess not in list("123456789") :
		user_guess =  \
			input("Who's the winner? (use the player's number as your guess) ")
		if user_guess == "q":
			exit()
	return user_guess

def is_right_guess(guess, winners):
	return int(guess) in winners

def process_user_guess(user, winners):
	user_guess = get_user_guess()
	if is_right_guess(user_guess, winners):
		user.score += 1
		result_message = "\n\nYou're right!"
	else:
		user.lives -= 1
		result_message = "\n\nSorry, keep trying!"
	return result_message

def congratulate_winner(screen, community_cards, winners, guess_msg):
	winners_str = ""
	for w in winners:
		winners_str += str(w) + " "
	winner_message = "\n\nPlayer(s) " \
					+ winners_str      \
					+ "has(have) the highest card!"
	screen_tmp = screen                                  \
			     + community_cards.get_flop_turn_river() \
			     + winner_message                        \
			     + guess_msg                       
	util.clear_screen()
	print(screen_tmp)
	util.process_continuation_input(screen_tmp)
	
		
if __name__ == "__main__":
	util.clear_screen()
	print("FERNANDO'S SUPER POKER SIMULATOR 3000")
	user = User(score=0, lives=3)
	deck = Deck()
	num_players = util.get_num_players()
	level = num_players - 1
	
	while True:	
		community_cards = Community_cards()
		deck.shuffle()
		players = [ Player(i) for i in range(1, num_players + 1) ]
		deck.deal_player_hands(players)
			
		playing_hands = ""
		for player in players:
			playing_hands += player.hand_stringify() + "\n\n"

		screen = str(user) + playing_hands
		
		preflop(screen)
		flop(screen, community_cards, deck)			
		turn(screen, community_cards, deck)	
		river(screen, community_cards, deck)

		best_card, winners = ranker.get_high_card_from_players(players, \
															   community_cards)
		guess_msg = process_user_guess(user, winners)
		screen = str(user) + playing_hands
		congratulate_winner(screen, community_cards, winners, guess_msg )

		util.clear_player_hands(players)
		if user.lives <= 0 or user.score >= 100:
			break

	print( "Final score:", user.score, "great Job!" )
        				
