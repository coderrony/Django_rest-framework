# from django.shortcuts import render
# from .models import Movie
# from django.http import HttpResponse, JsonResponse
# # Create your views here.


# def movie_list(request):
#     # movies = Movie.objects.all().values()  # all objects are converted to dictionary
#     movies = Movie.objects.all()

#     data = {
#         'movies': list(movies.values())
#     }

#     return JsonResponse(data)


# def movie_details(self, pk):
#     movie = Movie.objects.get(pk=pk)

#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active

#     }
#     return JsonResponse(data)
