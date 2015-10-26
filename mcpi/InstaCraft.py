import minecraft
import block

def main():
    m=minecraft.Minecraft.create()
    m.postToChat("Good Day, Good Chaps!")
    m.setBlock(8,5,-14, block.GOLD_BLOCK.id)
    for x in range(10):
        for y in range(10):
            for z in range(10):
                if (x== 0 or x== 9 or y == 0 or y == 9 or z == 0 or z == 9):
                    m.setBlock(x+5,y+5,z+5,block.GOLD_BLOCK.id)
    m.setBlock (5,7,9,block.DOOR_WOOD.id)
    m.setBlock (5,6,9,block.DOOR_WOOD.id)

    

if __name__ == "__main__":
    main()

