import re

def is_bracket_balance(expression):
    open_brace=len(re.findall(r'\(',expression))
    close_brace=len(re.findall(r'\)',expression))
    return open_brace%2==0 and close_brace%2==0

expression="(a+b*(a/b)())"

if is_bracket_balance(expression):
    print("braces are proper")
else:
    print("braces are not proper")



