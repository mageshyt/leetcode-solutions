def romanToInt( s: str) -> int:
    letters = list(s) # this will split the string in to list for example : s="ABC" list(s) will return ["A","B","C"]  
    
    romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    total = 0
    
    previous_value = None
    
    for i in letters:
        if previous_value is not None and romans[previous_value] <  romans[i]:
            # if previous was not none and previous value is less than the next value then minus 2*previous value to the current value and add to the total
            total+=(romans[i]-(romans[previous_value]*2))
        else:
            # if previous value is none and previous value is greater than the next value then add the value to total
            total+=romans[i]
        print({'previous_value':previous_value,'total':total})
        previous_value = i
    return total
    

    

print(romanToInt('VL'))
