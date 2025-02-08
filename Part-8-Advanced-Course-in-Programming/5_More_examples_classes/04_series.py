# Write your solution here:
class Series:
    def __init__(self, title: str, season: int, genre: list):
        self.title = title
        self.season = season
        self.genre = genre
        self.rating = -1
        self.count = 0

    def rate(self, rating: int):
        if self.rating < 0:
            self.rating =  self.rating + 1 + rating
        else:
            self.rating += rating
        self.count += 1


    def __str__(self):
        if self.rating < 0:
            return f"{self.title} ({self.season} seasons)\ngenres: {", ".join(self.genre)}\nno ratings"
        else:
            return f"{self.title} ({self.season} seasons)\ngenres: {", ".join(self.genre)}\n{self.count} ratings, average {self.rating/self.count:.1f} points"

def minimum_grade(rating:float, series_list: list):
    series = []
    for serie in series_list:
        if serie.rating > rating:
            series.append(serie)
    
    return series

def includes_genre(genre: str, series_list: list):
    series = []
    for serie in series_list:
        if genre in serie.genre:
            series.append(serie)
    
    return series

if __name__=="__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]
    print("a minimum grade of 4.5:")
    
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
