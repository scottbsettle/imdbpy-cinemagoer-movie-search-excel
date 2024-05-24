from excelReader import ExcelReader
from imdbInfo import IMDBInfo

#set excel file read from
excelReadPath = 'C:/Users/scott/Documents/Development/Data Files/'
excelReadFileName = 'imdbDataNewMoviesFiltered - Copy.xlsx'
excelReadColumn = 'CleanTitle'

#Set the excel out put
excelOutputPath = ''
excelOutputFileName = 'Output.xlsx'

#Create Excel Reader Obj
excelReaderObj = ExcelReader(excelReadPath)

#Set the dataframe from excel obj to read from
excelReaderObj.setDataFrame(excelReadFileName)

#Set the columns to read from in excel
excelReaderObj.setColumnValues(excelReadColumn)

#initialize IMDBInfo Object 
imdb = IMDBInfo()

#Start Title Search 
imdb.searchMovieList(excelReaderObj.getColumnValue())

#export to excel file
print('Exporting to Excel File')
excelReaderObj.exportExcel(imdb.getMovieList(), excelOutputFileName)
print('Export Completed')