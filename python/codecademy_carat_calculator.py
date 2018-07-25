# You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of positive integers.

# Given an expression string using the "+" and "-" operators like "5+16-2", write a function to parse the string and returns the result.
import string
# import pdb
import operator

expression1 = "(5+16-((9-6)-(4-2)))"
expression2 = "22+(2-4)"


TYPE = {
    'OPEN_PAREN': 0,
    'CLOSE_PAREN': 1,
    'OPERATOR': 2,
    'DIGIT': 3,
}

VALUES = (
    '(',
    ')',
    '+-',
    string.digits,
)

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
}


class Node():
    def __init__(self):
        self.value = None
        self.type = None
        self.p = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def build_tree(expression):
    tokens = []
    current_number = ''
    for char in expression:
        if char in VALUES[TYPE['DIGIT']]:
            current_number += char
        else:
            if current_number:
                tokens.append(int(current_number))
                current_number = ''
            tokens.append(char)

    print(tokens)

    current_node = root = Node()

    if tokens[0] is not VALUES[TYPE['OPEN_PAREN']]:
        p = current_node
        p.left = Node()
        current_node = p.left
        current_node.p = p

    for token in tokens:
        if token is VALUES[TYPE['OPEN_PAREN']]:
            # print('OPEN_PAREN: %s' % token)
            # traverse to left node
            p = current_node
            p.left = Node()
            current_node = p.left
            current_node.p = p

        elif type(token) is int:
            # set current node value
            current_node.value = token

            # traverse to parent node
            current_node.type = TYPE['DIGIT']
            # print('DIGIT: %d' % token)
            current_node = current_node.p

        elif token in VALUES[TYPE['OPERATOR']]:
            # print('OPERATOR: %s' % token)
            # set current node value

            if current_node.value:
                while current_node.p:
                    current_node = current_node.p

                new_node = Node()
                new_node.left = current_node
                current_node.p = new_node
                root = current_node = new_node

            current_node.value = token
            current_node.type = TYPE['OPERATOR']

            # traverse to right node
            p = current_node
            p.right = Node()
            current_node = p.right
            current_node.p = p

        elif token is VALUES[TYPE['CLOSE_PAREN']]:
            # print('CLOSE_PAREN: %s' % token)
            # traverse to parent node
            current_node = current_node.p

        else:
            raise ValueError('invalid')

    return root


def evaluate_tree(node):
    print(node)
    if node.left and node.right:
        # operator node: has left and right
        operation = OPERATORS[node.value]
        return operation(evaluate_tree(node.left), evaluate_tree(node.right))
    else:
        # digit nodes all leaves
        return node.value


def evaluate_expression_as_tree(expression):
    return evaluate_tree(build_tree(expression))


def evaluate_expression(expr):
    current_sign_is_positive = True
    current_int = ''
    values = []

    c = 0
    while c < len(expr):
        char = expr[c]

        print(char)

        if char in '+-':
            # print('found +-, current int is %s' % current_int)
            if current_sign_is_positive:
                values.append(int(current_int))
            else:
                values.append(-int(current_int))

            current_int = ''
            if char is '-':
                current_sign_is_positive = False
            else:
                current_sign_is_positive = True

        # handle parens
        elif char is '(':
            n = c
            paren_open = True
            paren_depth = 1
            while paren_open:
                n += 1
                print('testing for close paren at %s' % expr[n])
                if expr[n] is ')':
                    print('found close paren')
                    paren_depth -= 1
                elif expr[n] is '(':
                    paren_depth += 1

                print('current paren depth is %d' % paren_depth)
                if paren_depth == 0:
                    paren_open = False

            paren_value = evaluate_expression(expr[c:n])
            if current_sign_is_positive:
                values.append(paren_value)
            else:
                values.append(-paren_value)

            c = n

        elif char in string.digits:
            current_int += char
            # print('found digit, current int is %s' % current_int)
        else:
            raise ValueError('invalid')

        print(values)
        c += 1

    if current_sign_is_positive:
        values.append(int(current_int))
    else:
        values.append(-int(current_int))


    return sum(values)

# print(evaluate_expression(expression2))

print(evaluate_expression_as_tree(expression1))
