file1 = open("day11.input.txt", 'r')
lines = file1.readlines()

rowNum = len(lines)
grid = []
for line in lines:
	currRow = line.rstrip()
	grid.append(list(currRow))
colNum = len(grid[-1])

def part1():
	currentOccupied = 0
	changedSeatCount = -1
	while(changedSeatCount != 0):
		changedSeat = []
		checkSeatsP1(changedSeat)
		changedSeatCount = len(changedSeat)
		currentOccupied = updateCurrentOccupied(changedSeat, currentOccupied)
	print(currentOccupied)

def updateCurrentOccupied(changedSeat, currentOccupied):
	for seat in changedSeat:
		currentChar = grid[seat[0]][seat[1]] 
		if currentChar == 'L':
			grid[seat[0]][seat[1]] = '#'
			currentOccupied += 1
		elif currentChar == '#':
			grid[seat[0]][seat[1]] = 'L'
			currentOccupied -= 1

	return currentOccupied

def checkSeatsP1(changedSeat):
	for i in range(rowNum):
		for j in range(colNum):
			occupied = checkNeighborsP1(i, j)
			if grid[i][j] == 'L' and occupied == 0:
				changedSeat.append((i, j))
			elif grid[i][j] == '#' and occupied >= 4:
				changedSeat.append((i, j))


def checkNeighborsP1(row, col):
	occupied = 0
	neighborIndex = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	for neighbor in neighborIndex:
		neighborRow = row + neighbor[0]
		neighborCol = col + neighbor[1]
		if ((0 <= neighborRow < rowNum) and (0 <= neighborCol < colNum)):
			if grid[neighborRow][neighborCol] == '#':
				occupied += 1

	return occupied

def part2():
    currentOccupied = 0
    changedSeatCount = -1
    while(changedSeatCount != 0):
        changedSeat = []
        checkSeatsP2(changedSeat)
        changedSeatCount = len(changedSeat)
        currentOccupied = updateCurrentOccupied(changedSeat, currentOccupied)
    print(currentOccupied)

def checkSeatsP2(changedSeat):
    for i in range(rowNum):
        for j in range(colNum):
            occupied = checkNeighborsP2(i, j)
            if grid[i][j] == 'L' and occupied == 0:
                changedSeat.append((i, j))
            elif grid[i][j] == '#' and occupied >= 5:
                changedSeat.append((i, j))

def checkNeighborsP2(row, col):
    occupied = 0
    neighborIndex = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for neighbor in neighborIndex:
        neighborRow = row + neighbor[0]
        neighborCol = col + neighbor[1]
        while ((0 <= neighborRow < rowNum) and (0 <= neighborCol < colNum)):
            if grid[neighborRow][neighborCol] == '#':
                    occupied += 1
                    break
            if grid[neighborRow][neighborCol] == 'L':
                    break
            neighborRow += neighbor[0]
            neighborCol += neighbor[1]
    return occupied
part2()