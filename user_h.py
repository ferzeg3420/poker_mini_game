import util

class User:
	def __init__(self, score, lives):
		self.score = score
		self.lives = lives
		self.name = "User"

	def __repr__(self):
		score = self.score
		hearts = util.lives_2_hearts(self.lives)
		lives = self.lives
		name = self.name
		user_string = name + "\t" + hearts + "\t\tScore: " + str(score) + "\n\n"
		return user_string
