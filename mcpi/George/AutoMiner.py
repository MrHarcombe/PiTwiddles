import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import datetime
import math
mc = minecraft.Minecraft.create()
playerpos = mc.player.getPos()

alive = 1

while alive == 1:
	playerpos = mc.player.getPos()
	if (playerpos.y > -59):
		mc.setBlock(playerpos.x + 1, playerpos.y, playerpos.z + 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y, playerpos.z, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y, playerpos.z - 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 1, playerpos.z + 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 1, playerpos.z, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 1, playerpos.z - 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y - 1, playerpos.z + 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y - 1, playerpos.z, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y - 1, playerpos.z - 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 2, playerpos.z + 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 2, playerpos.z, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 2, playerpos.z - 1, 0)
	else:
		mc.setBlock(playerpos.x + 1, playerpos.y, playerpos.z + 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y, playerpos.z, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y, playerpos.z - 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 1, playerpos.z + 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 1, playerpos.z, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 1, playerpos.z - 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 2, playerpos.z + 1, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 2, playerpos.z, 0)
		mc.setBlock(playerpos.x + 1, playerpos.y + 2, playerpos.z - 1, 0)
		