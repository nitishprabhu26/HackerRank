if __name__ == '__main__':
    N = int(input())
    myList=[]
    
    # https://www.geeksforgeeks.org/taking-input-in-python/
    # https://www.w3schools.com/python/ref_string_strip.asp
    # https://www.w3schools.com/python/ref_string_split.asp
    
    for i in range(N):
        val = input().strip().split()
        if val[0] == 'insert':
            myList.insert(int(val[1]),int(val[2]))
        elif val[0] == 'print':
            print(myList)
        elif val[0] == 'remove':
            myList.remove(int(val[1]))
        elif val[0] == 'append':
            myList.append(int(val[1]))
        elif val[0] == 'sort':
            myList.sort()
        elif val[0] == 'pop':
            myList.pop()
        elif val[0] == 'reverse':
            myList.reverse()
            
   
if __name__ == '__main__':
    # https://www.w3schools.com/python/ref_func_getattr.asp
    N = int(input())
    L = []
    for t in range(N):
        args = input().strip().split(" ")
        if args[0] == "print":
            print(L)
        elif len(args) == 3:
            getattr(L, args[0])(int(args[1]), int(args[2]))
        elif len(args) == 2:
            getattr(L, args[0])(int(args[1]))
        else:
            getattr(L, args[0])()

