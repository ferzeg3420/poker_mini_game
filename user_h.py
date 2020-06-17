
class User:
	def __init__(self, score, lives):
		self.score = score
		self.lives = lives
		self.name = "User"

	def __repr__(self):
		score = self.score
		lives = self.lives
		name = self.name
		user_string = name                   \
					 + "\t\tScore: "         \
					 + str(score)            \
                     + " lives: "            \
                     + str(lives)            \
                     + "\n"    
		return user_string
