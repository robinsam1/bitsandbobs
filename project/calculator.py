class calculator(object):
	def __init__(self):
		self.x = 'Calculator'

	def calculate(self, answers):
		score = 10.0
		if "commute" in answers and "transport" in answers:
			distance = float(answers["commute"])
			commuteimpact = 0.0
			if answers["transport"] == "auto":
				commuteimpact = 0.250
			elif answers["transport"] == "bus":
				commuteimpact = 0.100
			elif answers["transport"] == "subway":
				commuteimpact = 0.05
			score += (distance * commuteimpact)
		if "diet" in answers:
			foodimpact = 0.0
			if answers["diet"] == "meat":
				foodimpact = 4.0
			elif answers["diet"] == "white":
				foodimpact = 1.5
			elif answers["diet"] == "vegetarian":
				foodimpact = 1.0
			score += foodimpact
		if "flights" in answers and "flightfrequency" in answers:
			flightdistance = 0.0
			flightfrequency = float(answers["flightfrequency"])
			flightimpact = 0.08
			returntrip = 2.0
			if answers["flights"] == "shorthaul":
				flightdistance = 1000 * returntrip * flightfrequency
			elif answers["flights"] == "mediumhaul":
				flightdistance = 3000 * returntrip * flightfrequency
			elif answers["flights"] == "longhaul":
				flightdistance = 5000 * returntrip * flightfrequency
			score += (flightdistance * flightimpact)/365
		return score
