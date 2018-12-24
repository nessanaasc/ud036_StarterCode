import webbrowser

#This Python file contains the structure of Movie Class
#Atributes Movie_Title, Movie_Storyline, Poster_image e Trailer_Youtube
#Method Show_Trailer

class Movie():
    """ This class provides a way to store movie related information """
   
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_year,movie_quote):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = movie_year
        self.quote = movie_quote

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
