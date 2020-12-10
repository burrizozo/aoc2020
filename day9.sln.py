file1 = open("day9.input.txt", 'r')
lines = file1.readlines()

preamble = lines[:25]
lolines = len(lines)
currentFreqCount = {}
i = 25

def checkRules(targetNumber, preamble, currentFreqCount):
	for key, value in currentFreqCount.items():
		if currentFreqCount[key] <= 0:
			continue
		currentFreqCount[key]  -= 1
		if (((targetNumber - key) in currentFreqCount) and (currentFreqCount[targetNumber-key] > 0)):
			currentFreqCount[key] += 1
			return True
		currentFreqCount[key] += 1
	return False

def part1():
	for number in preamble:
		if number not in currentFreqCount:
			currentFreqCount[int(number)] = 1
		else:
			currentFreqCount[int(number)] += 1

	while (i < lolines):
		targetNumber = int(lines[i])
		if (not checkRules(targetNumber, preamble, currentFreqCount)):
			print(targetNumber)

		currentFreqCount[int(lines[i-25])] -= 1
		if targetNumber not in currentFreqCount:
			currentFreqCount[targetNumber] = 1
		else:
			currentFreqCount[targetNumber] += 1
		i += 1

def part2(targetNumber):
	totalsum = 0
	leftIndex = 0
	rightIndex = 0
	while(totalsum != targetNumber):
		if totalsum < targetNumber:
			totalsum += int(lines[rightIndex])
			rightIndex += 1
		else:
			totalsum -= int(lines[leftIndex])
			leftIndex += 1
	print(lines[leftIndex:rightIndex+1])

part2(258585477)
27525818-11137204
