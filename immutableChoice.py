from mcpi.minecraft import Minecraft
mc = Minecraft
mc.setting("world_immutable",True)
mc.postToChat("World is immutable")
Answer = int(input("Do you want blocks to be immutable? Y/N"))
if Answer > Y:
    mc.setting("world_immutable", True)
    mc.postToChat("World is immutable")
    print("world is immutable")
    else:
        mc.postToChat("World is mutable")
        mc.setting("world_immutable", False)
        print("world is immutable")
        
        
    
        
        

