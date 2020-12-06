file1 = open('day1.input.txt', 'r') 
Lines = file1.readlines() 
  
nums = []
# Strips the newline character 
for line in Lines: 
    nums.append(int(line))

nums.sort()

def part1(goal):
	i = 0
	j = len(nums)-1
	while i < j:
		if nums[i] + nums[j] == goal:
			return nums[i]*nums[j]
		elif nums[i] + nums[j] > goal:
			j -= 1
		else:
			i += 1

	return -1
def part2():
	for i in nums:
		ans = part1(2020-i) 
		if ans> 0:
			return i*ans

	return -1

print(part2())