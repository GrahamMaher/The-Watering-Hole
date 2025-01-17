from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Table(models.Model):

    number = models.IntegerField(unique=True)

    seats = models.IntegerField()


    def __str__(self):

        return f"Table {self.number} - Seats: {self.seats}"


class Reservation(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    date = models.DateField()

    time = models.TimeField()

    number_of_guests = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"Reservation by {self.user.username} on {self.date} at {self.time}"