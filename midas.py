from mcpi.minecraft import Minecraft
mc = Minecraft.create()


air = 0
water = 9

pos = mc.player.getTilePos()
blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)

while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if blockBelow != 0 and blockBelow != 9:
        mc.setBlock(pos.x, pos.y - 1, pos.z, 41)
        print("blockBelow")


  
