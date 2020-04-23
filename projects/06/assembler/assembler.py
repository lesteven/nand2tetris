import sys
import re
from parser import parseLine
from binaryCode import toBinary


def assembler(fileName):
    m = re.search('[a-zA-Z]+\.asm', fileName)
    name = m.group(0).split('.')[0] + '.hack'
    with open(name, 'w') as output:
        with open(fileName,"r") as f:
            num = 0
            for line in f:
                parsed = parseLine(line, num)
                if parsed == None:
                    continue
                #print(str(parsed) + " " + toBinary(parsed))
                # writes to file
                output.write(toBinary(parsed))
                num += 1


argArr = sys.argv

if len(argArr) < 2:
    print("You must provide a file")
else:
    fileName = argArr[1]
    assembler(fileName)
