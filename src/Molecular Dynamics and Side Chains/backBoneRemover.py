def removeSideChain(fileName,num):
    f1 = open(fileName, "r")
    f2 = open(r"R" + str(num) + ".pdb", 'w')
    lines = [line for line in f1.readlines()]
    def find_nth_overlapping(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+1)
            n -= 1
        return start
    for i in lines:
        if(i.find(" CA ")!= -1 or i.find(" C ")!= -1 or i.find(" N ")!= -1 or i.find(" O ")!= -1):
            f2.write((i))


for i in range(578):
    removeSideChain(str(i+1) + ".pdb", (i+1))



