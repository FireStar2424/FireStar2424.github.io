# tutorial link: https://www.makeuseof.com/python-text-adventure-game-create/
import time
weapon = False

def strangeCreature():
actions = ["fight", "flee"]
global weapon
print("a strange ghoul-like creature has appeared. what will you do?")
userInput = ""
while userInput not in actions:
print("options: flee/fight")
userInput = input()
if userInput == "fight":
if weapon:
print("you kill the creature. it looks like it was guarding an exit. you escape.")
time.sleep(1)
quit()
else:
print("the strange creature kills you.")
time.sleep(1)
quit()
elif userInput == "flee":
showSkeletons()
else:
print("invalid selection")
def showSkeletons():
directions = ["forward", "backward"]
global weapon
print("you see a wall of skeletons, giving you the creeps. you can feel someone's gaze. what will you do?")
userInput = ""
while userInput not in directions:
print("options: left/forward/backward")
userInput = input()
if userInput == "left":
print("a dead end. you look carefully in the walls and see there's a hole, and you tear it open and find a sword.")
weapon = True
elif userInput == "forward":
strangeCreature()
elif userInput == "backward":
introScene()
else:
print("invalid selection")
def hauntedRoom():
directions = ["right", "left", "backward"]
print("you hear haunting sounds. perhaps you woke of some of the dead? where would you like to go?")
userInput = ""
while userInput not in directions:
print("options: right/left/backward")
userInput = input()
if userInput == "right":
print("several ghosts emerge. you are killed.")
time.sleep(1)
quit()
elif userInput == "left":
print("you reach an exit and escape")
time.sleep(1)
quit()
elif userInput == "backward":
introScene()
else:
print("invalid selection")
def cameraScene():
directions = ["forward", "backward"]
print("you see a camera on the ground. someone's been here recently. where do you go?")
userInput = ""
while userInput not in directions:
print("options: forward/backward")
userInput = input()
if userInput == "forward":
print("you see a stream of light ahead... you found an exit")
time.sleep(1)
quit()
elif userInput == "backward":
showShadowFigure()
else:
print("invalid selection")
def showShadowFigure():
directions = ["right", "backward"]
print("you see something shadowy ahead that gives you the creeps. where do you go?")
userInput = ""
while userInput not in directions:
print("options: left/right/backward")
userInput = input()
if userInput == "right":
cameraScene()
elif userInput == "left":
print("it appears to be a dead end")
elif userInput == "backward":
introScene()
else:
print("invalid selection")
def introScene():
directions = ["left", "right", "forward"]
print("in front of you is a crossroad. what path will you choose?")
userInput = ""
while userInput not in directions:
print("options: left/right/forward/backward")
userInput = input()
if userInput == "left":
showShadowFigure()
elif userInput == "right":
showSkeletons()
elif userInput == "forward":
hauntedRoom()
elif userInput == "backward":
print("it appears to be a dead end")
else:
print("invalid selection")
if __name__ == "__main__":
while True:
print("you, an avid explorer, stumble across a dungeon.")
print("while exploring, it appears you've become lost.")
print("it's up to you to find the exit, but beware, there are many dangers.")
print("brave traveler, may i ask what your name is?")
name = input()
print("best of luck, " +name+ ".")
introScene()
