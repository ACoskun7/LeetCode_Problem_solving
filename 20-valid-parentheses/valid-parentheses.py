class Solution:
    def isValid(self, s: str) -> bool:
     
        if len(s) %2 != 0:
            return False
        else:
            my_stack=[]
            for i in s:
                if i=='(':
                    my_stack.append(1)
                elif i == '{':
                    my_stack.append(2)
                elif i =='[':
                    my_stack.append(3)

                else:
                    if not my_stack:
                        return False
                    elif i==')':
                        if  my_stack[-1] == 1:
                            my_stack.pop(-1)
                        else:
                            return False
                        
                    elif i == '}':
                        if my_stack[-1] == 2:
                            my_stack.pop(-1)
                        else:
                            return False
                            
                    elif i ==']':
                        if my_stack[-1] == 3:
                            my_stack.pop(-1)
                        else:
                            return False
                   
            if  not my_stack:
                return True
            else :
                return False
                             
                  

                
            
           

