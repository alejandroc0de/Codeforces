lista = [True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False]

def getIndex():
    l = 0 
    r = len(lista)-1
    while l<=r:
        m = (l+r)//2
        if(lista[m]==False and lista[m-1]==True):
            return m
        elif(lista[m]==False):
            r = m-1
        else:
            l = m+1
    return -1



print(getIndex())