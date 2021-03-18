if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    #sorted function which accepts an iterable and return a sorted list 
    # and then reassign the result to the original name (is recommended):

    a = sorted(arr)
    
    # new_list is a set of a
    new_list = set(a) 

  
    # removing the largest element from temp list 
    new_list.remove(max(new_list)) 
    
    # elements in original list are not changed 
    # print(list1) 
    
    print(max(new_list)) 