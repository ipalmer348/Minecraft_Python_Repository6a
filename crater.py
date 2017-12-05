from mcpi.minecraft import Minecraft
mc = Minecraft.create()

anser = input("Create a crater? Y/N ")

# Add an if statment here

pos = mc.player.getPos()
mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1,pos.x - 1, pos.y - 1, pos.z - 1, 0)
mc.postToChat("Boom!")

