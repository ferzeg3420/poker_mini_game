import card_h
import community_cards_h
import player_h

def get_high_card_from_players(players, community_cards):
	""" This function is erroneous don't use """

	high_card = players[0].get_hand()[0]
	winning_players = []

	for p in players:
		hand = p.get_hand()
		if high_card < hand[0]:
			high_card = hand[0]
		if high_card < hand[1]:
			high_card = hand[1]

	for p in players:
		hand = p.get_hand()
		if high_card == hand[0] or high_card == hand[1]:
			winning_players.append(p.id)
	return [high_card, winning_players]
