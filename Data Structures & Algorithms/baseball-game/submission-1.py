class Solution:
    

    def is_int(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False
    
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0

        if len(operations) == 0:
            return
        
        for op in operations:
            if self.is_int(op):
                stack.append(int(op))
            elif op == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num1 + num2
                stack.append(num2)
                stack.append(num1)
                stack.append(num3)
                
            elif op == "C":
                p = stack.pop()
                
            elif op == "D":
                num = stack.pop()
                num1 = num * 2
                stack.append(num)
                stack.append(num1)
                
        
        if len(stack) > 0:
            for num in stack:
                result += num
        
        return result

        