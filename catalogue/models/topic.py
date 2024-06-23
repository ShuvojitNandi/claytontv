from django.db import models
from .video import Video
from .series import Series
from django.urls import reverse # generate urls by reversing url pattern


class Topic(models.Model):
    """Model representing video topics"""
    name = models.CharField(max_length=200, unique=True, help_text="Enter a topic or theme")
    summary = models.TextField(max_length=5000, help_text="Enter a brief summary of the topic")
    category = models.CharField(max_length=200, unique=True, help_text="Enter the categpry of he topic") #could be a many to many?
    videos = models.ManyToManyField(Video, help_text="Select topics for this video")
    series = models.ManyToManyField(Series, help_text="Select topics for this video")
    #sub_topic needed, maybe a class inheriting from Topic? Eg. am/pm for services and bible books for 'bible teaching' topic?

    def __str__(self):
        """String for representing the model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular topic instance"""
        return reverse('topic-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']