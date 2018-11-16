# import needed to open web page
import webbrowser

# create a class
class Movie():
    """This class provies a way to store movie related information
	
	Attributes: 
		movie_title(string): Title of movie
		movie_storyline(string): Brief Description of the movie's plot
		poster_image(string): Official movie cover poster
		trailer(string): Video trailer of movie		
		
	"""

    # The following 2 lines of code are not in use--only kept for reference 
    '''create a CONSTANT class variable all caps
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]'''

    # define and initialize class variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    # open youtube movie trailer when user clicks on poster_image
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)