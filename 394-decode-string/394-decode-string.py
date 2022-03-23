class Solution(object):
    def decodeString(self, s):
        num = 0
        string = ''
        list = []
        
        for i in s:
            if i.isalpha(): #i > alphabet or number
                string += i
                
            elif i.isdigit():
                num = num*10 + int(i)
            
            elif i == '[':
                list.append(string) 
                list.append(num)
                string = ''
                num = 0
            
            elif i == ']':
                # a * 3 = aaa
                num_list = list.pop()
                string_list = list.pop()
                string = string_list + num_list * string
                
        return string