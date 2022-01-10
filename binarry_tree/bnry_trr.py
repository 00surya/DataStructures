class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
    
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)



tree = BinaryTree('a')
print(tree.value)
print(tree.left_child)
print(tree.right_child)


a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child
print(a_node.value) # a
print(b_node.value) # b
print(c_node.value) # c 
print(d_node.value) # d
print(e_node.value) # e
print(f_node.value) # f

###### Insering No in tree structure :) ######

one_node  = BinaryTree(1)
one_node.insert_left(2)
one_node.insert_right(5)

two_node = one_node.left_child
two_node.insert_left(3)
two_node.insert_right(4)

five_node = one_node.right_child
five_node.insert_left(6)
five_node.insert_right(7)

#            1
#          /   \
#        2       5
#      /   \   /   \
#     3     4 6     7

#############################################




# Dfs Tree Traversal Algorithm **********************************

# three types Pre-oreder, In-order, post-order

###In-order

def InOrd(root):
    if root:
        InOrd(root.left_child)
        print(f"In-Order > {root.value}")
        InOrd(root.right_child)


## This is how recursive function working here ######

# def InOrd(1):
#     if root:
#         InOrd(2)
#         def InOrd(3):
#             if root:
#                 InOrd(None)
#                 3
#                 2
#                 def InOrd(4):
#                     if root:
#                         InOrd(None)
#                         def InOrd(None):
#                             4
#                             1
#                             def InOrd(5):
#                                 if root:
#                                     InOrd(6)
#                                         InOrd(None):
#                                             6
#                                                 InOrd(None):
#                                                     5
#                                                     InOrd(7):
#                                                         InOrd(None):
#                                                             7
#                                                             InOrd(None)
                                                                                                
#####################################################################################3                                                       

## In-order function call

# InOrd(a_node)
# print("\n")
InOrd(one_node)

### In-order ends ####

###Pre-order

print("\n")


def PreOrd(root):
    if root:
        print(f"Pre-order> {root.value}")
        PreOrd(root.left_child)
        PreOrd(root.right_child)
PreOrd(one_node)

# preordr other algo -- :>
# def PreOr(root):
    # if root:
        # print(f"dfs > {root.value}")
        # if root.left_child:
            # PreOr(root.left_child)

        # if root.right_child:   
            # PreOr(root.right_child)
# PreOr(one_node)

###Post-order

print("\n")

def PostOrd(root):
    if root:
        PostOrd(root.left_child)
        PostOrd(root.right_child)
        print(f"Post-order{root.value}")
PostOrd(one_node)


# Bfs Tree Traversal Algorithm **********************************

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')

print("\n")


vstd = []
o = 1
def bfs(node):
    global o
    vstd.append(node.value)
    s = vstd.pop(0)
    print(s, end=" ")

    if o==1:
        o=1-1
        bfs(node.left_child)
        bfs(node.right_child)
        o+=1    
    
bfs(one_node)
