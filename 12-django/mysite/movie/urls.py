from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:language>', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
]
