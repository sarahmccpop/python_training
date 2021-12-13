#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    #for each item in a list 
    for x in l:
        if type(x) == str:
            del x
    # if item at index is a string
    
    # delete item
    return l  
myList= [1,2,'a','b']    
print(filter_list(myList))