import math
file1 = open("day12.input.txt", 'r')
lines = file1.readlines()

def part1():
	curWayPointEW = 0
	curWayPointNS = 0
	curAngle = 0

	for line in lines:
		curEW, curNS, curAngle = executeInstructionP1(line.rstrip(), curEW, curNS, curAngle)

	print(abs(curNS) + abs(curEW))

def executeInstructionP1(instruction, curEW, curNS, curAngle):
	action = instruction[0]
	value = int(instruction[1:])

	if action == "N":
		curNS += value
	elif action == "S":
		curNS -= value
	elif action == "E":
		curEW += value
	elif action == "W":
		curEW -= value
	elif action == "R":
		curAngle -= value
	elif action == "L":
		curAngle += value
	elif action == "F":
		curEW += value*math.cos(math.radians(curAngle))
		curNS += value*math.sin(math.radians(curAngle))

	return curEW, curNS, curAngle

def part2():
	curShipX = 0
	curShipY = 0
	curWayX = 10
	curWayY = 1
	curAngle = 0

	for line in lines:
		curShipX, curShipY, curWayX, curWayY = executeInstruction(line.rstrip(), curShipX, curShipY, curWayX, curWayY)
	print(abs(curShipX) + abs(curShipY))

def executeInstruction(instruction, curShipX, curShipY, curWayX, curWayY):
	action = instruction[0]
	value = int(instruction[1:])

	if action == "N":
		curWayY += value
	elif action == "S":
		curWayY -= value
	elif action == "E":
		curWayX += value
	elif action == "W":
		curWayX -= value
	elif action == "R":
		curWayX, curWayY = rotateWaypoint(curWayX, curWayY, -1*value)
	elif action == "L":
		curWayX, curWayY = rotateWaypoint(curWayX, curWayY, value)
	elif action == "F":
		curShipX += value*curWayX
		curShipY += value*curWayY
	return curShipX, curShipY, curWayX, curWayY

def rotateWaypoint(wayX, wayY, angle):
	newWayX = round(wayX*math.cos(math.radians(angle))-wayY*math.sin(math.radians(angle)))
	newWayY = round(wayX*math.sin(math.radians(angle))+wayY*math.cos(math.radians(angle)))
	return newWayX, newWayY

part2()