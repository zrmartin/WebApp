from .models import Entry, Activity, Concert, Artist, Venue, User
from rest_framework import serializers
from django.shortcuts import get_object_or_404

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    pub_date_errors = {"unique" : "Date must be unique", "invalid": "Invalid date"}
    pub_date = serializers.DateField(format="%m/%d/%Y", error_messages=pub_date_errors)

    class Meta:
        model = Entry
        fields = ('pub_date', 'summary')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    entry = EntrySerializer()
    class Meta:
        model = Activity
        fields = ('entry', 'name', 'duration')

    def create(self, validated_data):
        entry_dict = validated_data.pop('entry')
        entry = Entry.objects.get(pub_date=entry_dict['pub_date'])
        activity = Activity.objects.create(entry=entry, **validated_data)
        return activity

    def update(self, instance, validated_data):
        entry = Entry.objects.get(pub_date=validated_data.get('entry')['pub_date'])
        instance.entry = entry
        instance.name = validated_data.get('name', instance.name)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ('name', 'state', 'city', 'style')

class ConcertSerializer(serializers.HyperlinkedModelSerializer):
    venue = VenueSerializer()
    date_errors = {"unique" : "Date must be unique", "invalid": "Invalid date"}
    date = serializers.DateField(format="%m/%d/%Y")

    class Meta:
        model = Concert
        fields = ('date', 'name', 'notes', 'venue')

    def create(self, validated_data):
        venue_dict = validated_data.pop('venue')
        venue = Venue.objects.get(name=venue_dict['name'])
        concert = Concert.objects.create(venue=venue, **validated_data)
        return concert
    def update(self, instance, validated_data):
        venue = Venue.objects.get(name=validated_data.get('venue')['name'])
        instance.venue = venue
        instance.date = validated_data.get('date', instance.date)
        instance.name = validated_data.get('name', instance.name)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    concert = ConcertSerializer()
    class Meta:
        model = Artist
        fields = ('name', 'genre', 'rating', 'concert')

    def create(self, validated_data):
        concert_dict = validated_data.pop('concert')
        concert = Concert.objects.get(date=concert_dict['date'])
        artist = Artist.objects.create(concert=concert, **validated_data)
        return artist

    def update(self, instance, validated_data):
        concert = Concert.objects.get(date=validated_data.get('concert')['date'])
        instance.concert = concert
        instance.name = validated_data.get('name', instance.name)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance








