**Imdbpy -Cinemagoer-Excel-Wrapper**

This wrapper utilizes Excel to read the movie list and find related titles in the IMDb database. Python imports needed are pandas, openpyxl, and cinemagoer. 

Before running 
1.)	install needed packages 

Pandas – pip install pandas 

Openpyxl – pip install openpyxl

Cinemagoer – pip install cinemagoer 

2.)	Update main.py variables for Excel input/output

**# Set Excel file read from**
excelReadPath – path for Excel file to read in movie list inputs

excelReadFileName – filename of xlsx file to read from

excelReadColumn – column name in the Excel file used to search (this was tested for movie titles but should work if you have the IDs also) 

**#Set the Excel output (if left default, this will output files to the project location called Output.xlsx)**

excelOutputPath – folder path for output location

excelOutputFileName – output file name

After updates, execute the python file main.py to start the process of searching movies from the IMDB database.

I was getting a timeout error, so I added sleep functions to the imdbInfo.py functions. To execute faster, either remove or change the time. It is currently set to sleep for 5 seconds before each call to imdb. 
