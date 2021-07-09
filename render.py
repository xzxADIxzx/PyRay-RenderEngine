from PyRay import *
import math

def canvas(camera):
	pxl = []
	# step = camera.fov / camera.width
	# for x in range(camera.width):
	# 	for y in range(camera.height):
	# 		pxl += [Vector(math.cos(x * step - camera.fov / 2), math.sin(y * step - camera.fov / 2), 1)]
	for x in range(camera.width * camera.height):
		pxl +=	[Vector(0, 0, 1)]
	return pxl

def trace(ray, objects, light, recursion, max_recursion, dis = None):
	if dis is None: # Trace all objects
		dis = []
		for obj in objects:
			hit = obj.intersects(ray)
			if hit is not None:
				dis += [hit]

	if len(dis) == 0:
		return Color(0, 0, 0)

	dis.sort(key = lambda x: x[1])
	hit = dis[0] # The closest object the ray collided with
	clr = hit[0].material.color * hit[0].material.transparency
	pos = Vector(ray.origin.x, ray.origin.y, 1 * hit[1])

	# Normal
	nrm = pos - hit[0].position
	nrm = light.dot(nrm.normalized) * -120 # Temp "-120" Because Bug#0001
	clr += Color(nrm, nrm, nrm)

	# Transparency
	if hit[0].material.transparency < 1 and not recursion == max_recursion:
		trndis = dis
		trndis.remove(dis[0])
		clr += trace(ray, objects, light, recursion + 1, max_recursion, dis) * (1 - hit[0].material.transparency)

	# Shadows
	# # pos = Vector(x - scene.camera.width/2, y - scene.camera.height/2, 1 * hit[1])
	# # pos = Vector(x - scene.camera.width/2, y - scene.camera.height/2, 0) + can[x * y] * hit[1]
	# ray = Ray(pos, Vector(0, 1, 0))
	# shd = hit[0].intersects(ray)
	# if hit is not None:
	# 	clr = Color(100, 100, 100)

	return clr

def render(scene):
	img = [[None for x in range(scene.camera.height)] for y in range(scene.camera.width)]
	can = canvas(scene.camera)
	for x in range(scene.camera.width):
		for y in range(scene.camera.height):
			# ray = Ray(scene.camera.position, can[x * y])
			ray = Ray(Vector(x - scene.camera.width/2, y - scene.camera.height/2, 0), can[x * y])
			img[x][y] = trace(ray, scene.objects, scene.light, 0, scene.camera.recursion)

	return Frame(scene.camera.width, scene.camera.height, img)