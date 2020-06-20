
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

def draw_screen(screen, is_pause):
	user = screen[0]
	playing_hands = screen[1]
	community_cards = screen[2]
	tutorial_msg = screen[3]

	util.clear_screen()
	to_draw = str(user) + playing_hands + str(community_cards) + tutorial_msg
	print(to_draw)
	if is_pause:
		util.process_continuation_input(to_draw)

def get_user_guess(screen):
	guess = ""
	draw_screen(screen, is_pause=False)
	while guess not in list("123456789") :
		guess =  \
			input("Who's the winner? (use the player's number as your guess) ")
		if guess == "q":
			exit()
		if guess == "r":
			ascii.show_rankings()
			draw_screen(screen, is_pause=False)
	print("user guess:", guess)
	return int(guess)

def is_guess_in_players(guess, players):
	for p in players:
		if p.id == guess:
			return True
	return False

def is_right_guess(guess, winners):
	print("is_right_guess")
	return is_guess_in_players(guess, winners)

def process_user_guess(guess, user, winners):
	if is_right_guess(guess, winners):
		user.score += 2
		result_message = "\n\nYou're right!"
		print("You're right!")
	else:
		user.lives -= 1
		result_message = "\n\nSorry, keep trying!"
		print("Sorry!")
	return result_message

def congratulate_winner(screen, winners, guess_msg):
	winner_message = guess_msg + "\n" + get_showdown(winners)	
	if len(winners) == 1:
		winner_message += "has the best hand!"
	else:
		winner_message += "have the best hand!"
		
	screen[3] += winner_message                       
	draw_screen(screen, is_pause=True)

def get_showdown(players):
	res_str = ""
	for p in players:
		res_str += p.showdown_hand + "\n"
	return res_str
		
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
		tutorial_msg = ""
			
		playing_hands = ""
		for player in players:
			playing_hands += player.hand_stringify() + "\n\n"

		screen = [user, playing_hands, community_cards, tutorial_msg]

		community_cards.append([Card('A', Suit.clubs),                 \
								Card('A', Suit.spades),                 \
								Card('A', Suit.hearts),                 \
								Card('K', Suit.diamonds),                 \
								Card('2', Suit.spades)])
        				
		draw_screen(screen, is_pause=True)

		winners = ranker.find_winners(players, community_cards)
		if is_tutorial:
			screen[3] = "\n\nPossible winners:\n" + get_showdown(players)	
		guess = \
			get_user_guess(screen)
		guess_msg = process_user_guess(guess, user, winners)
		congratulate_winner(screen, winners, guess_msg)

		util.clear_player_hands(players)
		if user.lives <= 0 or user.score >= 100:
			break

	print( "Final score:", user.score, "great Job!" )
        				
