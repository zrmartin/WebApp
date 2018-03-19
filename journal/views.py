from .models import Entry, Concert, Artist
from.serializers import EntrySerializer, ConcertSerializer, ArtistSerializer
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





