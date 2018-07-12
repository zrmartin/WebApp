from .models import Entry, Concert, Artist, Venue, Activity
from.serializers import EntrySerializer, ConcertSerializer, ArtistSerializer, VenueSerializer, ActivitySerializer
from rest_framework import generics

# ***** ENTRY **** #
class EntryList(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryCreate(generics.CreateAPIView):
    serializer_class = EntrySerializer

class EntryUpdate(generics.UpdateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'pub_date'

class EntryDelete(generics.DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'pub_date'

# ***** ACTIVITY **** #
class ActivityList(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityCreate(generics.CreateAPIView):
    serializer_class = ActivitySerializer

class ActivityUpdate(generics.UpdateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'name'

# ***** CONCERT ***** #
class ConcertList(generics.ListAPIView):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

class ConcertCreate(generics.CreateAPIView):
    serializer_class = ConcertSerializer

class ConcertUpdate(generics.UpdateAPIView):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    lookup_field = 'date'

class ConcertDelete(generics.DestroyAPIView):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    lookup_field = 'date'

# ***** ARTIST ***** #
class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'date'

class ArtistCreate(generics.CreateAPIView):
    serializer_class = ArtistSerializer

class ArtistUpdate(generics.UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'name'

class VenueList(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueCreate(generics.CreateAPIView):
    serializer_class = VenueSerializer

class VenueUpdate(generics.UpdateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    lookup_field = 'name'

class VenueDelete(generics.DestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    lookup_field = 'name'

class RawSQLQuery1(generics.ListAPIView):
    queryset = Venue.objects.raw('SELECT * FROM venue')
    serializer_class = VenueSerializer

class RawSQLQuery2(generics.ListAPIView):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer








