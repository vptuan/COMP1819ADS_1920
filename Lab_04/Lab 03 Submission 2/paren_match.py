from array_stack_common import ArrayStack
import time
start_time = time.time()


def expression_checker(expression):
    stack = ArrayStack()

    for char in expression:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        # Stack start with ({[ ?
        if stack.is_empty():
            return False
        # Remove opening paren from stack if the top item in the stack matches
        if char == ')':
            if stack.top() == '(':
                stack.pop()
        if char == '}':
            if stack.top() == '{':
                stack.pop()
        if char == ']':
            if stack.top() == '[':
                stack.pop()

    if stack.is_empty():
        return True
    else:
        return False


given_expression = "[(5+x)-(y+z)]"
valid_expression = "({[]})"
invalid_expression = "([{]})"
no_opening_paren = "]()]"

print(expression_checker(given_expression))
print(expression_checker(valid_expression))
print(expression_checker(invalid_expression))
print(expression_checker(no_opening_paren))

end_time = time.time()

print("Time to calculate: ", end_time - start_time, "seconds")



