class Music:
    def __init__(self, title, lyrics):
        self.title = title
        self.lyrics = lyrics
        
    # Método para comparação de igualdade
    def __eq__(self, other):
        if isinstance(other, Music):
            return self.title == other.title and self.lyrics == other.lyrics
        return False