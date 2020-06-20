from card_h import *
import community_cards_h
import player_h

STRAIGHT_FLUSH = 90000000000
FOUR_OF_A_KIND = 80000000000
FULL_HOUSE = 70000000000 
FLUSH = 60000000000 
STRAIGHT = 50000000000
THREE_OF_A_KIND = 40000000000 
TWO_PAIR = 30000000000 
PAIR = 20000000000 
HIGH_CARD = 10000000000 

def combine_cards(player, community_cards):
	player_hand = player.get_hand()
	return player_hand + community_cards.cards

def get_aces(cards):
	aces = []
	for c in cards:
		if c.get_value_as_int() == 14:
			aces.append(c)
	return aces

def score_cards(cards):
	score = 0
	for i, c in enumerate(cards, start=0):
		score += c.get_value_as_int() * (10 ** (8 - 2 *i))
	return score

def find_reps_or_high_card(cards):
	cards.sort(reverse=True)
	pairs = []
	no_reps = []
	card_buffer = []
	three_of_a_kind = []
	four_of_a_kind = []
	repetitions = 0

	for i, c in enumerate(cards, start=0):
		if i + 1 >= len(cards):
			next_card = Card('0', Suit.spades)
		else:
			next_card = cards[i + 1]
		if next_card == c:
			if repetitions == 0:
				repetitions = 2
				card_buffer.append(c)
				card_buffer.append(next_card)
			else:
				repetitions += 1
				card_buffer.append(next_card)
		elif repetitions == 2:
			#print("appending pair", card_buffer)
			pairs.append(card_buffer)
			card_buffer = []
			repetitions = 0
		elif repetitions == 3:
			three_of_a_kind.append(card_buffer)
			card_buffer = []
			repetitions = 0
		elif repetitions == 4:
			four_of_a_kind.append(card_buffer)
			card_buffer = []
			repetitions = 0
		elif repetitions == 0:
			no_reps.append(c)
		else:
			print("ERROR")

	if len(four_of_a_kind) > 0:
		hand = four_of_a_kind[0] + no_reps[:1]
		score = FOUR_OF_A_KIND + score_cards(hand)
	elif len(three_of_a_kind) > 0 and len(pairs) > 0:
		hand = three_of_a_kind[0] + pairs[0]
		score = FULL_HOUSE + score_cards(hand)
	elif len(three_of_a_kind) > 0:
		hand = three_of_a_kind[0] + no_reps[:2]
		score = THREE_OF_A_KIND + score_cards(hand)
	elif len(pairs) >= 2:
		hand = pairs[0] + pairs[1] + no_reps[:1]
		score = TWO_PAIR + score_cards(hand)
	elif len(pairs) > 0:
		hand = pairs[0] + no_reps[:3]
		score = PAIR + score_cards(hand)
	else:
		hand = no_reps[:5]
		score = HIGH_CARD + score_cards(hand)
	return score, hand

def check_flush(cards):
	cards.sort(reverse=True, key=lambda c: c.suit.value)
	last_suit = cards[0].suit
	for c in cards:
		if c.suit != last_suit:
			return False
	return True

def branch_duplicates(cards):
	duplicates = []
	deduped_possible_cards = []
	last_card = Card('0', Suit.spades) # empty card
	for i, c in enumerate(cards, start=0):
		if c.get_value_as_int() == last_card.get_value_as_int():
			duplicates.append(i)
		last_card = c
	card_set_buffer = []
	
	if len(duplicates) > 2: # if more than 2 then no possible straight w 7cards
		deduped_possible_cards.append(cards)
		return deduped_possible_cards

	if len(duplicates) == 2:
		d = duplicates[0]
		dd = duplicates[1]
		first_div = cards[:d-1] + cards[d:]	
		second_div = cards[:d] + cards[d+1:]	
		deduped_possible_cards.append(first_div[:d] + first_div[d+1:])
		deduped_possible_cards.append(first_div[:d-1] + first_div[d:])
		deduped_possible_cards.append(second_div[:d] + first_div[d+1:])
		deduped_possible_cards.append(second_div[:d-1] + second_div[d:])

	if len(duplicates) == 1:
		d = duplicates[0]
		deduped_possible_cards.append(cards[:d-1] + cards[d:])
		deduped_possible_cards.append(cards[:d] + cards[d+1:])

	if len(duplicates) == 0:
		deduped_possible_cards.append(cards)
	return deduped_possible_cards
		

