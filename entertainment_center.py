import fresh_tomatoes
import media

# So this is first attempt at adding stuff from testing.py

import requests
import json

# Take this out -- only for testing
import webbrowser

youtube_key = 'AIzaSyCmJT7e_pi5-5yWNi4F9UXuV8j1fUTlIm8'
youtube_prefix = 'https://www.youtube.com/watch?v='


# Movie list -- Here you can add and subtract movies as your tastes change
movie_list = ["There Will Be Blood", "The Life Aquatic", "Unforgiven"]

# TODO: make consistent qoutes, either single or double...check style guide

def getApi(movie):
    # Youtube stuff here
    youtube = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + movie + 'trailer&maxResults=1&key=' + youtube_key)
    youtube_str = youtube.text
    youtube_dict = json.loads(youtube_str)
    video_Id = youtube_dict['items'][0]['id']['videoId']
    video_url = youtube_prefix + video_Id

        # Open the trailer...just for testing
    # webbrowser.open(video_url)

    # Movie Database stuff here
    result = requests.get('http://www.omdbapi.com/?t=' + movie + '&y=&plot=short&r=json')

    resp_str = result.text

        # Convert data into a python dictionary
        # http://stackoverflow.com/questions/12788217/extract-single-value-from-json-response-python
    resp_dict = json.loads(resp_str)
    print(resp_dict)

    trailer = video_url
    title = resp_dict["Title"]
    #poster = 
    #release = 
    #rating = 
    #runtime = 
    #genre = 
    #director = 
    #plot = 
    #actors = 

getApi(movie_list[2])
