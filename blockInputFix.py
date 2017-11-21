from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
try:
    mc.setBlock(x, y, z, blocktype)
    blockType = int(input("Enter a block type: "))
except:
    mc.postToChat("You did not enter a number! Enter a number next time.")
    
