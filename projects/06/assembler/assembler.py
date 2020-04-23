import sys
import re
from parser import parseCode
from binaryCode import toBinary
from symbolTable import getSymbols,symbolParser


def extractName(fileName):
    m = re.search('[a-zA-Z]+\.asm', fileName)
    name = m.group(0).split('.')[0] + '.hack'
    return name

def assembler(fileName):
    name = extractName(fileName)
    symbolTable = getSymbols(fileName)
    #print(symbolTable)
    symbolToAddress = symbolParser(symbolTable)
    with open(name, 'w') as output:
        with open(fileName,"r") as f:
            parseLine = parseCode()
            for line in f:
                parsed = parseLine(line)
                if parsed == None:
                    continue
                #print(str(parsed) + " " + toBinary(parsed))
                #writes to file
                binaryLine = ''
                if parsed['instructionType'] == 'a-instruction':
                    binaryLine = symbolToAddress(parsed, symbolTable)
                else:
                    binaryLine = toBinary(parsed)
                output.write(binaryLine)


argArr = sys.argv

if len(argArr) < 2:
    print("You must provide a file")
else:
    fileName = argArr[1]
    assembler(fileName)
