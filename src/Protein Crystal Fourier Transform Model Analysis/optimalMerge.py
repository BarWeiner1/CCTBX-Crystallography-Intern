import functools
def run():
    f1 = open("computedValues.txt", "r")
    f2 = open("theoreticalValues.txt", "r")
    f3 = open(r"merge.txt", 'w')
    def find_nth_overlapping(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+1)
            n -= 1
        return start
    def compare(item1, item2):
        if (float(item1[item1.find('(') + 1: item1.find(',')]) > float(item2[item2.find('(') + 1: item2.find(',')])):
            return 1
        elif(float(item1[item1.find('(') + 1: item1.find(',')]) < float(item2[item2.find('(') + 1: item2.find(',')])):
            return -1
        elif(float(item1[item1.find(',')+2:find_nth_overlapping(item1,",",2)]) > float(item2[item2.find(',')+2:find_nth_overlapping(item2,",",2)])):
            return 1
        elif(float(item1[item1.find(',')+2:find_nth_overlapping(item1,",",2)]) < float(item2[item2.find(',')+2:find_nth_overlapping(item2,",",2)])):
            return -1
        elif (float(item1[find_nth_overlapping(item1, ",", 2) + 1: item1.find(')')]) > float(item2[find_nth_overlapping(item2, ",", 2) + 1:item2.find(')')])):
            return 1
        elif(float(item1[find_nth_overlapping(item1, ",", 2) + 1: item1.find(')')]) < float(item2[find_nth_overlapping(item2, ",", 2) + 1:item2.find(')')])):
            return -1
        elif(item1[item1.find('('):item1.find(')')] == item2[item2.find('('):item2.find(')')]):
            return 0
        else:
            return -1

    lines = [line for line in f1.readlines()]
    lines2 =[line for line in f2.readlines()]
    lines.extend(lines2)
    total = sorted(lines, key=functools.cmp_to_key(compare))
    for i in range(len(total)-1):
        line1 = total[i]
        line2 = total[i+1]
        if(line1[line1.find('('):line1.find(')')] == line2[line2.find('('):line2.find(')')]):
            String = line2[line2.find(')') + 1: line2.find('.') + 2], line1[line1.find(')') + 1:]
            String = str(String)
            String = String[2:String.find(',')-1] + " " + String[String.find(',')+4:String.find(')')-4]
            f3.write((String) + '\n')




