import re

ile = 0

tekst = 'To be, or not to be, that is the question '
samogloski = re.findall('a|e|i|o|u', tekst)
for samogloska in samogloski:
    ile += 1
    
print (ile)

