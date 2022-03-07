from django.db import models
from django.contrib.auth.models import User


OUTPUT_CHOCES = (
    ('N', 'normal'),
    ('D', 'diagonal'),
)


class Matrix(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    matrix = models.JSONField()
    output_data = models.IntegerField(null=True)
    output_type = models.CharField(max_length=1, choices=OUTPUT_CHOCES)


class String(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    string = models.CharField(max_length=255)
    output_data = models.CharField(max_length=255, null=True)

