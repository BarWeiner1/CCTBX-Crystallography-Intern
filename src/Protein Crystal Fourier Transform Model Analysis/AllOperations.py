import R_Calculator
import pdbMap
import optimalMerge
import iotbx.pdb
def runScripts(fileName):
    pdbMap.pdbMap(fileName)
    print(1)
    optimalMerge.run()
    print(2)
    R_Value = R_Calculator.calc_R()
    print(R_Value)
    f2.write(str(R_Value) + '\n')

f2 = open(r"R_Values.txt", 'w')
#for i in range(96):
#runScripts(("A" + str(i+1) + ".pdb"))
runScripts("BAdded.txt")
