from mcpi.minecraft import Minecraft
mc= Minecraft.create()

points = int(input("Enter your points: "))
if points > 2:
    mc.player.setPos(134, 39, 134)
elif points > 6:
    MC.player.setPos(172, 34, 48)
elif points > 4:
    mc.player.setPos(70, 10, 93)
elif points <=  2:
    mc.player.setPos(36, 34, 124)
    
else:
    mc.postToChat("I don't know what to do with that information.")
    
