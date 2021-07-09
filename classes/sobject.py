import math

total = 0

def get_total_intr():
	return total

def add_total_intr():
	# Counts the number of intersections
	global total
	total += 1

class Sobject():
	def __init__(self, name, position, rotation, scale, material):
		self.name = name
		self.position = position
		self.rotation = rotation
		self.scale = scale
		self.material = material

	def intersects(self, ray):
		add_total_intr()
		return None

class Camera(Sobject):
	def __init__(self, name, position, rotation, width, height, fov, recursion):
		super().__init__(name, position, rotation, None, None)
		self.width = width
		self.height = height
		self.fov = fov
		self.recursion = recursion

class Sphere(Sobject):
	def __init__(self, name, position, material, radius):
		super().__init__(name, position, None, None, material)
		self.radius = radius

	def intersects(self, ray):
		add_total_intr()
		cp = self.position - ray.origin
		v = cp.dot(ray.direction.normalized)
		discriminant = self.radius ** 2 - cp.dot(cp) + v ** 2

		if discriminant < 0:
			return None
		else:
			# return ray.position(v - sqrt(discriminant))
			return (self, v - math.sqrt(discriminant))

		# b = ray.origin.dot(ray.direction);
		# c = ray.origin.dot(ray.origin) - self.radius ** 2;
		# h = b * b - c;

		# if h < 0:
		# 	return None
		# else:
		# 	import math
		# 	h = math.sqrt(h);
		# 	# return Vector(-b - h, -b + h, 0)
		# 	return (self, -b - h)