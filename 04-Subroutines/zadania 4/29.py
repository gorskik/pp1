tab=[2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]

tab.sort()
for x in tab:
    int(x)
def mediana(tab):
    d=len(tab)
    if d%2==0:
        return(tab[d//2-1]+tab[d//2])/2
    else:
        return tab[len(tab)//2]
    
def dominanta(tab):
    l=[]
    for x in tab:
        l.append(0)
    for x in range(0,len(tab)-1):    
        if tab[x+1]==tab[x]:
            l[tab[x]]+=1
    j=l[0]
    for i in range(0,len(l)-1):
        if l[i+1]>j:
            j=l[i+1]
            k=i+1
    return k
              
print(f'Mediana: {mediana(tab)}')
print(f'Dominanta: {dominanta(tab)}')
