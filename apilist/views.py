from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import HttpResponse,  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from .serializers import AnimeSerializer
from .models import Anime
from rest_framework.decorators import api_view
# class AnimeViewSet(viewsets.ModelViewSet):
#     queryset = Anime.objects.all().order_by('name')
#     serializer_class = AnimeSerializer


@csrf_exempt
def anime_list(request):
    """
    List all code snippets, or create a new snippet
    """
    if request.method == 'GET':
        anime = Anime.objects.all()
        serializer = AnimeSerializer(anime, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnimeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def anime_detail(request, pk):

    try:
        anime = Anime.objects.get(pk=pk)
    except Anime.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = AnimeSerializer(anime)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AnimeSerializer(anime, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        anime.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
def anime_status(request, status):
    try:
        anime = Anime.objects.filter(status=status)
    except Anime.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        print(anime)
        serializer = AnimeSerializer(anime, many=True)
        return JsonResponse(serializer.data, safe=False)
