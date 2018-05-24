import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,year_released, director, writer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year_released = year_released
        self.director = director # MODIFY this in fresh_tomatoes!
        self.screenwriter = writer # MODIFY this in fresh_tomatoes!
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)