class LibraryItemV2:
    def __init__(self, name, director, rating = 0, playcount = 0):
        self.name = name
        self.director = director
        self.rating = rating
        self.playcount = playcount
        
    def details(self):
        return f"{self.name} - {self.director} {self.get_stars()}"
    
    def get_stars(self):
        stars = ""
        for i in range(self.rating):
            stars +="*"
        return stars