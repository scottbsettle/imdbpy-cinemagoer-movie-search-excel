import pandas as pd

from movieInfoList import MovieInfoList


class ExcelReader:
    filePath = ''
    outputPath = ''
    dataFrame = pd.DataFrame()
    columnValues = []
    exportdf = pd.DataFrame()

    def __init__(self, _inputPath = '', _outputPath = '') -> None:
        self.filePath = _inputPath
        self.outputPath = _outputPath

    def setDataFrame(self, _fileName) -> None:
        try:
            self.dataFrame = pd.read_excel(self.filePath + _fileName)
        except:
            print('Error')
            pass
    
    def setColumnValues(self, _columnName) -> None:
        try:
            self.columnValues = self.dataFrame[_columnName].values
        except:
            print('Error')
            pass

    def exportExcel(self, _movie_arry: MovieInfoList, _outputPath = 'Output.xlsx') -> None:
        self.generateExportdf(_movie_arry)
        self.exportdf.to_excel(self.outputPath + _outputPath)
    
    def getColumnValue(self) -> list[str]:
        return self.columnValues
    
    def generateExportdf(self, _movie_arry: MovieInfoList):
        self.exportdf = pd.DataFrame()
        self.exportdf.insert(0  , 'Id' , _movie_arry.id_arry)
        self.exportdf.insert(1  , 'currMovieTitle' , _movie_arry.currMovieTitle_arry)
        self.exportdf.insert(2  , 'Title' , _movie_arry.title_arry)
        self.exportdf.insert(3  , 'Year' , _movie_arry.year_arry)
        self.exportdf.insert(4  , 'Original_Title' , _movie_arry.originalTitle_arry)
        self.exportdf.insert(5  , 'imdbId' , _movie_arry.imdbId_arry)
        self.exportdf.insert(6  , 'Cover_Url' , _movie_arry.coverURL_arry)
        self.exportdf.insert(7  , 'Rating' , _movie_arry.rating_arry)
        self.exportdf.insert(8  , 'Votes' , _movie_arry.votes_arry)
        self.exportdf.insert(9  , 'Kind' , _movie_arry.kind_arry)
        self.exportdf.insert(10 , 'Runtime' , _movie_arry.runtime_arry)
        self.exportdf.insert(11 , 'Plot_Outline' , _movie_arry.plotOutline_arry)
        self.exportdf.insert(12 , 'Plot' , _movie_arry.plot_arry)
        self.exportdf.insert(13 , 'Cast' , _movie_arry.cast_arry)
        self.exportdf.insert(14 , 'Genres' , _movie_arry.genres_arry)
        self.exportdf.insert(15 , 'Keywords' , _movie_arry.keyWords_arry)