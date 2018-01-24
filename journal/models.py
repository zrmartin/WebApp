from django.db import models

class Entry(models.Model):
    pub_date = models.DateField()

    def __str__(self):
        return str(self.pub_date)

class Activity(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200)

    def __str__(self):
        return self.activity_name



