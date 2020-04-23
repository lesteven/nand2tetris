# parse line of code and separate int comp, dest, jump
def parseCode():
    num = 0
    def parseLine(line):
        nonlocal num
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
        num += 1

        return parsed
    return parseLine
