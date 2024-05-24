class MovieInfoObj:
    
    id = ''
    currMovieTitle = ''
    title = ''
    year = ''
    originalTitle = ''
    imdbId = ''
    coverURL = ''
    rating = ''
    votes = ''
    kind = ''
    runtime = ''
    plotOutline = ''
    plot = []
    cast = []
    genres = []
    keyWords = []


    def __init__(self, movie, currMovieTitle) -> None:
        self.id = movie.movieID
        self.currMovieTitle  = currMovieTitle
        self.id              = movie.movieID
        self.title           = movie.get('title')
        self.year            = movie.get('year')
        self.originalTitle   = movie.get('original title')
        self.imdbId          = movie.get('imdbID')
        self.coverURL        = movie.get('cover url')
        self.rating          = movie.get('rating')
        self.votes           = movie.get('votes')
        self.kind            = movie.get('kind')
        self.runtime         = movie.get('runtime')
        self.plotOutline     = movie.get('plot outline')
        self.plot            = movie.get('plot')
        self.cast            = movie.get('cast')
        self.genres          = movie.get('genres')
        self.keyWords        = movie.get('keywords')
