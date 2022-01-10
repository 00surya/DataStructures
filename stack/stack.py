class Stack:

    def __init__(self,l):
        self.stack = []
        self.length = l
        self.elements = 0

    def arr_length(self):
        return len(self.stack)

    def is_full(self):
        if self.arr_length() == self.length:
            return True    
        else:
            return False    

    def push(self,element):
        if self.arr_length() <self.length:
            self.elements+=1
            self.stack.append(element)
            return self.stack
        else:
            return "overflow :/"

    def pop(self):
        if self.length==0 or self.elements==0:
            return "underflow :/"
        else:
            self.elements -=1
            return self.stack.pop()




if __name__ == "__main__":

    s = Stack(4)
