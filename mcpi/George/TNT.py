import minecraft
import block
import time
import datetime
import math

mc = minecraft.Minecraft.create()

x = 0
y = 0
z = 0
x2 = 0
y2 = 0
z2 = 0
portalx = 0
portaly = 0
portalz = 0

while True :
	hits = mc.events.pollBlockHits()
	for hit in hits:
		for x in range(5):
			for y in range(5):
				if ((x == 0) or (x == 4)) or ((y == 0) or (y == 4)):
					if (x2 != 0):
						mc.setBlock(portalx2, portaly2 + x - 2, portalz2 + y - 2, 0)
					if (y2 != 0):
						mc.setBlock(portalx2 + x - 2, portaly2, portalz2 + y - 2, 0)
					if (z2 != 0):
						mc.setBlock(portalx2 + y - 2, portaly2 + x - 2, portalz2, 0)
		x = 0
		y = 0
		z = 0
		info = str(hits[0]).split()
		direction = info[4][0]
		if (direction == "4"):
			x = -1
		if (direction == "2"):
			z = -1
		if (direction == "3"):
			z = 1
		if (direction == "1"):
			y = 1
		if (direction == "5"):
			x = 1
			mc.postToChat(x)
		if (direction == "0"):
			y = -1
		x2 = x
		y2 = y
		z2 = z
		portalx2 = portalx
		portaly2 = portaly
		portalz2 = portalz
		portalx = hit.pos.x + x
		portaly = hit.pos.y + y
		portalz = hit.pos.z + z
		mc.postToChat(x)
		for x in range(5):
			for y in range(5):
				if ((x == 0) or (x == 4)) or ((y == 0) or (y == 4)):
					if (x2 != 0):
						mc.postToChat("working")
						mc.setBlock(portalx, portaly + x - 2, portalz + y - 2, 1)
					if (y2 != 0):
						mc.postToChat("working")
						mc.setBlock(portalx + x - 2, portaly, portalz + y - 2, 1)
					if (z2 != 0):
						mc.postToChat("working")
						mc.setBlock(portalx + y - 2, portaly + x - 2, portalz, 1)
	pos = mc.player.getPos()
	inport = 0
	if (x != 0):
		if (int(pos.x) == portalx) and (pos.y > portaly - 2) and (pos.y < portaly + 2) and (pos.z > portalz - 2) and (pos.z < portalz + 2):
			inport = 1
	if (y != 0):
		if ((int(pos.y) == portaly) or (int(pos.y) + 1 == portaly)) and (pos.x > portalx - 2) and (pos.x < portalx + 2) and (pos.z > portalz - 2) and (pos.z < portalz + 2):
			inport = 1
	if (z != 0):
		if (int(pos.z) - 1 == portalz) and (pos.x > portalx - 2) and (pos.x < portalx + 2) and (pos.y > portaly - 2) and (pos.y < portaly + 2):
			inport = 1
	if (x2 != 0):
		if (int(pos.x) == portalx2) and (pos.y > portaly2 - 2) and (pos.y < portaly2 + 2) and (pos.z > portalz2 - 2) and (pos.z < portalz2 + 2):
			inport = 2
	if (y2 != 0):
		if ((int(pos.y) == portaly2) or (int(pos.y) + 1 == portaly2) or (int(pos.y) - 1 == portaly2) or (int(pos.y) - 2 == portaly2)) and (pos.x > portalx2 - 2) and (pos.x < portalx2 + 2) and (pos.z > portalz2 - 2) and (pos.z < portalz2 + 2):
			inport = 2
	if (z2 != 0):
		if (int(pos.z) - 1 == portalz2) and (pos.x > portalx2 - 2) and (pos.x < portalx2 + 2) and (pos.y > portaly2 - 2) and (pos.y < portaly2 + 2):
			inport = 2
	if (inport == 1):
		mc.player.setPos(portalx2 + x2, portaly2 + y2, portalz2 + z2)
		time.sleep(0.1)
	if (inport == 2):
		mc.player.setPos(portalx + x, portaly+ y, portalz + z)
		time.sleep(0.1)
