from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTile()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(x, z)
mc.postToChat(highestBlockY)
