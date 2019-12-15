class Music():
    def __init__(self, title, author, album, year):
        self.author=author
        self.title=title
        self.album=album
        self.year=year
    def __str__(self):
        return f'''
        Author: {self.author}
        Title: {self.title}
        Album: {self.album}
        Year: {self.year}
                '''

song = Music('Interlude', 'Chopin', 'C-dur', '1678')
song2=Music('costam', 'idk', 'nwm', '2019')
song3 = Music('asasa','sasa','as','1989')
print(song,song2,song3)