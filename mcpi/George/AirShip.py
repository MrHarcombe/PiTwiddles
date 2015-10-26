import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import datetime
import math
mc = minecraft.Minecraft.create()

x = 64
y = 32
z = 64
xmv = 1
zmv = 0
try:
	while True :
		MOVE = 0
		pos = mc.player.getPos()
		if (pos.x > x - 6) and (pos.z < z + 6) and (pos.z > z - 6) and (pos.z < z + 6) and (pos.y - 1 == y):
			MOVE = 1
		xb = x - 5
		while xb < x + 6:
			zb = z - 5
			while zb < x + 6:
				mc.setBlock(xb, y, zb, 0)
				zb = zb + 1
			xb = xb + 1
		x = x + xmv
		z = z + zmv
		xb = x - 5
		while xb < x + 6:
			zb = z - 5
			while zb < x + 6:
				mc.setBlock(xb, y, zb, 1)
				zb = zb + 1
			xb = xb + 1
		if (MOVE == 1):
			mc.player.setPos(pos.x + xmv, pos.y, pos.x + zmv)
		time.sleep(1)

except KeyboardInterrupt:
	xb = x - 5
	while xb < x + 6:
		zb = z - 5
		while zb < z + 6:
			mc.setBlock(xb, y, zb, 0)
			zb = zb + 1
		xb = xb + 1
	x = x + xmv
	z = z + zmv
	xb = x - 5
	while xb < x + 6:
		zb = z - 5
		while zb < z + 6:
			mc.setBlock(xb, y, zb, 0)
			zb = zb + 1
		xb = xb + 1