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

            else:
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

    def LvlOrdTr(self):
        print("Level Order Traversal")
        root = self.root
        tree = True
        first_elem = True
        elem_list = []
        queue = queu()
        while tree:
            if first_elem:
                queue.enq(root)
                first_elem = False
            else:        
                deque_root = queue.deq()
                if deque_root != "underflow":
                    elem_list.append(deque_root.node)
                    left_child = deque_root.left
                    right_child = deque_root.right
                    if left_child !=None:
                        queue.enq(left_child)
                    if right_child != None:
                        queue.enq(right_child)   
                else:
                    tree = False

        self.print_slowly(elem_list)
        return elem_list

    def InOrdTr(self):
        print("Inorder Traversal (Left <-> Root <-> Right)")
        elem_list = []
        def traverse(root = self.root):
            if root:
                traverse(root.left)
                # print(root.node,end=" ")
                elem_list.append(root.node)
                traverse(root.right)

        traverse(self.root)
        self.print_slowly(elem_list)

        return elem_list
    
    def PreOrdTr(self):
        print("PreOrder Traversal (Root <-> Left <-> Right)")
        elem_list = []
        def traverse(root = self.root):
            if root:
                # print(root.node,end=" ")
                elem_list.append(root.node)
                traverse(root.left)
                traverse(root.right)

        traverse(self.root)
        self.print_slowly(elem_list)

        return elem_list
    
    def print_slowly(self,lst):
        last = lst[-1]
        for i in range(len(lst)-1):
            print(lst[i],end=" -> ")
            sys.stdout.flush()
            time.sleep(.5)
        print(last)

        return 

        


if __name__ == "__main__":

        elem_to_pus = [50,10,30,5,300,15]
        bst = BinaryTree(elem_to_pus[0])
        for idx in range(1,len(elem_to_pus)):
            bst.push(idx)

        bst.LvlOrdTr() # level-order traversing
        bst.InOrdTr()  # in-order traversing
        bst.PreOrdTr() # pre-order traversing























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
