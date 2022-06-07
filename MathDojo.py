class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        
        self.result=self.result+num
        if len(nums) >0:
            for x in nums:
                self.result +=x
        return self
    def subtract(self, num, *nums):
        self.num=num
        # your code here
        self.result=self.result-num
        if len(nums) >0:
            for x in nums:
                self.result -=x
        return self
        


# create an instance:
md = MathDojo()
gg = MathDojo()
# to test:

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)
# should print 5
y=gg.add(2).add(2,5,1).subtract(1,2,3).result
print(y)