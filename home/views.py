from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import movie_recommender

import requests
my_api_key = "e48a6eb6523a890ae3303e1f6d93a049"


# Create your views here.
def index(request):
    return render(request, "home/index.html")

def search(request):
    form = forms.SearchForm()
    r_dict = []
    flag = "null"

    if request.method == 'POST':
        form = forms.SearchForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            flag = movie_recommender.look_for(title)
            
            if(flag==False):
                print("Movie does not exist in our database.")
            else:
                r_list = movie_recommender.rcmd(title)
                r_dict =[]
                for element in r_list:
                    url = 'https://api.themoviedb.org/3/search/movie?api_key='+str(my_api_key)+'&query='+str(element)
                    response = (requests.get(url)).json()
                    img_result = response['results'][0]['poster_path']
                    poster_path = 'https://image.tmdb.org/t/p/original'+str(img_result)
                    r_dict.append(poster_path)    


    return render(request, 'home/search_page.html',{"form":form, "flag":flag,"r_dict": r_dict })
