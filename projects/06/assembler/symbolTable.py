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

def addToTableIfSymbol(line, symbolsCopy):
    if len(line) > 1 and line[0] == '@':
        splitA = line.split('@')[1]
        # print(splitA)
        if splitA not in symbolsCopy:
            symbolsCopy[splitA] = ''
    return symbolsCopy


# run this method first to get all symbols
# for program
def getSymbols(fileName):
    symbolsCopy = copy.deepcopy(symbols)
    with open(fileName,"r") as f:
        for line in f:
            strippedLine = stripLine(line)
            symbolsCopy = addToTableIfSymbol(strippedLine, symbolsCopy)
    return symbolsCopy


    

# run this during second iteration
def symbolToAddress(parsed, symbolTable):
    if parsed['instructionType'] == 'a-instruction':
        splitA = parsed['line'].split('@')

        # if no letters, then not symbol, so convert to binary
        if re.match('[a-zA-Z]', splitA[1]) is None:
            return toBinaryStr(int(splitA[1])) + '\n'
        # else remove '@' and return symbol
        if symbolTable[splitA[1]] != '':
            return symbolTable[splitA[1]] + '\n'
        else:
            # increment and return binary string of incremented address
            return ''
    return ''
