from classes.vector import *
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

	def get_normal(self, pos):
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
			dis = v - math.sqrt(discriminant)
			if dis < 0:
				return None
			return (self, dis)

	def get_normal(self, pos):
		return (pos - self.position).normalized

class Cube(Sobject):
	def __init__(self, name, position, scale, material):
		super().__init__(name, position, None, scale, material)
		self.name = name
		self.position = position
		self.scale = scale
		self.material = material
		self.min = position - scale/2
		self.max = position + scale/2

	def intersects(self, ray):
		add_total_intr()

		try: x = 1/ray.direction.x
		except: x = 1/0.0001

		try: y = 1/ray.direction.y
		except: y = 1/0.0001

		try: z = 1/ray.direction.z
		except: z = 1/0.0001

		tx1 = (self.min.x - ray.origin.x) * x;
		tx2 = (self.max.x - ray.origin.x) * x;

		tmin = min(tx1, tx2);
		tmax = max(tx1, tx2);

		ty1 = (self.min.y - ray.origin.y) * y;
		ty2 = (self.max.y - ray.origin.y) * y;

		tmin = max(tmin, min(ty1, ty2));
		tmax = min(tmax, max(ty1, ty2));

		tz1 = (self.min.z - ray.origin.z) * z;
		tz2 = (self.max.z - ray.origin.z) * z;

		tmin = max(tmin, min(tz1, tz2));
		tmax = min(tmax, max(tz1, tz2));

		if tmax >= tmin and tmax >= 0:
			return (self, tmin)
		else:
			return None

	def get_normal(self, pos):
		nrm = (pos - self.position)
		nmx = max(abs(nrm.x), max(abs(nrm.y), abs(nrm.z)))
		if nmx == abs(nrm.x):
			return Vector(nrm.x, 0, 0).normalized
		if nmx == abs(nrm.y):
			return Vector(0, nrm.y, 0).normalized
		if nmx == abs(nrm.z):
			return Vector(0, 0, nrm.z).normalized