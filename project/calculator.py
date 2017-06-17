class calculator(object):
	def __init__(self):
		self.x = 'Calculator'

	def calculate(self, answers):
		score = 10.0
		if "driving" in answers:
			score+=(float(answers["driving"]) * .250)
		if "diet" in answers:
			if answers["diet"] == "meat":
				score+=4.0
			elif answers["diet"] == "white":
				score+= 1.5
			elif answers["diet"] == "vegetarian":
				score+= 1.0
		return score
