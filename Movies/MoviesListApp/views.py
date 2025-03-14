from .models import Movies_Info
from django.shortcuts import render
from .utils import average_rating


def Movies_list(request):
    Movies = Movies_Info.objects.all()
    Movies_list = []
    for Movie in Movies :
        reviews = Movie.review_set.all()
        if reviews :
            Movie_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            Movie_rating = None
            number_of_reviews = 0
        Movies_list.append({'Movie':Movie, 'Movie_rating':Movie_rating, 'number_of_reviews':number_of_reviews})

    context = {'Movies_list': Movies_list}
    return render(request, 'MoviesListApp/Movies_list.html', context)