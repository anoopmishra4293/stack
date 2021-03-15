class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None


    def push(self,val):
        n = Node(val)
        
        if not self.head:
            self.head = n
        else:
            n.next = self.head
            self.head = n
    

    def pop(self):
        if not self.head:
            return None
        if self.head:
            a = self.head
            self.head = self.head.next
            x=a.val
            del a
            return x

    
    def top(self):
        if not self.head:
            return None
        if self.head:
            return self.head.val


s1 = Stack()
s1.push(4)
s1.push(5)
print(s1)
print(s1.pop())
s1.push(6)
print(s1.pop())
print(s1.pop())
