class calculator(object):
	def __init__(self):
		self.x = 'Calculator'

	def calculate(self, answers):
		score = 10.0
		if "commute" in answers and "transport" in answers:
			distance=float(answers["commute"])
			if answers["transport"] == "auto":
				score+=(distance *.250)
			elif answers["transport"] == "bus":
				score+=(distance *.1)
			elif answers["transport"] == "subway":
				score+=(distance *.05)
		if "diet" in answers:
			if answers["diet"] == "meat":
				score+=4.0
			elif answers["diet"] == "white":
				score+= 1.5
			elif answers["diet"] == "vegetarian":
				score+= 1.0
		return score
