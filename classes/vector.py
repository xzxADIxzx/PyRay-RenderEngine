import math

class Vector():
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return str((self.x, self.y, self.z))

	def __add__(self, other):
		if isinstance(other, Vector):
			return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
		else:
			return Vector(self.x + other, self.y + other, self.z + other)

	def __sub__(self, other):
		if isinstance(other, Vector):
			return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
		else:
			return Vector(self.x - other, self.y - other, self.z - other)

	def __mul__(self, other):
		if isinstance(other, Vector):
			return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
		else:
			return Vector(self.x * other, self.y * other, self.z * other)

	def __truediv__(self, other):
		if isinstance(other, Vector):
			return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
		else:
			return Vector(self.x / other, self.y / other, self.z / other)
	
	def __abs__(self):
		return Vector(abs(self.x), abs(self.y), abs(self.z))

	@property
	def zero(self):
		return Vector(0, 0, 0)

	@property
	def magnitude(self):
		return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

	@property
	def normalized(self):
		mag = self.magnitude
		return Vector(self.x / mag, self.y / mag, self.z / mag)

	def dot(self, other):
		return self.x * other.x + self.y * other.y + self.z * other.z