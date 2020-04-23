import sys


def parseLine(line, num):
    strippedLine = line.lstrip().rstrip()
    if len(strippedLine) == 0 or strippedLine[0] == "" \
        or strippedLine[0] == "/" or strippedLine[0] == "(":
        return None

    # remove comments after code
    modLine = strippedLine.partition('//')[0].rstrip()

    instructionType = 'a-instruction' if modLine[0] == '@' \
        else 'c-instruction'

    parsed = { 
        'line': modLine, 
        'address': num,
        'instructionType': instructionType
    }
    if instructionType != 'a-instruction':
        splitColon = modLine.split(';')
        parsed['jump'] = splitColon[1] if len(splitColon) > 1 else ''

        splitEqual = splitColon[0].split('=')
        parsed['comp'] = splitEqual[1] if len(splitEqual) > 1 else ''
        parsed['dest'] = splitEqual[0]

    return parsed

def assembler(fileName):
    with open(fileName,"r") as f:
        num = 0
        for line in f:
            parsed = parseLine(line, num)
            if parsed == None:
                continue
            print(parsed)
            num += 1


argArr = sys.argv

if len(argArr) < 2:
    print("You must provide a file")
else:
    fileName = argArr[1]
    assembler(fileName)
