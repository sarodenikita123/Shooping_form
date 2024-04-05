from django.db import models


class Shopping(models.Model):
    que = [("ONE", "1"), ("TWO", "2"), ("TREE", "3"), ("FOUR", "4"), ("FIVE", "5")]
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    quantity = models.CharField(max_length=20, choices=que, default=True)
    destination = models.CharField(max_length=30)
    arrival_date = models.DateField()
    return_date = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


