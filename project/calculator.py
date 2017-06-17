class calculator(object):
	def __init__(self):
		self.x = 'Calculator'

	def calculate(self, answers):
		score = 10.0
		#for answer in answers:
		#	score+=answer
		score+=(float(answers["driving"]) * .250)
		return score
