import re
file1 = open('day8.input.txt', 'r')
lines = file1.readlines()

def executeCommand(command):
	if command[0] == "nop":
		return 0, 1
	elif command[0] == "jmp":
		return 0, int(command[1])
	else:
		return int(command[1]), 1

def part1():
	loc = []
	for line in lines:
		commandStatus = (line.rstrip().split(" "), False)
		loc.append(commandStatus)

	locLength = len(loc)
	currentCommandIndex = 0
	currentSpeed = 0
	while(not loc[currentCommandIndex][1]):
		# reset visited status
		commandText = loc[currentCommandIndex][0]
		loc[currentCommandIndex] = (commandText, True)
		speedD, indexD = executeCommand(commandText)
		currentSpeed += speedD
		currentCommandIndex += indexD

def part2():
	#index -> currentAcc
	problematicCommand ={}
	loc = []
	for line in lines:
		commandStatus = (line.rstrip().split(" "), False)
		loc.append(commandStatus)
	constructGraph(problematicCommand, loc)
	return fixProgram(problematicCommand, loc)

def constructGraph(problematicCommand, loc):
	currentCommandIndex = 0
	currentSpeed = 0
	while(not loc[currentCommandIndex][1]):
		commandText = loc[currentCommandIndex][0]
		loc[currentCommandIndex] = (commandText, True)
		if commandText[0] != "acc":
			problematicCommand[currentCommandIndex] = currentSpeed
		speedD, indexD = executeCommand(commandText)
		currentSpeed += speedD
		currentCommandIndex += indexD

def fixProgram(problematicCommand, loc):
	lenOfLoc = len(loc)
	for commandIndex, currentSpeed in problematicCommand.items():
		commandText = loc[commandIndex][0]
		if commandText[0] == "nop":
			currentIndex = commandIndex + int(commandText[1])
		else:
			currentIndex = commandIndex + 1
		while((currentIndex < lenOfLoc) and (currentIndex not in problematicCommand)):
			speedD, indexD = executeCommand(loc[currentIndex][0])
			currentSpeed += speedD
			currentIndex += indexD
			if currentIndex >= lenOfLoc:
				return currentSpeed
print(part2())