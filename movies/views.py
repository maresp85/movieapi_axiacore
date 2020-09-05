from django.shortcuts import render
from django.http import HttpResponse

from .serializers import GenreSerializer, MovieSerializer, MovieSerializerP
from .models import Genre, Movie
'''Rest framework'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
'''Background task'''
from background_task.models import Task
from background_task import background
from .tasks import call_api
import logging
import coreapi
import datetime

logger = logging.getLogger(__name__)
#log in file
logging.basicConfig(filename='logs/debug.log', level=logging.DEBUG)

#Web Service - GET Detail Movie
class DetailMovieAPI(APIView):

    permission_classes = (IsAuthenticated,)

    '''Get Movie (only 1)'''
    def get(self, request, pk):

        # if error occurs when querying id, so return with except
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, many=False)
            return Response({ "data": serializer.data }, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({ "error": str(error) }, status=status.HTTP_400_BAD_REQUEST)



# Web Services CRUD Movie
class MovieAPI(APIView):

    permission_classes = (IsAuthenticated,)

    '''List all movie'''
    def get(self, request):
        movie = Movie.objects.all()

        #pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(movie, request)

        serializer = MovieSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    '''Create movie'''
    def post(self, request, format=None):

        serializer = MovieSerializerP(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "data": serializer.data }, status=status.HTTP_201_CREATED)
        return Response({ "error": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

    '''Update movie'''
    def put(self, request, pk, format=None):

        # if error occurs when querying id, so return with except
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({ "data": serializer.data }, status=status.HTTP_200_OK)
            return Response({ "error": serializer.error }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({ "error": str(error) }, status=status.HTTP_400_BAD_REQUEST)

    '''Delete movie'''
    def delete(self, request, pk, format=None):

        # if error occurs when querying id, so return with except
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({ "data": "ok" }, status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({ "error": str(error) }, status=status.HTTP_400_BAD_REQUEST)


#Web Service - UPDATE Rating
class RatingMovieAPI(APIView):

    permission_classes = (IsAuthenticated,)

    '''Update Ranking Movie'''
    def put(self, request, pk, format=None):

        # if error occurs when querying id, so return with except
        try:
            movie = Movie.objects.get(pk=pk)
            if 'rating' in request.data:
                rating = request.data['rating']
                if rating >= 0 and rating <= 5:
                    serializer = MovieSerializer(movie, data=request.data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({ "data": serializer.data }, status=status.HTTP_200_OK)
                    return Response({ "error": serializer.error }, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({ "error": "The Rating value must be between 0 and 5" },
                                      status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({ "error": 'Not Rating value received' },
                                  status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({ "error": str(error) },
                              status=status.HTTP_400_BAD_REQUEST)

def tasks(request):
    date = datetime.datetime(year=datetime.datetime.now().year,
                             month=datetime.datetime.now().month,
                             day=datetime.datetime.now().day,
                             hour=16,
                             minute=58)
    call_api(schedule= date, repeat= Task.DAILY)
    #print(datetime.datetime.now())
    logging.debug("Init process Call API")
    return HttpResponse("End process Call API ")
