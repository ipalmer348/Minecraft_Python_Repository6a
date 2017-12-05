from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = 1
y = 7
z = 1
width = 10
height = 5
length = 6
blockType = 4
air = 0
lava = 11
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
mc.setBlocks(x+1, y+1, z+1, x-1 + width, y-1 + height, z-1 + length, air)
gift = mc.getBlock(0, 10, 2)
print(gift)
if gift != 0:
    if gift == 57:
        mc.setBlocks(1, 8, 3, air)
        mc.setBlocks(1, 9, 3, air)
    else:
        mc.setBlocks(0, 7, 4, lava)
else:
    mc.postToChat("Place an offering on the pedestal.")
    
