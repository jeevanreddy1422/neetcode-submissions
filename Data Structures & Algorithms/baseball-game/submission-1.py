class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        total=0
        for i in operations:
            if i=="+":
                x=stack[-1]+stack[-2]   
                stack.append(x)
                total+=x

            elif i=="C":
                total-=stack.pop()
        
            
            elif i=="D":
                peek=stack[-1]*2
                stack.append(peek)
                total+=peek
            else:
                x=int(i)
                stack.append(x)
                total+=x
        return total
        