from .models import Entry
from.serializers import EntrySerializer, ActivitySerializer
from rest_framework import generics


class EntryList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryCreate(generics.CreateAPIView):
    serializer_class = EntrySerializer

class EntryUpdate(generics.UpdateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'pub_date'




