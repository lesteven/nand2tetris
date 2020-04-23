import sys


def parseLine(line):
    strippedLine = line.lstrip().rstrip()
    if len(strippedLine) == 0 or strippedLine[0] == "" \
        or strippedLine[0] == "/":
        return None
    return strippedLine

def assembler(fileName):
    with open(fileName,"r") as f:
        num = 0
        for line in f:
            parsed = parseLine(line)
            if (parsed == None):
                continue
            print(str(num) + " " + parsed)
            num += 1


argArr = sys.argv

if len(argArr) < 2:
    print("You must provide a file")
else:
    fileName = argArr[1]
    assembler(fileName)
