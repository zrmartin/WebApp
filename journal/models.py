from django.db import models

class Entry(models.Model):
    pub_date = models.DateField(format("%m/%d/%Y"), unique=True)
    summary = models.TextField(blank=True, default="You have not written a summary for today yet.")

    def __str__(self):
        return str(self.pub_date)
    class Meta:
        db_table = 'entry'

class Activity(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'activity'

    def __str__(self):
        return str(self.name)

class Concert(models.Model):
    date = models.DateField(format("%m/%d/%Y"), unique=True)
    venue = models.ForeignKey('Venue', related_name='venue', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    notes = models.TextField(default="You have written no notes about this concert.")

    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = 'concert'

class Venue(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    style = models.CharField(max_length=100)    #I.E Indoor Bar / Outdoor Festival

    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = 'venue'

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.SmallIntegerField()
    concert = models.ForeignKey('Concert', related_name='concert', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = 'artist'


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    birth_day = models.DateField(format("%m/%d/%Y"))

    class Meta:
        db_table = 'user'
    def __str__(self):
        return str(self.first_name)



