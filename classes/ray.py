total = 0

def get_total_rays():
	return total

class Ray():
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction

		# Counts the number of rays
		global total
		total += 1