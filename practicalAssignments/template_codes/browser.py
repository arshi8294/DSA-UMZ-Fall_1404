
class BrowserHistory:

    def __init__(self, homepage: str):
        """در این بخش صفحه اصلی را بسازید."""
        pass
        

    def visit(self, url: str) -> None:
        pass

        

    def back(self, steps: int) -> str:
        pass

    def forward(self, steps: int) -> str:
        pass

if __name__ == "__main__":
    pass
    ## simple test:
    # pages = ["google.com", "facebook.com", "umz.ac.ir", "maktabkhooneh.com", "Quera.org", "codewars.com"]
    # calls = [] 
    
    # for i in range(len(pages)):
    #     if i == 0:
    #         obj = BrowserHistory(pages[i])
    #     elif i == 2:
    #         calls.append(obj.back(2))  # google.com
    #         calls.append(obj.visit(pages[i]))
    #         calls.append(obj.forward(2))  # returns itself because there is no forward history => umz.ac.ir
    #     elif i == 5:
    #         calls.append(obj.back(2))
    #         calls.append(obj.forward(1))
    #     else: 
    #         calls.append(obj.visit(pages[i]))
    # calls.append(obj.back(10))


    ## check your answer
    # print(calls)  # [None, 'google.com', None, 'umz.ac.ir', None, None, 'umz.ac.ir', 'maktabkhooneh.com', 'google.com']
