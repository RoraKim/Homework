
from rest_framework import serializers
from .models import Artist, Music


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('title',)


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artists',)

class ArtistSerializer(serializers.ModelSerializer):
    class MusicSerializerForArtist(serializers.ModelSerializer):

        class Meta:
            model = Music
            fields = ('title',)
    #이 가수가 가지고 있는 음악 정보 
    #field에 있는 music_set에 정보를 직접 넣을 필요는 없게 read_only=True
    music_set = MusicSerializerForArtist(many=True, read_only=True)
    #음악 정보 개수 
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count')



