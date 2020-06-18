from card_h import *
import community_cards_h
import player_h

def combine_cards(player, community_cards):
	player_hand = player.get_hand()
	return player_hand + community_cards.cards

def score_repeated_helper(repeated_cards):
	is_pair = False
	is_two_pair = False
	is_three_of_a_kind = False
	is_four_of_a_kind = False
	is_full_house = False

	repetitions = 0
	for card, reps in repeated_cards:
		print(card, reps)
		if (is_pair and reps == 3) or (is_three_of_a_kind and reps == 2):
			is_full_house = True# full house
		elif is_pair and reps == 2:
			is_two_pair = True
		elif reps == 2:
			is_pair = True
		elif reps == 3:
			is_three_of_a_kind = True
		elif reps == 4:
			print("Four of a kind")
			return 80000000000 # four of a kind
	
	if is_full_house:
		print("Full house", )
		return 70000000000
	elif is_three_of_a_kind:
		print("Three of a kind")
		return 40000000000
	elif is_two_pair:
		print("Two pair")
		return 30000000000
	elif is_pair:
		print("One pair")
		return 20000000000

def find_best_flush(player, community_cards):
	combined_cards = combine_cards(player, community_cards)
	combined_cards.sort(reverse=True, key=lambda c: (c.suit.value, c))
	num_repeated_suit = 0
	is_flush = False
	flushes = []
	last_card = combined_cards[0]
	for i, c in enumerate(combined_cards):
		if c.suit == last_card.suit:
			num_repeated_suit += 1
		else:
			num_repeated_suit = 0
		if num_repeated_suit == 5:
			flushes.append(combined_cards[:i][:5])
			is_flush = True
		if num_repeated_suit == 6:
			flushes.append(combined_cards[:i][:5])
		if num_repeated_suit == 7:
			flushes.append(combined_cards[:i][:5])
		last_card = c
	
	if is_flush:
		print("Found best flush", flushes[0])
		return flushes[0]
	else: 
		return []

def check_flush(cards):
	cards.sort(reverse=True, key=lambda c: c.suit.value)
	last_suit = cards[0].suit
	for c in cards:
		if c.suit != last_suit:
			return False
	print("Straight flush!")
	return True

def get_aces(cards):
	aces = []
	for c in cards:
		if c.value_as_int() == 14:
			aces.append(c)
	return aces
		

def find_straights(player, community_cards):
	combined_cards = combine_cards(player, community_cards)
	combined_cards.sort(reverse=True)
	last_card = Card('0', Suit.spades) # empty card
	cards_in_straight = 0
	straights = []
	straight = []
	for c in combined_cards:
		last_c_val = last_card.get_value_as_int()
		c_val = c.get_value_as_int()
		if (last_c_val == c_val - 1):
			cards_in_straight += 1
			straight.append(c)
		elif (last_c_val == 2 and cards_in_straight == 4):
			aces = get_aces(combined_cards)
			for a in aces:
				straights.append(straight + [ a ] )
		else:
			cards_in_straight = 0
			straight = []
		if cards_in_straight >= 5:
			straights.append(straight[-5:])
	if len(straights) > 0:
		print("Found straights:", straights)
	return straights

def score_repeated_cards(player, community_cards):
	combined_cards = combine_cards(player, community_cards)
	combined_cards.sort(reverse=True)
	repetitions = 0
	last_card = Card('0', Suit.spades) # empty card
	reps = []
	for c in combined_cards:
		if last_card == c:
			repetitions += 1
		else:
			if repetitions >= 1:
				reps.append([last_card, repetitions + 1])
			repetitions = 0
		last_card = c
	if len(reps) == 0: # error
		score, high_hand = score_high_card(player, community_cards)
		print("high_card:", high_hand)
		return score
	return score_repeated_helper(reps)
		
def score_high_card(player, community_cards):
	combined_cards = combine_cards(player, community_cards)
	combined_cards.sort(reverse=True)
	highest_value_cards = combined_cards[:5]
	score = 10000000000
	for i, c in enumerate(highest_value_cards, start=0):
		score += c.get_value_as_int() * (10 ** (8 - 2 *i))
	return score, highest_value_cards

def get_hand_score(player, community_cards):
	score = 0
	straights = find_straights(player, community_cards)
	for s in straights:
		if( check_flush(s) ):
			score =  90000000000
	score_tmp = score_repeated_cards(player, community_cards)
	if score_tmp > 60000000000:
		score = score_tmp
	flush = find_best_flush(player, community_cards)
	if len(flush) > 0:
		score = 60000000000
	if len(straights) > 0 and score < 60000000000:
		score = 50000000000
	score = score_tmp
	print("player", player.id, "score:", score)
	input()
	return score

def find_winners(players, community_cards):
	cc = community_cards
	scored_players =  \
		[ [i, get_hand_score(p, cc)] for i, p in enumerate(players, start=1) ]
	scored_players.sort(reverse=True, key=lambda c: c[1])
	highest_score = scored_players[0][1]
	i = 0
	winners = []
	for player, score in scored_players:
		if score < highest_score:
			break
		winners.append(player)
	return winners
