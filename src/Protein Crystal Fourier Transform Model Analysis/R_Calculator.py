def calc_R():
    f1 = open("merge.txt", "r")
    Difference= 0
    Sum=0

    for i in f1:
        print(float(i[0:i.find(".")+1]))
        Sum = Sum + float(i[0:i.find(".")+1])

    f1.seek(0)
    for j in f1:
        num1= float(j[0:j.find(".")+1])
        num2= float(j[j.find(".")+3: ])
        Difference = Difference + abs(num1-num2)

    rFactor = Difference/Sum
    return rFactor


