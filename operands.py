numbers = '0123456789'
operands = {
    '=': 'equals',
    '+': 'plus',
    '-': 'minus',
    '%': 'percent',
    '÷': 'digit',
    '×': 'X'
}

methods = {
    ',': 'add_coma',
    'AC': 'reset',
    '+/-': 'change_sign'
}

def getTypeCommand(text):
    if text in numbers:
        return 'number'
    if text in methods.keys():
        return 'method'
    if text in operands.keys():
        return 'operand'
