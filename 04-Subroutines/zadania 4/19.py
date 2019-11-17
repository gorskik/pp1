def suma(n):
    if n!=0:
        return n+suma(n-1) 
    else:
        return 0
    
print(suma(500))