f1 = open("computedValues.txt", "r")
f2 = open("theoreticalValues.txt", "r")
f3 = open(r"merge.txt", 'w')



def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start
for line1 in f1:
    for line2 in f2:
        if (line1[line1.find('('):line1.find(')')] == line2[line2.find('('):line2.find(')')]):
            String = line2[line2.find(')')+1: find_nth_overlapping(line2," ", 4)],line1[line1.find(')')+1:]
            String = str(String)
            String = String[2:String.find(',')-1] + " " + String[String.find(',')+4:String.find(')')-4]
            f3.write(String + '\n')
