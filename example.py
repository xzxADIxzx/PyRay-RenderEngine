from PyRay import *
from PIL import Image
import time

rimg = [[] for x in range(100)]
spr = Sphere("Object", Vector(50, 50, 10), Vector(0, 0, 0), Vector(0, 0, 0), 35)
rt = time.time()
for x in range(100):
	for y in range(100):
		rimg[x] += [spr.intersects(Ray(Vector(x, y, 0), Vector(0, 0, 1)))]
print("Render: " + str(time.time() - rt))

img = Image.new('RGB', (100, 100))
for x in range(100):
	for y in range(100):
		if rimg[x][y]:
			img.putpixel((x, y), (255, 255, 255))
img.save('render.png')
img.show()