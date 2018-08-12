def validate_parenthesis(expression):
    stack = []
    parenthesis_map = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }
    for token in expression:
        if token in parenthesis_map:
            stack.append(token)
        else:
            ch = stack.pop()
            if parenthesis_map[ch] != token:
                return False        
    if len(stack):
        return False
    return True

if __name__=="__main__":
    expression = "(())()"
    print expression, validate_parenthesis(expression)
    expression = "(())("
    print expression, validate_parenthesis(expression)
    expression = "([])({})"
    print expression, validate_parenthesis(expression)
    expression = "([]({})"
    print expression, validate_parenthesis(expression)