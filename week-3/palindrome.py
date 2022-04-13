class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue:
    # A doubly-linked list.
    def __init__(self):
        self.items = []
        

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.insert(0, data) 

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items [-1]

    def size(self):
        return len(self.items) 

class Stack:
    # A doubly-linked list.
    def __init__(self):
       self.top = None
       self.length = 0

    def isEmpty(self):
        return self.length == 0

    def push(self, data):
        newNode = Node(data)
        if self.length >= 1:
            newNode.next =self.top
            self.top = newNode
        else:
            self.top = newNode
        self.length += 1 

    def pop(self):
        look = self.top.data
        if self.length > 1:
            self.top = self.top.next
        else: 
            self.top = None
        self.length -= 1
        return look
      

    def peek(self):
        return self.top.data

    def size(self):
        return self.length  

def isPalindrome(str):
    strStack = Stack()
    strQueue = Queue()
    strQueue.enqueue(str)
    # store the str in a stack and in a queue
    # for element in str:
    #     strStack.push(element)
    #     strQueue.enqueue(element)
    letters = list(strQueue.items[0])
    letters.reverse()
    strStack.push(letters)
    turnArround = strStack.top.data
    #loop through the stack and queue, removing one element at a time
    # and checking to see if they are equal.
     
    # Only need to loop through half of the string as we are checking the first and last elements
    # of the string and then moving inward towards the middle.
    # for i in range(int(len(str)/2)):
    #     if (strStack.pop() != strQueue.dequeue()):
    #         return False
    # return True      
    regular = list(strQueue.items[0])
    if regular == turnArround:
        return True
    else:
        return False

print(isPalindrome("racecar"))        
print(isPalindrome("noon"))        
print(isPalindrome("python"))        
print(isPalindrome("madam")) 
