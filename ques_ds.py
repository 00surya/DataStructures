class myqueue:
    
    def __init__(self):
        self.data = []
        
    def length(self):
        return len(self.data)
    
    def enque(self, element): # put the element in the queue
        if len(self.data) < 5:
            self.data.append(element)
            return self.data
        else:
            return "overflow"
        
    def deque(self): # remove the first element that we have put in queue
        if len(self.data) == 0:
             return "underflow"
        else:
            return self.data.pop(0)
            
b = myqueue()
b.enque(2) # put the element into the queue
b.enque(3)
b.enque(4)
b.enque(5)
# print(b.data)
# b.deque()# # remove the first element that we have put in the queue
print(b.enque(2))
print(b.enque(2))

print(b.deque())
print(b.deque())
print(b.deque())
print(b.deque())
print(b.deque())
print(b.deque())

print(b.enque(5))