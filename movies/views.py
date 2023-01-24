from rest_framework.views import APIView
from .serializers import MovieSerializer
from django.http.response import JsonResponse
from .models import movie
from django.http.response import Http404
from rest_framework.response import Response



class MovieView(APIView):
    def post(self ,request):
        data =request.data
        serializer =MovieSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse("MOVIES ADDED SUCCESFULLY",safe=False)
        return JsonResponse("failed to add movie",safe=False)

    def get_movie(self,pk):
        try:
            movies = movie.objects.get(movieId=pk)
            return movies;
        except movies:
            raise Http404;

    def get(self,request,pk=None):
        if pk:
            data=self.get_movie(pk)
            serializer = MovieSerializer(data)
        else:
            data=movie.objects.all()
            serializer=MovieSerializer(data ,many=True)
        return Response(serializer.data)


    def put(self ,request,pk=None):
        movie_to_update=movie.objects.get(movieId=pk)
        serializer =MovieSerializer(instance=movie_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("movie UPDATED SUCCESSFULLY", safe=False)
        return JsonResponse("FAILED TO UPDATE movie")

    def delete(self,request,pk=None):
        movie_to_delete =movie.objects.get(movieId=pk)
        movie_to_delete.delete()
        return JsonResponse("Movie deleted succesfully",safe=False)
    
