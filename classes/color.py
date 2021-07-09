class Color():
	def __init__(self, r, g, b):
		self.r = int(r)
		self.g = int(g)
		self.b = int(b)

	def __str__(self):
		return str((self.r, self.g, self.b))

	def __add__(self, other):
		if isinstance(other, Color):
			return Color(self.r + other.r, self.g + other.g, self.b + other.b)
		else:
			return Color(self.r + other, self.g + other, self.b + other)

	def __mul__(self, other):
		if isinstance(other, Color):
			return Color(self.r * other.r, self.g * other.g, self.b * other.b)
		else:
			return Color(self.r * other, self.g * other, self.b * other)