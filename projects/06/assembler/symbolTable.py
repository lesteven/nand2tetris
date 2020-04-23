import copy
import re

# to do:
# translate symbols from decimal to binary
# automatically add addresses to variables

def toBinaryStr(num):
    return str("{0:016b}".format(num)) 

symbols = {
    'SP': toBinaryStr(0),
    'LCL': toBinaryStr(1),
    'ARG': toBinaryStr(2),
    'THIS': toBinaryStr(3),
    'THAT': toBinaryStr(4),
    'R0': toBinaryStr(0),
    'R1': toBinaryStr(1),
    'R2': toBinaryStr(2),
    'R3': toBinaryStr(3),
    'R4': toBinaryStr(4),
    'R5': toBinaryStr(5),
    'R6': toBinaryStr(6),
    'R7': toBinaryStr(7),
    'R8': toBinaryStr(8),
    'R9': toBinaryStr(9),
    'R10': toBinaryStr(10),
    'R11': toBinaryStr(11),
    'R12': toBinaryStr(12),
    'R13': toBinaryStr(13),
    'R14': toBinaryStr(14),
    'R15': toBinaryStr(15),
    'SCREEN': toBinaryStr(16384),
    'KBD': toBinaryStr(24576)
}

def stripLine(line):
    strippedLine = line.lstrip().rstrip()
    # remove comments after code
    modLine = strippedLine.partition('//')[0].rstrip()
    return modLine

# if pseudo  command add to table
def addToTableIfSymbol(line, symbolsCopy, num):
    if line[0] == '(':
        removeParen = line.replace('(',"").replace(')',"")
        symbolsCopy[removeParen] = toBinaryStr(num)
    return symbolsCopy


# run this method first to get all symbols
# for program
def getSymbols(fileName):
    symbolsCopy = copy.deepcopy(symbols)
    with open(fileName,"r") as f:
        num = 0
        for line in f:
            strippedLine = stripLine(line)
            if len(strippedLine) > 0 and strippedLine[0] != "/":
                #print(str(num) + " " + strippedLine)
                symbolsCopy = addToTableIfSymbol(strippedLine, symbolsCopy, num)
                if strippedLine[0] != '(':
                    num += 1
    return symbolsCopy


    

# run this during second iteration
def symbolParser(symbolTable):
    num = 16
    def symbolToAddress(parsed, symbolTable):
        nonlocal num
        if parsed['instructionType'] == 'a-instruction':
            splitA = parsed['line'].split('@')

            # if no letters, then it's not a symbol, so convert to binary
            if re.match('[a-zA-Z]', splitA[1]) is None:
                return toBinaryStr(int(splitA[1])) + '\n'
            # if in table, return value
            elif splitA[1] in symbolTable:
                return str(symbolTable[splitA[1]]) + '\n'
            else:
            # if symbol doesnt exist add to symbol table and return
                currNum = num
                symbolTable[splitA[1]] = toBinaryStr(currNum)
                num += 1
                return toBinaryStr(currNum) + '\n'
        return ''
    return symbolToAddress
