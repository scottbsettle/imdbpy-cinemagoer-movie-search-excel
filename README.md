Imdbpy -Cinemagoer-Excel-Wrapper
This wrapper utilizes excel to read in the movie list and find related titles in the imdb database. Python imports needed are pandas, openpyxl, and cinemagoer 
Before running 
1.)	install needed packages 
Pandas – pip install pandas 
Openpyxl – pip install openpyxl 
Cinemagoer – pip install cinemagoer 

2.)	Update main.py variables for excel input/output
#set excel file read from
excelReadPath – path for excel file to read in movie list inputs
excelReadFileName – filename of xlsx file to read from
excelReadColumn – column name in the excel file using to search (this was test for movie titles but should work if you have the Ids also) 

#Set the excel output (if left default this will output files to project location called Output.xlsx)
excelOutputPath – folder path for output location 
excelOutputFileName – output file name

After updates execute the python file main.py to start the process of searching movies from the imdb database

I was getting a timeout error and added sleep functions to the imdbInfo.py functions. To execute faster either remove or change the time. Currently set to sleep for 5 seconds before each call to imdb. 
