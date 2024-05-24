from movieInfoObj import MovieInfoObj

class MovieInfoList:

    id_arry = []
    currMovieTitle_arry = []
    title_arry = []
    year_arry = []
    originalTitle_arry = []
    imdbId_arry = []
    coverURL_arry = []
    rating_arry = []
    votes_arry = []
    kind_arry = []
    runtime_arry = []
    plotOutline_arry = []
    plot_arry = []
    cast_arry = []
    genres_arry = []
    keyWords_arry = []

    def __init__(self) -> None:
        pass

    def appendToList(self, _movie: MovieInfoObj):
        self.id_arry.append(_movie.id)
        self.currMovieTitle_arry.append(_movie.currMovieTitle)
        self.title_arry.append(_movie.title)
        self.year_arry.append(_movie.year)
        self.originalTitle_arry.append(_movie.originalTitle)
        self.imdbId_arry.append(_movie.imdbId)
        self.coverURL_arry.append(_movie.coverURL)
        self.rating_arry.append(_movie.rating)
        self.votes_arry.append(_movie.votes)
        self.kind_arry.append(_movie.kind)
        self.runtime_arry.append(_movie.runtime[0] if _movie.runtime != None else '')
        self.plotOutline_arry.append(_movie.plotOutline)
        self.plot_arry.append(_movie.plot[0] if _movie.plot != None else '')
        self.cast_arry.append(_movie.cast)
        self.genres_arry.append(_movie.genres)
        self.keyWords_arry.append(_movie.keyWords)