from card_h import *

class Player:
	def __init__(self, id):
		self.id = id
		self.hand = []
		self.chips = 0
		self.blind = Blind.no_blind

	def __repr__(self):
		ret_str = "hand: " + \
		 str(self.hand)    + \
		 "; chips: "       + \
		 str(self.chips)   + \
		 "; blind: "       + \
		 str(self.blind.name)
		return ret_str

	def fold(self):
		self.hand.clear()

	def get_hand(self):
		return [self.hand[0], self.hand[1]]

	def hand_stringify(self):
		if len(self.hand) != 2:
			return "ERROR"

		first_card = self.hand[0]
		second_card = self.hand[1]
		
		if first_card.value == '10':
			first_card_str = "| " + str(first_card) + " |"
		else:
			first_card_str = "| " + str(first_card) + "  |"

		if second_card.value == '10':
			second_card_str = "| " + str(second_card) + " |"
		else:
			second_card_str = "| " + str(second_card) + "  |"

		return  "Player "          \
				+ str(self.id)     \
                + "\n"             \
				+ first_card_str   \
			    + " "              \
			    + second_card_str 
