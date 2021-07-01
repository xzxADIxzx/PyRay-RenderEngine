from PyRay import *
from PIL import Image
import time

cam = Camera("Main Camera", Vector().zero, Vector().zero, 355, 200, 60, 2, 20)
col = Color(255, 0, 0)
mat = Material(col, .2, 1)
spr = Sphere("Sphere", Vector(-5, 5, 100), mat, 70)
col = Color(0, 150, 255)
mat = Material(col, .2, 1)
bsr = Sphere("Sphere", Vector(20, -15, 100), mat, 60)
col = Color(100, 255, 100)
mat = Material(col, .2, 1)
bgs = Sphere("Sphere", Vector(0, 0, 100), mat, 80)
scn = Scene(cam, Vector(0, 100, 0), [spr, bsr, bgs])
rtx = time.time()
rim = render(scn).content
print("Render: " + str(time.time() - rtx))

img = Image.new('RGB', (cam.width, cam.height))
for x in range(cam.width):
	for y in range(cam.height):
		img.putpixel((x, y), (rim[x][y].r, rim[x][y].g, rim[x][y].b))
img.save('render.png')
img.show()

# Bug#0001: Камера отзеркалена по вертикале.
# Лучи должный пускаться слева -> направо
# И сверху -> вниз, а не наоборот

# Bug#0002: Отображает обЪекты в том порядке
# К котором они находятся в спике.
# Надо отсортировать список по растоянию от камеры

# P.S. Возможно это не поможет, тогда надо будет
# Записывать растояния которое прошел луч
# И отрисовывать тот который прошёл наименьшее растояние