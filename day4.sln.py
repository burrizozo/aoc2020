import re

file1 = open('day4.input.txt', 'r')
lines = file1.readlines()

def processCurrentPassport(passport):
	currentfield = []
	score = 0
	for i in passport:
		i = i.split(" ")
		for fieldinfo in i:
			field = fieldinfo[0:3]
			info = fieldinfo[4:]
			if field == 'cid':
				continue

			if checkInfo(field, info):
				score += 1
			else:
				return False

	if score == 7:
		return True

	retrun False

def checkInfo(field, info):
	if field == "byr":
		return re.search(r'^[0-9]{4}$', info) and 1920 <= int(info) <= 2002
	elif field == "iyr":
		return re.search(r'^[0-9]{4}$', info) and 2010 <= int(info) <= 2020
	elif field == "eyr":
		return re.search(r'^[0-9]{4}$', info) and 2020 <= int(info) <= 2030
	elif field == "hgt":
		return ((re.search(r'cm$', info) is not None) and 150 <= int(info[:-2]) <= 193) or \
		((re.search(r'in$', info) is not None) and 59 <= int(info[:-2]) <= 76)
	elif field == "hcl":
		return re.search(r'^#[0-9a-f]{6}$', info) is not None
	elif field == "ecl":
		return info in ["amb","blu", "brn", "gry", "grn", "hzl", "oth"]
	elif field == "pid":
		return re.search(r'^[0-9]{9}$', info) is not None

def main():
	ans = 0
	currentPassport = []
	for line in lines:
		if line != "\n":
			currentPassport.append(line.rstrip('\n'))
		else:
			if processCurrentPassport(currentPassport):
				ans += 1
			currentPassport = []

	if currentPassport != []:
		if processCurrentPassport(currentPassport):
				ans += 1
	print(ans)

main()