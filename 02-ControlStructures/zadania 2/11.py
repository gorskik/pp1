login = 'marek'
haslo = 'm-123'

login1 = input("podaj login")
haslo1 = input("podaj haslo")

print("zostales zalogowany" if login1==login and haslo1==haslo else "dane sa nieprawidlowe")