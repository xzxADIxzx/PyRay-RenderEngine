class Sobject():
	def __init__(self, name, position, rotation, scale, material):
		self.name = name
		self.position = position
		self.rotation = rotation
		self.scale = scale
		self.material = material

	def intersects(self, ray):
		return None

class Camera(Sobject):
	def __init__(self, name, position, rotation, width, height, fov, reflections, fog):
		super().__init__(name, position, rotation, None, None)
		self.width = width
		self.height = height
		self.fov = fov
		self.reflections = reflections
		self.fog = fog
		

class Sphere(Sobject):
	def __init__(self, name, position, material, radius):
		super().__init__(name, position, None, None, material)
		self.radius = radius

	def intersects(self, ray):
		cp = self.position - ray.origin
		v = cp.dot(ray.direction.normalized)
		discriminant = self.radius ** 2 - cp.dot(cp) + v * v

		if discriminant < 0:
			return None
		else:
			# return ray.position(v - sqrt(discriminant))
			import math
			return (self, v - math.sqrt(discriminant))