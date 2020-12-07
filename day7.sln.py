import re
file1 = open('day7.input.txt', 'r')
lines = file1.readlines()

bagRelationship = {}
allColor = []
for line in lines:
	line = line.rstrip().split("contain")
	parentColor = re.search(r'.+(?=\s+bags)', line[0]).group()
	allColor.append(parentColor)
	if parentColor not in bagRelationship:
		bagRelationship[parentColor] = []

	childrenBagLine = line[1][1:-1].split(", ") # remove last character
	for baginfo in childrenBagLine:
		childrenColor = re.search(r'(?<=\s)\w+\s\w+(?=\s+bags?)', baginfo)
		childrenNumber = re.search(r'^\d+(?=\s)', baginfo)
		if childrenColor:
			bagRelationship[parentColor].append((childrenColor.group(), childrenNumber.group()))

def part1():
	visited = {}
	ans = 0
	for color in allColor:
		if DFSHelper(color, visited):
			print(color)
			ans += 1

	return ans-1
def DFSHelper(color, visited):
	if color == "shiny gold":
		return True

	if color in visited:
		return visited[color]

	for neighborColor in bagRelationship[color]:
		if DFSHelper(neighborColor[0], visited):
			visited[color] = True
			return True
	visited[color] = False
	return False

def part2():
	visited = {}
	print(part2helper('shiny gold', visited))
	print(visited)

def part2helper(color, visited):
	if color in visited:
		return visited[color]

	totalBag = 0
	for children in bagRelationship[color]:
		childcolor = children[0]
		childnumber = int(children[1])
		totalBag += (childnumber + childnumber*part2helper(childcolor, visited))
	visited[color] = totalBag
	return totalBag

