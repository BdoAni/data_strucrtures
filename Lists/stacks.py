#  Pop elements from the stack  (LIFO) (Last-in, First-out)
# The list methods make it very easy to use a list as a stack, 
# where the last element added is the first element retrieved (“last-in, first-out”). 
# To add an item to the top of the stack, use append(). To retrieve an 
# item from the top of the stack, use pop() without an explicit index. For example:

# Create an empty stack
stack = []
# Push elements onto the stack
stack.append("apple")
stack.append("banana")
stack.append("cherry")
print(stack)  # Output: ['apple', 'banana', 'cherry']

# Pop elements from the stack (Last-in, First-out)
popped_element = stack.pop()
print(popped_element)  # Output: cherry

print(stack)  # Output: ['apple', 'banana']

# Peek at the top element of the stack without removing it
top_element = stack[-1]
print(top_element)  # Output: bananastack=[]

#  Valid parentheses 
def is_balanced_parentheses(input_string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # Closing bracket with no corresponding opening bracket
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False  # Mismatched opening and closing brackets
    
    return len(stack) == 0  # True if all brackets are matched and stack is empty

# Example usage:
print(is_balanced_parentheses("()"))  # Output: True
print(is_balanced_parentheses("()[]{}"))  # Output: True
print(is_balanced_parentheses("([)]"))  # Output: False
print(is_balanced_parentheses("(]"))  # Output: False