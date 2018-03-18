from .models import Entry, Activity, Concert, Artist
from rest_framework import serializers

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    pub_date_errors = {"unique" : "Date must be unique", "invalid": "Invalid date"}

    pub_date = serializers.DateField(format="%m/%d/%Y", error_messages=pub_date_errors)

    class Meta:
        model = Entry
        fields = ('pub_date', 'summary')

class ConcertSerializer(serializers.HyperlinkedModelSerializer):
    date = serializers.DateField(format="%m/%d/%Y")

    class Meta:
        model = Concert
        fields = ('date', 'venue', 'name', 'notes')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    concert = ConcertSerializer()
    class Meta:
        model = Artist
        fields = ('name', 'genre', 'rating', 'concert')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('entry', 'activity_name',)



