import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import datetime
import math
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

mc.player.setPos(pos.x, pos.y + 100, pos.z)
print pos.y + 100
x = 1
while mc.getBlock(pos.x, pos.y - 2, pos.z) != 0:
	pos = mc.player.getPos()
	x = 1
	
while mc.getBlock(pos.x, pos.y - 2, pos.z) == 0:
	pos = mc.player.getPos()
	time.sleep(0.0001)
	x = x + 1
	

print x