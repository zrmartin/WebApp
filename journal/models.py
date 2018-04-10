from django.db import models

class Entry(models.Model):
    pub_date = models.DateField(format("%m/%d/%Y"), unique=True)
    summary = models.TextField(blank=True, default="You have not written a summary for today yet.")

    def __str__(self):
        return str(self.pub_date)

class Concert(models.Model):
    date = models.DateField(format("%m/%d/%Y"), unique=True)
    venue = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    notes = models.TextField(default="You have written no notes about this concert.")

    def __str__(self):
        return str(self.name)


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.SmallIntegerField()
    concert = models.ForeignKey('Concert', related_name='concert', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Activity(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200)

    def __str__(self):
        return self.activity_name



