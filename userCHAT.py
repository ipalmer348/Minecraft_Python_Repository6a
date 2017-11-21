from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = "this is the default message. "
mc.postToChat(message)
username = input("Please enter a username:")
message = input("Enter your message: ")

