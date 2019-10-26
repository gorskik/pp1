tab = [15, 8, 31, 47, 2, 19]
elementy = 0
l_el = 0
for i in tab:
    if i%2!=0:
        elementy = elementy + i
        l_el=l_el + 1
        
print(elementy/l_el)
                
