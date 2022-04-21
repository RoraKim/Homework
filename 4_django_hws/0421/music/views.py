
from turtle import st
from rest_framework.response import Response
from rest_framework import status
from urllib import request
from rest_framework.decorators import api_view
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Artist
from .serializers import (ArtistListSerializer, ArtistSerializer)
from music import serializers

# Create your views here.

@api_view( ['GET'])
def artist_list_create(request):
    if request.method == 'GET':
        # artists = Artist.Objects.all()
        # artists = Artist.object.order_by('-pk')
        artists = get_list_or_404(Artist)
        serializers = ArtistListSerializer(artists, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = ArtistListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'POST'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        artist.delete()
        data = {
            'DELETE' : f'{artist_pk} 번째 게시글이 삭제 되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)