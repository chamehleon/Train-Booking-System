from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User

# Create your models here.


class Train(models.Model):
    train_id = models.IntegerField()
    model = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return str(self.train_id)


class Trip(models.Model):
    date = models.DateField(default=django.utils.timezone.now)
    From = models.TimeField(default=django.utils.timezone.now)
    To = models.TimeField(default=django.utils.timezone.now)
    source = models.CharField(max_length=50, default="")
    destination = models.CharField(max_length=50, default="")
    number_of_seats = models.IntegerField(default=0)
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)
    books =models.ManyToManyField(User,blank=True)
    trip_id =models.IntegerField(primary_key=True,default=0000)
    
    def __str__(self):
        return str("From " + self.source + " to " + self.destination)
