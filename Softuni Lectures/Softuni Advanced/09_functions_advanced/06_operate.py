from functools import reduce

# mapper = {
#     "+": lambda nums: reduce(lambda x, y: x+y, nums),
#     "-": lambda nums: reduce(lambda x, y: x-y, nums),
#     "*": lambda nums: reduce(lambda x, y: x*y, nums),
#     "/": lambda nums: reduce(lambda x, y: x/y, nums)
# }

def operate(operator, *args):
    
    if operator == "+":
        return reduce(lambda x, y: x+y, args)

    elif operator == "-":
        return reduce(lambda x, y: x-y, args)
        
    elif operator == "*":
        return reduce(lambda x, y: x*y, args)
    
    elif operator == "/":
        return reduce(lambda x, y: x/y, args)

print(operate("+", 1, 2, 3))