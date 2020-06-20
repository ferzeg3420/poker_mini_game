# Attributions to slideshare for the neat list comprehensions
# more attributions

from card_h import Card, Suit, Blind
from community_cards_h import *
from deck_h import *
from player_h import *
from user_h import *
import util
import ranker
import ascii

def get_level(score):
	return (score // 10) + 1

def get_num_players(level):
	if level > 8:
		return 9
	else:
		return level + 1

def display_table(screen, community_cards):
	util.clear_screen()
	screen_tmp = screen + str(community_cards)
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
		user.score += 5
		result_message = "\n\nYou're right!"
	else:
		user.lives -= 1
		result_message = "\n\nSorry, keep trying!"
	return result_message

def congratulate_winner(screen, community_cards, winners, guess_msg):
	winners_str = ""
	for i, w in enumerate(winners, start=1):
		if len(winners) == 2 and i == 1:
			winners_str += str(w) + " and "
		elif len(winners) == i:
			winners_str += str(w)
		elif len(winners) == i + 1:
			winners_str += str(w) + ", and "
		elif len(winners) != 1:
			winners_str += str(w) + ", "
		else:
			winners_str += str(w)
		
	if len(winners) == 1:
		winner_message = "\n\nPlayer " \
						+ winners_str      \
						+ " has the best hand!"
	else:
		winner_message = "\n\nPlayer " \
						+ winners_str      \
						+ " have the best hand!"
		
	screen_tmp = screen                                  \
			     + str(community_cards)                  \
			     + winner_message                        \
			     + guess_msg                       
	util.clear_screen()
	print(screen_tmp)
	util.process_continuation_input(screen_tmp)
	
		
if __name__ == "__main__":
	util.clear_screen()
	ascii.print_welcome()
	user = User(score=0, lives=3)
	deck = Deck()
	level = 1
	is_tutorial = util.is_tutorial_mode()
	
	while True:	
		level = get_level(user.score)
		num_players = get_num_players(level)
		community_cards = Community_cards()
		deck.shuffle()
		players = [ Player(i) for i in range(1, num_players + 1) ]
		deck.deal_player_hands(players)
			
		playing_hands = ""
		for player in players:
			playing_hands += player.hand_stringify() + "\n\n"

		screen = str(user) + playing_hands

		community_cards.append([Card('A', Suit.spades),                 \
								Card('A', Suit.spades),                 \
								Card('A', Suit.spades),                 \
								Card('A', Suit.spades),                 \
								Card('2', Suit.spades)])
		display_table(screen, community_cards) 


		winners = ranker.find_winners(players, community_cards, is_tutorial)
		guess_msg = process_user_guess(user, winners)
		screen = str(user) + playing_hands
		congratulate_winner(screen, community_cards, winners, guess_msg)

		util.clear_player_hands(players)
		if user.lives <= 0 or user.score >= 100:
			break

	print( "Final score:", user.score, "great Job!" )
        				
