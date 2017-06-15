class BinarySearch(list):
    def __init__(self,a,b):
    
        self.a = a # a is length of ist to be created
        self.b = b # b is the step between consequtive numbers
        self.li = [i for i in range(b,a+1)]
        self.length = len(self.li)
    def search(self,item):
        self.count =0
        self.index = 0
        self.first = 0
        self.last = len(li)-1
        self.found = False

        while self.first <= self.last and not found:
            self.count+=1
            midpoint = (self.first + self.last)//2
            if li[midpoint] == self.item:
                self.found = True
            else:
                if item < self.li[midpoint]:
                    self.last = midpoint-1
                else:
                    self.first = midpoint+1
        return dict([(self.count,self.li.index(found))])



