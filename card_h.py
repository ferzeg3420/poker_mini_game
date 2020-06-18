from enum import Enum
import sys

is_windows = hasattr(sys, 'getwindowsversion')

class Blind(Enum):
	dealer = 1
	big_blind = 2
	small_blind = 3
	no_blind = 4

class Suit(Enum):
	spades = 1
	hearts = 2
	diamonds = 3
	clubs = 4

values = [ 'A' , \
		   '2' , \
           '3' , \
           '4' , \
           '5' , \
           '6' , \
           '7' , \
           '8' , \
           '9' , \
           '10', \
           'J' , \
           'Q' , \
           'K' ]

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return self.display_card()

	def display_card(self):
		if self.suit == Suit.spades:
			suit = "♠"
		elif self.suit == Suit.hearts:
			if is_windows:
				suit = "♥"
			else: #unix
				suit = "♡"
		elif self.suit == Suit.diamonds:
			if is_windows:
				suit = "♦"
			else: #unix
				suit = "♢"
		elif self.suit == Suit.clubs:
			suit = "♣"
		else:
			print ("ERROR")	
		return self.value + suit

	def get_value_as_int(self):
		value = 0
		if self.value == 'A':
			value = 14
		elif self.value == 'J':
			value = 11
		elif self.value == 'Q':	
			value = 12
		elif self.value == 'K':	
			value = 13
		else:
			value = int(self.value)
		return value

	def __lt__(self, other):
		return self.get_value_as_int() < other.get_value_as_int()	

	def __eq__(self, other):
		return self.get_value_as_int() == other.get_value_as_int()	
