class queue:
    
    def __init__(self,size):

        self.q  = []
        self.size = size
        self.r = -1
        self.f = -1
        

    def enq(self,item):

        #base case
        if self.r==self.f-1 or (self.r==self.size-1 and self.f==0):
            return "overflow"
        if self.f==-1:
            self.f = 0
            self.r = 0
        elif self.r==self.size-1:
            self.r = 0
        else:
            self.r+=1
        print(self.f,self.r)
        self.q.append(item)
    
        return self.q
    
    def denq(self):
        
        #base case
        if self.r==-1:
            return "underflow"

        if self.f == self.r:
            self.f = -1
            self.r = -1

        elif self.f==self.size-1:
            print("he")
            self.f = 0
        else:
            self.f +=1
        item = self.q.pop(0)
        return item

q = queue(4)

print(q.enq(1))
print(q.enq(2))
print(q.enq(3))
print(q.enq(4))

print(q.denq())
print(q.enq(40))
print(q.denq())
print(q.enq(50))
print(q.denq())
print(q.enq(500))
print(q.denq())
print(q.enq(500))