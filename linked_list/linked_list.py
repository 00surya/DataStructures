# Simple Linked->List

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList1:

    '''    
        - inserting element with the time complexity of O(n).
        - Deletion of node with the time complexity of O(1)
        - traversing with the time complexity O(n)

    '''
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print("")
    def push(self,data):

        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node

        else:
            last = self.head
            while last.next:
                last = last.next

            last.next = new_node

    def pop(self):

        if self.head==None:
            return None
        else:
            del_val = self.head
            self.head = self.head.next

            return del_val.data


    def traverse(self,data):

        last = self.head
                
        while last.next:
            if last.data==data:
                break
            last = last.next

        if last.data!=data:
            # print(False)
            return False
        else:
            # print(True)
            return True

# Simple Linked List - deletion in O(1) insertion O(1)

class LinkedList2(LinkedList1):

    '''    
        - inserting element with the time complexity of O(1).
        - Deletion of node with the time complexity of O(1)
        - traversing with the time complexity O(n)

    '''
    
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):

        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            
        else:
            self.tail.next = new_node
            self.tail = new_node


import time

if __name__ == "__main__":


    start = time.time()
    l_list1 = LinkedList1()
    for i in range(10000):
        l_list1.push(i)
    time.sleep(1)
    end = time.time()
    print(f"Time taken at insertion of elements in O(n) {end - start}")
    

    l_list2 = LinkedList2()
    start = time.time()
    for i in range(10000):
        l_list2.push(i)
    time.sleep(1)
    end = time.time()
    print(f"Time taken at insertion of elements in O(1) {end - start}")




