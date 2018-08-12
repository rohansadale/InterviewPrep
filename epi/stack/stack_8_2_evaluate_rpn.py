def evaluate_rpn(expression):
    result = []
    DELIMITER = ","
    OPERATORS = {
        "+": lambda x, y : x+y,
        "-": lambda x, y : x-y,
        "*": lambda x, y : x*y,
        "/": lambda x, y : x/y
    }

    for token in expression.split(DELIMITER):    
        if token in OPERATORS:
            temp_result = OPERATORS[token](result.pop(), result.pop())            
            result.append(temp_result)
        else:
            result.append(int(token))
    return result[-1]

if __name__=="__main__":
    expression="3,4,+,2,*,1,+"
    print "Evaluating - ", expression
    print evaluate_rpn(expression)