file1 = open('day5.input.txt', 'r')
lines = file1.readlines()

def part1():
	ans = 0
	for line in lines:
		line = line.rstrip()
		rowinfo = line[:-3]
		colinfo = line[-3:]

		rowNum = findSeat(rowinfo, 'row')
		colNum = findSeat(colinfo, 'col')
		seatId = rowNum*8 + colNum

		ans = max(seatId, ans)

	return ans

def part2():
	idList = []
	for line in lines:
		line = line.rstrip()
		rowinfo = line[:-3]
		colinfo = line[-3:]

		rowNum = findSeat(rowinfo, 'row')
		colNum = findSeat(colinfo, 'col')
		seatId = rowNum*8 + colNum

		idList.append(seatId)

	idList.sort()
	idListLen =  len(idList)
	for i in range(1,idListLen -1 ):
		if idList[i-1] == idList[i] - 2:
			print(idList[i-1], idList[i])


def findSeat(info, rowOrCol):
	lower = 0
	higher = 127 if rowOrCol == 'row' else 7

	for letter in info:
		halfRange = (higher-lower + 1) // 2
		if letter == "B" or letter == "R":
			lower += halfRange
		else:
			higher = lower+halfRange -1

	if lower != higher:
		print("ERROR")
		return

	return lower

part2()
