from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField()
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()
    
    # Default String
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

class Seat(models.Model):
    seat_number = models.CharField()
    is_booked = models.BooleanField()
    
    # Default String
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('seat-detail', args=[str(self.id)])

class Booking():
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    # Default String
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('booking-detail', args=[str(self.id)])
