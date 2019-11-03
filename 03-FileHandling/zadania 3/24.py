
tab = [['Marek', 'Zelnik', 'zelnik@sed.pl'], [
    'Ewa', 'Maj', 'maje@wp.pl'], ['Piotr', 'Wyga', 'wygap@gop.pl']]
with open('data.csv', 'w') as file:
    file.write('Imie, Nazwisko, Email\n')
    for i in range(len(tab)): #1st tab dimension
        for j in range(len(tab[i])): #2nd tab dimension
            napis = ','.join(tab[j])
            file.write(f'{napis}\n')