import sys
import re


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
        if len(splitEqual) > 1:
            parsed['comp'] = splitEqual[1]
            parsed['dest'] = splitEqual[0]
        else:
            parsed['comp'] = splitEqual[0]
            parsed['dest'] = ''

    return parsed

num = ['000','001','010','011','100','101','110','111']
comp = {
    '0':'0' + num[5] + num[2],
    '1':'0' + num[7] + num[7],
    '-1':'0' + num[7] + num[2],
    'D':'0' + num[1] + num[4],
    'A':'0' + num[6] + num[0],
    '!D':'0' + num[1] + num[5],
    '!A':'0' + num[6] + num[1],
    '-D':'0' + num[1] + num[7],
    '-A':'0' + num[6] + num[3],
    'D+1':'0' + num[3] + num[7],
    'A+1':'0' + num[6] + num[7],
    'D-1':'0' + num[1] + num[6],
    'A-1':'0' + num[6] + num[2],
    'D+A':'0' + num[0] + num[2],
    'D-A':'0' + num[2] + num[3],
    'A-D':'0' + num[0] + num[7],
    'D&A':'0' + num[0] + num[0],
    'D|A':'0' + num[2] + num[5],
    'M':'1' + num[6] + num[0],
    '!M':'1' + num[6] + num[1],
    '-M':'1' + num[6] + num[3],
    'M+1':'1' + num[6] + num[7],
    'M-1':'1' + num[6] + num[2],
    'D+M':'1' + num[0] + num[2],
    'D-M':'1' + num[2] + num[3],
    'M-D':'1' + num[0] + num[7],
    'D&M':'1' + num[0] + num[0],
    'D|M':'1' + num[2] + num[5],
}

dest = {
    '': num[0],
    'M': num[1],
    'D': num[2],
    'MD': num[3],
    'A': num[4],
    'AM': num[5],
    'AD': num[6],
    'AMD': num[7],
}

jump = {
    '': num[0],
    'JGT': num[1],
    'JEQ': num[2],
    'JGE': num[3],
    'JLT': num[4],
    'JNE': num[5],
    'JLE': num[6],
    'JMP': num[7],
}

# to do
# convert a-instruction to binary
def toBinary(parsed):
    #print('parsed ' + str(parsed));
    if parsed['instructionType'] == 'a-instruction':
        splitA = parsed['line'].split('@')
        if re.match('[a-zA-Z]', splitA[1]) is None:
            return str("{0:016b}".format(int(splitA[1]))) + '\n'
        return splitA[1] + '\n'
    return '111' + comp[parsed['comp']] + dest[parsed['dest']] + jump[parsed['jump']] +'\n'
    


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
