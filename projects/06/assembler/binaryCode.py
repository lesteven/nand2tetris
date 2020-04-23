import re

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

        # if no letters, then not symbol, so convert to binary
        if re.match('[a-zA-Z]', splitA[1]) is None:
            return str("{0:016b}".format(int(splitA[1]))) + '\n'
        # else remove '@' and return symbol
        return splitA[1] + '\n'
    return '111' + comp[parsed['comp']] + dest[parsed['dest']] + jump[parsed['jump']] +'\n'
