from rest_framework import serializers
from .models import Artist, Music


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        # fileds = ('id', 'name', )
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'
        # exclude = ('artist', )
        read_only_fields = ('artist',)
        depth = 1
        

class ArtistSerializer(serializers.ModelSerializer):
    class MusicSerializerForArtist(serializers.ModelSerializer):

        class Meta:
            model = Music
            fields = ('title',)
    # 이 가수가 가지고 있는 음악 정보
    # music_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    music_set = MusicSerializerForArtist(many=True, read_only=True)
    # 음악 정보 개수
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)


    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count')
