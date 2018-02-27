from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def melon():
    """ Returns the value of the melon block """
    return 103

block = melon()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)
