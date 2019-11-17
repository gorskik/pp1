import random

def losowa():
    return random.randrange(1,51)

tab=[]
p=0
n=0
for x in range(1, 1001):
    a=losowa()
    if(a%2==0):
        p+=1
    else:
        n+=1
    tab.append(a)
    
print(f'Dla 1000 liczb losowych z przedziału <1,50>:\nLiczby parzyste: {round((p/len(tab))*100,2)}%\nLiczby nieparzyste: {round((n/len(tab))*100,2)}%')
