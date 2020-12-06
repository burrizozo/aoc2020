file1 = open('day2.input.txt', 'r') 
Lines = file1.readlines()

def part1():
	ans = 0
	for line in Lines: 
		pwPolicy = line.split(" ")

		FreqLimit = pwPolicy[0].split("-")
		lowest = int(FreqLimit[0])
		highest = int(FreqLimit[1])

		targetLetter = pwPolicy[1][0]

		password = pwPolicy[2]

		targetLetterFreq = 0
		for letter in password:
			if letter == targetLetter:
				targetLetterFreq += 1

		if lowest <= targetLetterFreq <= highest:
			ans += 1

	return ans

def part2():
	ans = 0
	for line in Lines: 
		pwPolicy = line.split(" ")

		FreqLimit = pwPolicy[0].split("-")
		firstPosition = int(FreqLimit[0]) -1
		secondPosition = int(FreqLimit[1]) -1

		targetLetter = pwPolicy[1][0]

		password = pwPolicy[2]

		if (password[firstPosition] == targetLetter) ^ (password[secondPosition] == targetLetter):
			ans += 1

	return ans
print(part2())


