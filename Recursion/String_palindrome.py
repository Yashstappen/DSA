str = "nitia"
left = 0
right = len(str)-1

def palin(string, l, r):
    if(l>=r):
        return True
    
    if(string[l]!=string[r]):
        return False
    
    return palin(string, l+1, r-1)

def test(str, left, right):
    return palin(str, left, right)
    

print(test(str,left,right))