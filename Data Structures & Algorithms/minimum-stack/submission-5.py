class MinStack:

    def __init__(self):
        self.l =[]
        self.minn=0
        
        

    def push(self, val: int) -> None:
        self.l.append(val)
        if(len(self.l)==1):
            self.minn = val
        if(self.minn>val):
            self.minn = val
        

    def pop(self) -> None:
        if self.l[-1]==self.minn:
            self.l.pop()
            if self.l :
                self.minn = min(self.l)
            
        else:
            self.l.pop()



        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return self.minn
        
