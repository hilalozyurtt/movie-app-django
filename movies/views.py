from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import date

data = {
    "movies":
    [
        {
            "title": "film adi 1",
            "description": "film açıklama 1",
            "imageURL": "m1.jpg",
            "coverImage": "cover.jpg",
            "slug": "film-adi-1",
            "language": "english",
            "date": date(2021,10,10),
        },
                {
            "title": "film adi 2",
            "description": "film açıklama 2",
            "imageURL": "m2.jpg",
            "coverImage": "cover2.jpg",
            "slug": "film-adi-2",
            "language": "english",
            "date": date(2022,10,10),
        },
                {
            "title": "film adi 3",
            "description": "film açıklama 3",
            "imageURL": "m3.jpg",
            "coverImage": "cover3.jpg",
            "slug": "film-adi-3",
            "language": "english",
            "date": date(2019,10,10),
        },
            {
            "title": "film adi 4",
            "description": "film açıklama 4",
            "imageURL": "m4.jpg",
            "coverImage": "cover.jpg",
            "slug": "film-adi-4",
            "language": "english",
            "date": date(2019,10,5),
        },
    ],
    "sliders":[
        {
            "slider_image": "slider1.jpg",
            "url": "slider-name-1",
        },
        {
            "slider_image": "slider2.jpg",
            "url": "slider-name-2",
        },
                {
            "slider_image": "slider3.jpg",
            "url": "slider-name-3",
        },
    ],
}



# Create your views here.

def index(request):
    movies = data["movies"][-4:]
    sliders = data["sliders"]
    return render(request, 'index.html',{
        "movies":movies,
        "sliders": sliders
    })

def movies(request):
    movies = data["movies"]
    return render(request, 'movies.html', {
        "movies": movies
    })

def movie_details(request, slugname):
    movies = data["movies"]
    
    #selectedMovie = None
    #for movie in movies:
    #    if movie["slug"] == slugname:
    #        selectedMovie = movie

    selectedMovie = next(movie for movie in movies if movie["slug"] == slugname) # Burdan generator tipi gelir, bizde veriyi next ile alırız.
    print(selectedMovie)

    return render(request, 'movie_details.html', {
        "movie" : selectedMovie,
    })