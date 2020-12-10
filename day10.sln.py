file1 = open("day10.input.txt", 'r')
lines = file1.readlines()

loj = [0]
for line in lines:
    loj.append(int(line.rstrip()))


loj.sort()
loj.append(loj[-1]+3)
def part1():
    difference = {1: 0,3:0}
    prevJot = 0
    for jolt in loj[1:]:
        difference[jolt-prevJot] += 1

        prevJot = jolt
    print(difference[1]*difference[3])

def part2():
    temp = [0 for i in range(len(loj))]
    temp[0] = 1
    temp[1] = 1
    temp[2] = 2 if loj[2] <=3 else 1

    for i in range(3, len(loj)):
        if loj[i] - loj[i-1] <=3:
            temp[i] += temp[i-1] 
        if loj[i] - loj[i-2] <=3:
            temp[i] += temp[i-2] 
        if loj[i] - loj[i-3] <=3:
            temp[i] += temp[i-3] 
    print(temp[-1])
part1()