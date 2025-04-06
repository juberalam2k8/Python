import re

def is_balanced(expression):
    # Count occurrences of opening and closing parentheses
    open_count = len(re.findall(r'\(', expression))
    close_count = len(re.findall(r'\)', expression))
    
    # Check if both counts are even
    return (open_count % 2 == 0) and (close_count % 2 == 0)

# Example usage:
expression = "(a + b) * (c + d)"
if is_balanced(expression):
    print("The expression has balanced parentheses.")
else:
    print("The expression does not have balanced parentheses.")

------------------------------------------------------------

import re

def is_balanced(expression):
    # Dictionary to map closing brackets to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Remove all whitespace characters
    expression = re.sub(r'\s+', '', expression)
    # Regular expression pattern to match any pair of brackets
    pattern = r'\(\)|\{\}|\[\]'
    # Iterate until no more pairs can be removed
    while re.search(pattern, expression):
        expression = re.sub(pattern, '', expression)
    # After removal, if the expression is empty, brackets are balanced
    return expression == ''

# Example usage:
expression = "(a + b * [c / d] {e + f} <g + h>)"
if is_balanced(expression):
    print("The expression has balanced brackets.")
else:
    print("The expression does not have balanced brackets.")

----------------------------------------------------------------------

def is_balanced(expression):
    # Dictionary to map closing brackets to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in expression:
        if char in bracket_map.values():
            # If it's an opening bracket, push to stack
            stack.append(char)
        elif char in bracket_map.keys():
            # If it's a closing bracket, check for match
            if not stack or stack.pop() != bracket_map[char]:
                return False
    # If stack is empty, all brackets are balanced
    return not stack

# Example usage:
expression = "(a + b * [c / d] {e + f} <g + h>)"
if is_balanced(expression):
    print("The expression has balanced brackets.")
else:
    print("The expression does not have balanced brackets.")


