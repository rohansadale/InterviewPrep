## Followup question of 3.3

from stack import *

class SetOfStacks:
    def __init__(self, stack_size):
        self.stacks = []
        self.max_size = stack_size
    
    def get_last_stack(self):
        if self.stacks:
            return self.stacks[-1]
        return None

    def push(self, x):
        last = self.get_last_stack()
        if last and len(last)<3:
            last.push(x)
        else:
            temp_s = Stack()
            temp_s.push(x)
            self.stacks.append(temp_s)

    def pop(self):
        last = self.get_last_stack()
        if not last:
            print "Nothing to pop. Stack is empty"
            return                
        x = last.pop()
        if len(last)==0:
            self.stacks.pop()
        return x
    
    def __str__(self):
        arr = []
        for stack in self.stacks:        
            arr.append(stack.__str__())
        return str(arr)
    
    def pop_at(self, index):
        return self.left_shift(index, True)
    
    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        if remove_top:
            x = stack.pop()
        else:
            x = stack.pop_bottom()
        if not stack:
            del(self.stacks[index])
        elif len(self.stacks) > index+1:
            val = self.left_shift(index+1, False)
            stack.push(val)
        return x


if __name__ == "__main__":
    s = SetOfStacks(3)
    for i in range(5):
        s.push(i*i)
    print "Elements in stack are ", s
    for i in range(2):
        print "Popping stack - ", s.pop()
    print "Elements in stack are ", s