def find_straights(cards):
	#print("find_straights", cards)
	cards.sort(reverse=True)
	#print("find_straights sorted:", cards)
	dedupped = branch_duplicates(cards)
	#print("deduped:", dedupped)
	straights = []
	straight = []
	for dd in dedupped:
		for i, c in enumerate(dd, start=0):
			#print("finding straights:", c)
			c_val = c.get_value_as_int()	
			if i+1 >= len(dd):
				next_val = 15 # just to make sure next test fails
			else:
				next_c = dd[i+1]
				next_val = next_c.get_value_as_int()
			if c_val == next_val + 1:
				if len(straight) == 0:
					#print("making straight with", next_val, c_val)
					straight.append(c)
					straight.append(next_c)
				else:
					#print("making straight with", next_val)
					straight.append(next_c)
			elif next_val == 2 and len(straight) == 4:
				aces = get_aces(dd)
				for a in aces:
					straights.append(straight + [ a ] )
			else:
				if len(straight) >= 5:
					straights.append(straight[:5])
				straight = []
	#print("all straights:", straights)
	return straights

def find_best_flush(cards):
	#print("find best flush")
	cards.sort(reverse=True, key=lambda c: (c.suit.value, c))
	#print("find best flush", cards)
	flushes = []
	candidate = []
	for i, c in enumerate(cards, start=0):
		#print("looking at:", c)
		if len(cards) <= i + 1:
			if len(candidate) >= 5:
				flushes.append(candidate[:5])
			break
		next_card = cards[i + 1]
		if c.suit == next_card.suit:
			if len(candidate) == 0:
				candidate.append(c)
				candidate.append(next_card)
			else:
				candidate.append(next_card)
		else:
			if len(candidate) >= 5:
				flushes.append(candidate[:5])
				break
			else:
				candidate = []
	
	if len(flushes) > 0:
		return flushes[0]
	else: 
		return []

def find_straight_flush(straights):
	for s in straights:
		if( check_flush(s) ):
			return s
	return []
	
def get_hand_score(player, community_cards, is_tutorial):
	combined_cards = combine_cards(player, community_cards)
	straights = find_straights(combined_cards)
	straight_flush = find_straight_flush(straights)
	if len(straight_flush) > 0:
		if(is_tutorial):
			print("Player", player.id, "with a straight flush")
			print(straight_flush)
		return STRAIGHT_FLUSH + score_cards(straight_flush)
	score_reps, rep_hand = find_reps_or_high_card(combined_cards)
	if score_reps >= FOUR_OF_A_KIND:
		if(is_tutorial):
			print("Player", player.id, "with four of a kind")
			print(rep_hand)
		return score_reps
	if score_reps >= FULL_HOUSE:
		if(is_tutorial):
			print("Player", player.id, "with a full house")
			print(rep_hand)
		return score_reps
	flush = find_best_flush(combined_cards)
	if len(flush) > 0:
		if(is_tutorial):
			print("Player", player.id, "with a flush")
			print(flush)
		return FLUSH + score_cards(flush)
	if len(straights) > 0:
		if(is_tutorial):
			print("Player", player.id, "with a straight")
			straights[0].sort(reverse=True)
			print(straights[0])
		return STRAIGHT + score_cards(straights[0])
	if score_reps >= THREE_OF_A_KIND:
		if(is_tutorial):
			print("Player", player.id, "with three of a kind")
			print(rep_hand)
		return score_reps
	if score_reps >= TWO_PAIR:
		if(is_tutorial):
			print("Player", player.id, "with two pairs")
			print(rep_hand)
		return score_reps
	if score_reps >= PAIR:
		if(is_tutorial):
			print("Player", player.id, "with a pair")
			print(rep_hand)
		return score_reps
	else: #high card
		if(is_tutorial):
			print("Player", player.id, "with high card")
			print(rep_hand)
		return score_reps

def find_winners(players, community_cards, is_tutorial):
	cc = community_cards
	is_t = is_tutorial
	scored_players =  \
		[[i, get_hand_score(p, cc, is_t)]for i, p in enumerate(players,start=1)]
	scored_players.sort(reverse=True, key=lambda c: c[1])
	highest_score = scored_players[0][1]
	i = 0
	winners = []
	for player, score in scored_players:
		if score < highest_score:
			break
		winners.append(player)
	return winners
