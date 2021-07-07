f1 = open("6f0o.pdb", "r")
f2 = open("A3.pdb", "r")

def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def findValue(value):
    for k in range(len(lines)):
        if(lines[k][13:26] == value[13:26]):
            return True;
def findIndex(value):
    for j in range(len(lines)):
        if (lines[j][13:26] == value[13:26]):
            return j;
def deleteExtra():
    for g in range(len(lines2)):
        if(find_nth_overlapping(lines2[g],'.', 7) == -1):
            lines2.remove(lines2[i])
            g-1


lines = [line for line in f1.readlines()]
lines2 = [line for line in f2.readlines()]
for i in range(len(lines2)):
    if(findValue(lines2[i])):
        index = findIndex(lines2[i])
        lines2[i] = lines2[i][0:find_nth_overlapping(lines2[i],'.', 4)+3] + " " + lines[index][find_nth_overlapping(lines[index],".",5)-2:find_nth_overlapping(lines[index],".",5)+3] + "           " + lines2[i][len(lines2[i])-2]
f3 = open("BAdded.txt", "w")
for i in lines2:
    f3.write(str(i))
    f3.write('\n')

