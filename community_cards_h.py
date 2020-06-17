import ascii

class Community_cards:
	def __init__(self):
		self.cards = []

	def append(self, cards):
		if type(cards) == type(list()):
			for c in cards:
				self.cards.append(c)
		else:
			self.cards.append(cards)

	def reset(self):
		self.cards.clear()

	def stringify(self):
		return str(self.cards)

	def get_flop(self):
		custom_string = ""
		custom_string = ascii.flop_string(self.cards)
		return custom_string + "\n" + "Flop"

	def get_flop_turn(self):
		custom_string = ""
		custom_string = ascii.flop_turn_string(self.cards)
		return custom_string + "\n" + "Turn"

	def get_flop_turn_river(self):
		custom_string = ""
		custom_string = ascii.flop_turn_river_string(self.cards)
		return custom_string + "\n" + "River"
