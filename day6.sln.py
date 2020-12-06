file1 = open('day6.input.txt', 'r')
lines = file1.readlines()

def part1():
	ans = 0
	questionset = set()
	for line in lines:
		if line != "\n":
			for question in line.rstrip():
				questionset.add(question)
		else:
			ans += len(questionset)
			questionset = set()
	ans += len(questionset)
	print(ans)

def part2():
	ans = 0
	questionset = {}
	headcount = 0
	for line in lines:
		if line != "\n":
			headcount += 1
			for question in line.rstrip():
				if question not in questionset:
					questionset[question] = 1
				else:
					questionset[question] += 1
		else:
			ans += sum(x == headcount for x in questionset.values()) 
			questionset = {}
			headcount = 0
	ans += sum(x == headcount for x in questionset.values()) 
	print(ans)
part2()