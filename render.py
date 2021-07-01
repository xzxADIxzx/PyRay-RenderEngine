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

def render(scene):
	img = [[None for x in range(scene.camera.width)] for x in range(scene.camera.width)]
	can = canvas(scene.camera)
	for x in range(scene.camera.width):
		for y in range(scene.camera.height):
			for obj in scene.objects:
				# ray = Ray(scene.camera.position, can[x * y])
				ray = Ray(Vector(x - scene.camera.width/2, y - scene.camera.height/2, 0), can[x * y])
				hit = obj.intersects(ray)
				if hit is None:
					img[x][y] = Color(0, 0, 0)
				else:
					img[x][y] = hit[0].material.color * hit[0].material.transparency
					# Move to while or def
					if hit[0].material.transparency < 1:
						trnobjects = list(scene.objects)
						trnobjects.remove(obj)
						for trnobj in trnobjects:
							trnhit = trnobj.intersects(ray)
							if trnhit is not None:
								img[x][y] += trnhit[0].material.color * (1 - hit[0].material.transparency)
					break
	return Frame(scene.camera.width, scene.camera.height, img)