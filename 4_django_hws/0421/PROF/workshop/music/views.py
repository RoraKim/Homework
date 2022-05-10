from urllib import request
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Artist, Music
from .serializers import (
    ArtistListSerializer,
    ArtistSerializer,
    MusicSerializer,
)

# Create your views here.

@swagger_auto_schema(methods=['POST'], request_body=ArtistSerializer)
@api_view(['GET', 'POST'])
def artist_list_create(request):
    if request.method == 'GET':
        # artists = Artist.objects.all()
        # artists = Artist.objects.order_by('-pk')
        artists = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def artist_detail_delete(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        artist.delete()
        data = {
            'DELETE' : f'{artist_pk}번째 게시글이 삭제 되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def music_list(request):
    music = get_list_or_404(Music)
    serializer = MusicSerializer(music, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save(commit=False)
        # serializer.artist = artist
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def music_detail_update(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        return Response({'id': music_pk}, status=status.HTTP_204_NO_CONTENT)