import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import datetime
import math
mc = minecraft.Minecraft.create()

for x in range(5):
	for y in range(30):
		for z in range(5):
			if (x == 0) or (x == 4) or (z == 0) or (z == 4):
				mc.setBlock(x, y, z, 1)