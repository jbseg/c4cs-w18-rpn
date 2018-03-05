#!/usr/bin/env python3
import readline
import colored
import operator

from colored import fg, bg, attr, stylize

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
            f = token
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
            color = bg(5) +  fg(29)
            minus  = bg(1) + fg(20)
            print(stylize('{}'.format(arg1), color)),
            if f == '-':
                print(stylize('{}'.format(f), minus)),
            else:
                print(stylize('{}'.format(f), color)),
            print(stylize('{}'.format(arg1), color)) 
        angry = colored.fg("red") + colored.attr("bold")
        print(stylize(stack, angry))
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("<rpn calc> "))
        print('%s%s Result:  %s' % (fg(10), bg(13), attr(0))),
	print(result)

if __name__ == '__main__':
    main()
