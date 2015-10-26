import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import datetime
import math
mc = minecraft.Minecraft.create()

x = 25
y = 0
z = -9
while True:
	for x1 in range(29):
		for y1 in range(30):
			for z1 in range(25):
				mc.setBlock(x + x1, y + y1, z + z1, 0)