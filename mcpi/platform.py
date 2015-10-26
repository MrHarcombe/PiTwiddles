#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  platform.py
#  
#  Copyright 2013  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import block
import time
from vec3 import Vec3
from block import Block
from minecraft import Minecraft

def drawBlock(m, position, draw):
	if draw and (Block(m.getBlock(position.x, position.y, position.z)) == block.AIR):
		m.setBlock(position.x, position.y, position.z, block.GLASS)
	elif not draw and (Block(m.getBlock(position.x, position.y, position.z)) == block.GLASS):
		m.setBlock(position.x, position.y, position.z, block.AIR)	

# draw at y = const, i.e. (round(x+-0.5), round(y-1), round(z+-0.5))
def drawPlatform(m, where, was):
	toDraw = (Vec3(round(where.x-0.5), round(where.y-1), round(where.z+0.5)),
		Vec3(round(where.x+0.5), round(where.y-1), round(where.z+0.5)),
		Vec3(round(where.x-0.5), round(where.y-1), round(where.z-0.5)),
		Vec3(round(where.x+0.5), round(where.y-1), round(where.z-0.5)))
		
	toErase = (Vec3(round(was.x-0.5), round(was.y-1), round(was.z+0.5)),
		Vec3(round(was.x+0.5), round(was.y-1), round(was.z+0.5)),
		Vec3(round(was.x-0.5), round(was.y-1), round(was.z-0.5)),
		Vec3(round(was.x+0.5), round(was.y-1), round(was.z-0.5)))

	for pos in toDraw:
		drawBlock(m, pos, True)
	for pos in toErase:
		if pos not in toDraw:
			drawBlock(m, pos, False)

def trackPlayer(m):
	where  = Vec3()
	was = Vec3()

	while True:
		# where = m.player.getPos() # returns decimals, e.g. (1.1, 2.2, 3.3)
		where = m.player.getTilePos()
		where.y -= 1

		if (where != was):
			drawBlock(m, where, True)
			drawBlock(m, was, False)
			# drawPlatform(m, where, was)
			was = where

def main():
	m = Minecraft.create()
	m.postToChat("You'll never walk alone!")
	trackPlayer(m)
	return 0

if __name__ == '__main__':
	main()

