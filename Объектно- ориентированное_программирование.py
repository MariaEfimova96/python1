# stack = []
# def push(val):
#     stack.append(val)
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
# push(3)
# push(2)
# push(1)
# print(pop())
# print(pop())
# print(pop())
class Stack:
    def __init__(self):
        self.__stackList = []
def push(self, val):
    self.__stackList.append(val)
def pop(self):
    val = self.__stackList[-1]
    del self.__stackList[-1]
    return val
stackObject = Stack()

stackObject.push(3)
stackObject.push(2)
stackObject.push(1)

print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())