"""problem link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # it represents first item of Queue unlike in simple queues which represented before first
        self.rear = self.head # it represents last item of queue like simple queues

    def isempty(self):
        return self.head is None

    def enqueue(self, data):
        if self.isempty():
            self.head = Node(data)
            self.rear = self.head
        else:
            newNode = Node(data)
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):

        if self.isempty():
            print("Queue is empty")
            return None

        temp = self.head
        self.head = self.head.next

        if self.head is None:
            # if queue emptied, rear has to point to nothing
            self.rear = None

        return temp.data

    def __len__(self):
        temp = self.head
        counter = 0
        while temp is not None:
            temp = temp.next
            counter += 1
        return counter

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.data)
            temp = temp.next
            if temp is not None:
                result += ', '
        return result
    

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            return
        else:
            t = self.top
            self.top = Node(data)
            self.top.next = t
    
    def pop(self):
        if self.top is None:
            print("stack underflow")
            return
        t = self.top
        self.top = self.top.next
        return t.data







class Solution:
    def countStudents(self, students: Queue, sandwiches: Stack) -> int:
        counter = 0
        n = len(students)
        while n > 0 and n >= counter:
            sandwich = sandwiches.pop()
            stud = students.dequeue()
            if sandwich == stud:
                n = len(students)
                counter = 0
            else:
                students.enqueue(stud)
                sandwiches.push(sandwich)
                counter += 1
        return n
    

# class Solution:
#     def countStudents(self, students: list, sandwiches: list) -> int:
#         counter = 0
#         n = len(students)
#         while n > 0 and n >= counter:
#             sandwich = sandwiches.pop(0)
#             stud = students.pop(0)
#             if sandwich == stud:
#                 n = len(students)
#                 counter = 0
#             else:
#                 students.append(stud)
#                 sandwiches.insert(0, sandwich)
#                 counter += 1
#         return n
  


if __name__ == "__main__":
    st = [1,1,1,0,0,1]
    s = [1,0,0,0,1,1]
    sandwiches = Stack()
    students = Queue()
    for i in s[: :-1]:
        sandwiches.push(i)

    for j in st:
        students.enqueue(j)
    
    Sol = Solution()
    print(Sol.countStudents(students, sandwiches))
    
    