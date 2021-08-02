from rest_framework import serializers

from .models import Anime, STATUS_OF_ANIME

# ModelSerializer has default create and update


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = ('__all__')
