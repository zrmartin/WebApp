from .models import Entry, Activity
from rest_framework import serializers

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    pub_date_errors = {"unique" : "Date must be unique", "invalid": "Invalid date"}

    pub_date = serializers.DateField(format="%m/%d/%Y", error_messages=pub_date_errors)

    class Meta:
        model = Entry
        fields = ('pub_date', 'summary')



class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('entry', 'activity_name',)



