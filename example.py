from PyRay import *
from PIL import Image
import time

print("PyRay - RenderEngine")
print("By xzxADIxzx")
print("V1.0 Release")
print()

col = Color(255, 0, 0)
mat = Material(col, .8, 1)
spr = Sphere("Sphere", Vector(-5, 5, 80), mat, 70)

col = Color(0, 150, 255)
mat = Material(col, .8, 1)
bsr = Sphere("Sphere", Vector(20, -15, 90), mat, 60)

col = Color(100, 255, 100)
mat = Material(col, .8, 1)
bgs = Sphere("Sphere", Vector(0, 0, 100), mat, 80)

col = Color(255, 0, 255)
mat = Material(col, 1, 1)
psp = Sphere("Sphere", Vector(0, 0, 200), mat, 100)

col = Color(0, 200, 255)
mat = Material(col, 1, 1)
lbs = Sphere("Sphere", Vector(-130, -50, 40), mat, 20)

col = Color(255, 50, 50)
mat = Material(col, .8, 1)
ars = Sphere("Sphere", Vector(-100, 50, 40), mat, 30)

col = Color(50, 50, 255)
mat = Material(col, 1, .6)
als = Sphere("Sphere", Vector(120, 40, 40), mat, 35)

col = Color(50, 240, 50)
mat = Material(col, 1, 1)
ags = Sphere("Sphere", Vector(110, -60, 20), mat, 15)

col = Color(150, 150, 150)
mat = Material(col, 1, 1)
cub = Cube("Cube", Vector(140, -15, 80), Vector(50, 50, 50), mat)


# col = Color(255, 50, 50)
# mat = Material(col, 1, .4)
# rsp = Sphere("Sphere", Vector(-90, 0, 90), mat, 80)

# col = Color(0, 150, 255)
# mat = Material(col, 1, .4)
# bsp = Sphere("Sphere", Vector(90, 0, 90), mat, 80)


# col = Color(255, 50, 50)
# mat = Material(col, 1, .4)
# rcb = Cube("Cube", Vector(0, 0, -70), Vector(120, 120, 120), mat)

# col = Color(0, 150, 255)
# mat = Material(col, 1, .4)
# bcb = Cube("Cube", Vector(0, 0, 70), Vector(150, 150, 150), mat)

cam = Camera("Main Camera", Vector().zero, Vector().zero, 355, 200, 60, 5)
scn = Scene(cam, Vector(0, 1, 0).normalized, [spr, bsr, bgs, psp, lbs, ars, als, ags, cub])

# scn = Scene(cam, Vector(0, 1, 0).normalized, [bgs])
# scn = Scene(cam, Vector(0, 1, 0).normalized, [rsp, bsp])
# scn = Scene(cam, Vector(0, 1, 0).normalized, [rcb, bcb])

rtx = time.time()
rim = render(scn).content

print("Render: " + str(round(time.time() - rtx, 2)) + " secs")
print("Traced: " + str(get_total_rays()) + " rays")
print("Checkd: " + str(get_total_intr()) + " intr")

img = Image.new('RGB', (cam.width, cam.height))
for x in range(cam.width):
	for y in range(cam.height):
		img.putpixel((x, y), (rim[x][y].r, rim[x][y].g, rim[x][y].b))
img.save('render.png')
img.show()
# input() for console