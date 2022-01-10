import sys
import time

class queu():
    def __init__(self) -> None:
        self.arr = []

    def enq(self,elem):
        self.arr.append(elem)
        return
    def deq(self):
        try:
            return self.arr.pop(0)
        except:
            return 'underflow'



class Node:
    def __init__(self,val):
        self.node = val
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self,val):
        self.root = Node(val)
        self.l_count = 1
        self.r_count = 1
        
    def push(self,val):
        base_val = self.root
        while True:
            if val>base_val.node: #move right
                if base_val.right==None:
                    base_val.right = Node(val)
                    self.l_count+=1
                    return
                else:
                    base_val = base_val.right
                    if base_val.node==val:
                        print("Dublicate Found!")
                        return

            else:#move left
                if base_val.left==None:
                    base_val.left = Node(val)
                    self.r_count+=1                
                    return
                
                else:
                    base_val = base_val.left
                    # print(base_val.node)
                    if base_val.node==val:
                        print("Dublicate Found!")
                        return
        
    def find(self,val):

        base_val = self.root
        
        while True:
            if base_val.node!=val:
                if val>base_val.node:
                    base_val = base_val.right
                    if base_val==None:
                        print("False")
                        return False

                else:
                    base_val = base_val.left
                    if base_val==None:
                        print("False")
                        return False

            else:
                print("True")
                return True

    def lvl_o_trvs(self):
        bst = self.root
        n = True
        base = True
        q = queu()
        while n:
            if base:
                q.enq(bst)
                base = False
            else:        
                e = q.deq()
                if e!="underflow":
                    print(e.node,end=" -> ")
                    sys.stdout.flush()
                    time.sleep(.5)
                    e_left = e.left
                    e_right = e.right
                    if e_left !=None:
                        q.enq(e_left)
                    if e_right != None:
                        q.enq(e_right)
                        
                else:
                    n = False









# q = queue(3)
a = []
bst = BinaryTree(20)

bst.push(50)
bst.push(10)
bst.push(30)
bst.push(5)
bst.push(300)
bst.push(15)

# bnt.find(5)

bst.lvl_o_trvs()























# code snpts

# def lvl_o_trvs(bst):
#         n = True
#         base = True
#         q = queu()
#         while n:
#             if base:
#                 q.enq(bst.root)
#                 base = False
#             else:        
#                 e = q.deq()
#                 if e!="underflow":
#                     print(e.node,end=" -> ")
#                     sys.stdout.flush()
#                     time.sleep(.5)
#                     e_left = e.left
#                     e_right = e.right
#                     if e_left !=None:
#                         q.enq(e_left)
#                     if e_right != None:
#                         q.enq(e_right)
                        
#                 else:
#                     n = False

# lvl_o_trvs(bnt)
