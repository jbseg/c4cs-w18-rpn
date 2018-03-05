#!/usr/bin/env python3
import readline
import colored
import operator

from colored import fg, bg, attr

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    color = fg('#c0c0c0') + bg('#00005f')
    reset = attr('reset')
    while True:
        result = calculate(input("rpn calc> "))
        print(color + "Result: " + reset, result)

if __name__ == '__main__':
    main()
