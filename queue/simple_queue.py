class queue:
    
    def __init__(self,size):

        self.q  = []
        self.size = size
        self.r = -1
        self.f = -1
        

    def enq(self,item):

        #base case
        if self.r==self.size-1:
            return "overflow"

        if self.r==-1:
            self.f = 0
            self.r = 0
        else:
            self.r+=1
        self.q.append(item)
        return self.q
    
    def denq(self):
        #base case
        if self.f==-1:
            return "underflow"
        if self.f == self.size-1:
            self.f = -1
        else:
            self.f+=1    
        item = self.q.pop(0)
        # self.f+=1
        return item
        

q = queue(3)
print(q.enq(1))
print(q.enq(2))
print(q.enq(3))

# print(q.enq(4))

print(q.denq())
print(q.denq())
print(q.denq())

# Problem
print(q.denq()) # underflow
print(q.enq(5)) # still showing overflow

# Check - Empty queue
print(q.q)