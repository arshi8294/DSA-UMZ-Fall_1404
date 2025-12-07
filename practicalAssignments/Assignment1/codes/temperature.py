"""problem Link: https://leetcode.com/problems/daily-temperatures/description/"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def __str__(self):
        curr = self.top
        lst = []
        while curr is not None:
            lst.append(curr.data)
            curr = curr.next
        return '\n'.join([str(i) for i in reversed(lst)]) + "\n--------------"


class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = Stack()
        stack.push(0)
        for i in range(1, len(temperatures)):
            # print(stack)
            top = stack.top
            while top and temperatures[top.data] < temperatures[i]:
                j = stack.pop()
                result[j] = i - j
                top = stack.top
            stack.push(i)
        # print(result)
        return result


if __name__ == "__main__":
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    res = sol.dailyTemperatures(temperatures=temperatures)
    print(res)
