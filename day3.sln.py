file1 = open('day3.input.txt', 'r')
lines = file1.readlines()[1:]
 
def part1(right, down):
	row = 0
	rowLen = len(lines[0])-1
	ans = 0
	currentDown = down
	for line in lines:
		currentDown -= 1
		if currentDown == 0:
			currentDown = down
			row += 1
			column = right*row
			columnIndex = column %rowLen
			if line[columnIndex] == '#':
				ans += 1

	return ans
print(part1(1, 1)*part1(3, 1)*part1(5, 1)*part1(7, 1)*part1(1, 2))