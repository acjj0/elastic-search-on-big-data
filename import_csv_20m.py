import csv
import re

movie_csv = open('movies_20m.csv','r')

movie_reader = csv.DictReader(movie_csv)

for movie in movie_reader:
    print("{ \"create\" : { \"_index\": \"movies_20m\", \"_id\" : \"", movie['movieId'], "\" } }", sep='')
    title = re.sub(" \(.*\)$", "", re.sub('"','', movie['title']))
    year = movie['title'][-5:-1]
    if(not year.isdigit()):
        year = "2000"
    genres =movie['genres'].split('|')
    print("{ \"id\": \"", movie['movieId'], "\", \"title\": \"", title, "\", \"year\":", year, ", \"genre\":[", end='', sep='')
    for genre in genres[:-1]:
        print("\"", genre, "\",", end='', sep='')
    print("\"",genres[-1],"\"",end='', sep='')
    print("] }")
    
    
