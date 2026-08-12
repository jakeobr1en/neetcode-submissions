class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []


    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            if val <= self.mins[-1]:
                self.mins.append(val) 

    def pop(self) -> None:
        if self.mins[-1] == self.values[-1]:
            self.mins.pop()
        self.values.pop()
        

    def top(self) -> int:
        return self.values[-1] if self.values else None

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else None
