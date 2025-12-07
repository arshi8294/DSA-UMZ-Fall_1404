"""problem link: https://leetcode.com/problems/design-browser-history/description/"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = Node(homepage)
        

    def visit(self, url: str) -> None:
        newpage = Node(url)
        newpage.prev = self.page
        self.page.next = newpage
        self.page = self.page.next
        print(self.page.next)

        

    def back(self, steps: int) -> str:

        for _ in range(steps):
            if self.page.prev is None:
                break
            self.page = self.page.prev
        return self.page.data

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.page.next is None:
                break
            self.page = self.page.next
        return self.page.data


if __name__ == "__main__":
    # Your BrowserHistory object will be instantiated and called as such:
    # obj = BrowserHistory('google.com')
    # obj.visit('facebook.com')
    # param_2 = obj.back(1)
    # param_3 = obj.forward(2)

    # print(param_2)
    # print(param_3)

    pages = ["google.com", "facebook.com", "umz.ac.ir", "maktabkhooneh.com", "Quera.org", "codewars.com"]
    calls = [] 
    
    for i in range(len(pages)):
        if i == 0:
            obj = BrowserHistory(pages[i])
        elif i == 2:
            calls.append(obj.back(2))  # google.com
            calls.append(obj.visit(pages[i]))
            calls.append(obj.forward(2))  # returns itself because there is no forward history => umz.ac.ir
        elif i == 5:
            calls.append(obj.back(2))
            calls.append(obj.forward(1))
        else: 
            calls.append(obj.visit(pages[i]))
    calls.append(obj.back(10))



    print(calls)  # [None, 'google.com', None, 'umz.ac.ir', None, None, 'umz.ac.ir', 'maktabkhooneh.com', 'google.com']