class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        ans = []                                            
        dict1 = {}                                          
        supplies = set(supplies)                  
        for i in range(len(recipes)):
            dict1[recipes[i]] = ingredients[i] 
        while True:                                       
            temp = []                                    
            for i in range(len(recipes)):        
                flag = True                            
                for j in range(len(dict1[recipes[i]])):          
                    if dict1[recipes[i]][j] not in supplies:     
                        flag = False                                     
                        temp.append(recipes[i])                  
                        break                                                  
                if flag:                                                         
                    ans.append(recipes[i])                            
                    supplies.add(recipes[i])       
            if temp == recipes:                                        
                break
            else:
                recipes = temp                                           
        return ans