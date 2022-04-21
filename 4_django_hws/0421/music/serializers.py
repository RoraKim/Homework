import imp
from rest_framework import serializers
from .models import Artist


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    #이 가수가 가지고 있는 음악 정보 
    #field에 있는 music_set에 정보를 직접 넣을 필요는 없게
    music_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #음악 정보 개수 
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set',)