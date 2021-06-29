class Sobject():
	def __init__(self, name, position, rotation, scale):
		self.name = name
		self.position = position
		self.rotation = rotation
		self.scale = scale

	def intersects(self, ray):
		return False

class Sphere(Sobject):
	def __init__(self, name, position, rotation, scale, radius):
		super().__init__(name, position, rotation, scale)
		self.radius = radius

	def intersects(self, ray):
		cp = self.position - ray.origin
		v = cp.dot(ray.direction.normalized)
		discriminant = self.radius ** 2 - cp.dot(cp) + v * v

		if discriminant < 0:
			return False
		else:
			# return ray.position(v - sqrt(discriminant))
			return True