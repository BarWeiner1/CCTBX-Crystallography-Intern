x=[0,1,2,3,4,5,6]
y=[0,1,2,3,4,5,6,7,8,9]
item1='(343.6, 173.5, 108.95) 128.415637741\n'
def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start
z="ATOM      1  N   THR A 868       2.865 -10.740  34.328  1.00"
print(find_nth_overlapping(z, '.', 58))
