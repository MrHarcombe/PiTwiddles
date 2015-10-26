import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import datetime
import math
mc = minecraft.Minecraft.create()

#coordinates from lowest x, y, z

#(length along x axis, heighest point of wall, length along z axis, x coordinate, y coordinate, z coordinate)

BlockType = 1

def Clear(x, y, z, x1, y1, z1):
	for a in range(x):
		for b in range(y):
			for c in range(z):
				mc.setBlock(a + x1, b + y1, c + z1, 0)
				if (b == 0):
					mc.setBlock(a + x1, b + y1, c + z1, BlockType)

def WallN(x, y, z, x1, y1, z1):
	y1 = int(y1 / 2)
	for z2 in range(z1 - 10):
		mc.setBlock(x + 2, y + y1 - 3, z + z2 + 5, BlockType)
		for y2 in range(y1):
			for x2 in range(2):
				if ((y2 != y1 - 1) or (z2 % 2 == 1)):
					mc.setBlock(x + 1 + (x2 * 2), y2 + y, z + z2 + 5, BlockType)
	

def WallS(x, y, z, x1, y1, z1):
	y1 = int(y1 / 2)
	for z2 in range(z1 - 10):
		mc.setBlock(x + (x1 - 3), y + y1 - 3, z + z2 + 5, BlockType)
		for y2 in range(y1):
			for x2 in range(2):
				if ((y2 != y1 - 1) or (z2 % 2 == 1)):
					mc.setBlock(x + (x1 - 4) + (x2 * 2), y2 + y, z + z2 + 5, BlockType)

def WallE(x, y, z, x1, y1, z1):
	y1 = int(y1 / 2)
	for z2 in range(x1 - 10):
		mc.setBlock(x + z2 + 5, y + y1 - 3, z + 2, BlockType)
		for y2 in range(y1):
			for x2 in range(2):
				if ((y2 != y1 - 1) or (z2 % 2 == 1)):   
					mc.setBlock(x + z2 + 5, y2 + y, z + 1 + (x2 * 2), BlockType)

def WallW(x, y, z, x1, y1, z1):
	y1 = int(y1 / 2)
	for z2 in range(x1 - 10):
		mc.setBlock(x + z2 + 5, y + y1 - 3, z + (z1 - 3), BlockType)
		for y2 in range(y1):
			for x2 in range(2):
				if ((y2 != y1 - 1) or (z2 % 2 == 1)):   
					mc.setBlock(x + z2 + 5, y2 + y, z + (z1 - 4) + (x2 * 2), BlockType)

def Towers(x, y, z, l, h, w):
	Tower(x, y, z, int((h * 3) / 4))
	Tower(x + (l - 5), y, z, int((h * 3) / 4))
	Tower(x, y, z + (w - 5), int((h * 3) / 4))
	Tower(x + (l - 5), y, z + (w - 5), int((h * 3) / 4))

def Tower(x1, y1, z1, h1):
	for x2 in range(5):
		for y2 in range(int(h1)):
			for z2 in range(5):
				if (x2 == 4) or (x2 == 0) or (z2 == 4) or (z2 == 0):
					if (int(h1) - 1 != y2) or ((x2 % 2 == 0) and (z2 % 2 == 0)):
						mc.setBlock(x1 + x2, y1 + y2, z1 + z2, BlockType)
	#				else:
						#mc.setBlock(x1 + x2, y1 + y2, z1 + z2, STONE_BRICK_HALF_SLAB)

def CastleSize(XLen, Height, ZLen, XCoord, YCoord, ZCoord, Block):
	BlockType = Block
	print BlockType
	YCoord = YCoord - 1
	Clear(XLen, Height, ZLen, XCoord, YCoord, ZCoord)
	YCoord = YCoord + 1
	WallN(XCoord, YCoord, ZCoord, XLen, Height, ZLen)
	WallS(XCoord, YCoord, ZCoord, XLen, Height, ZLen)
	WallE(XCoord, YCoord, ZCoord, XLen, Height, ZLen)
	WallW(XCoord, YCoord, ZCoord, XLen, Height, ZLen)
	Towers(XCoord, YCoord, ZCoord, XLen, Height, ZLen)
	#If (XLen > 9) and (ZLen > 9):
		#Keep(XLen, Height, ZLen)


CastleSize(31, 15, 31, -30, 6, 20, 0)
#mc.player.setPos(11, -10, 11)