import re
import time
from imdb import Cinemagoer
from movieInfoList import MovieInfoList
from movieInfoObj import MovieInfoObj

class IMDBInfo:
  
  moviedb = Cinemagoer()
  searchedTitles = []
  matchedMovies = []
  movie_arry = MovieInfoList()
  currMovieTitle = ''

  def __init__(self):
    pass

  def setCurrMovieTitle(self, _currMovieTitle):
     self.currMovieTitle = _currMovieTitle
    #Search Title 
  def searchTitle(self, _title):
      try:
        self.searchedTitles = self.moviedb.search_movie(_title)
      except:
         print('Error')
         pass

  
  def matchMovies(self) -> []:
     for searched in self.searchedTitles:
        time.sleep(5)
        if(re.sub('[^A-Za-z0-9]+', '', self.currMovieTitle.lower()) == re.sub('[^A-Za-z0-9]+', '', searched.get('title').lower()) and searched.get('kind') == 'movie'):
              try:
                print('Match Found')
                time.sleep(5)
                movie = self.moviedb.get_movie(searched.movieID)
                self.moviedb.update(movie, info=['keywords'])
                matchedMovie = MovieInfoObj(movie , self.currMovieTitle)
                self.matchedMovies.append(matchedMovie)
                self.movie_arry.appendToList(matchedMovie)
              except:
                print('Error')
                pass

  def searchMovieList(self, _movieList):
    count = 0
    for movie in _movieList:
      count += 1
      print(str(count) + ': searching imdb for ' + movie)
      self.setCurrMovieTitle(movie)
      self.searchTitle(movie)
      self.matchMovies()

  def getMatchedMovies(self) -> list[MovieInfoObj]:
     return self.matchedMovies
  
  def getMovieList(self) -> MovieInfoList:
     return self.movie_arry


     