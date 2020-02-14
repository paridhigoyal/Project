from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    type = (
        ('T', 'Transporter'),
        ('C', 'Customer'),
    )
    profile_type = models.CharField(max_length=1, choices=type)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=30, default="")
    state = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=12, default="")
    pin_code = models.IntegerField()

    def is_customer(self):
        return self.profile_type == 'C'

    def is_transporter(self):
        return self.profile_type == 'T'

    def __str__(self):
        return self.user.username


class Vehicle(models.Model):
    # vehicle_id = models.IntegerField(primary_key=True)
    vehicle_type = models.CharField(max_length=50, default='')
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    man_Year = models.IntegerField()
    capacity = models.IntegerField()
    picture = models.ImageField(null=True)
    document = models.CharField(max_length=100)
    transporter = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")

    def __unicode__(self):
        return self.Vehicle.id


class Rating(models.Model):
    rate = (('1', 'Worst Experience'), ('2', 'Bad Experience',),
            ('3', 'Good Experience'), ('4', 'Very Good Experience'),
            ('5', 'Excellent Experience')
            )
    rating = models.CharField(max_length=1, choices=rate)
    transporter = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # deal_id = models.OneToOneField(Deal, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.transporter.user.username


class Deal(models.Model):
    deal_id = models.IntegerField(primary_key=True)
    start_Date = models.DateField()
    end_date = models.DateField()
    start_city = models.CharField(max_length=50)
    end_city = models.CharField(max_length=50)
    price = models.IntegerField()
    # transporter = models.ManyToManyField(Profile)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vehicle_id = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.deal_id


class Query(models.Model):
    c_request = models.TextField(default="Handle with Care")
    t_response = models.TextField(default="yes")
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.Query
