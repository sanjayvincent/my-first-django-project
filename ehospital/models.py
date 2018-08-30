from django.db import models
from django.utils import timezone


class Patient(models.Model):
	
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    SEX = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('UNSURE', 'Unsure'),
        )    
    sex = models.CharField(null=True, blank=True, max_length=10, choices=SEX, verbose_name='Specify your sex')
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=8)

    def register_patient(self):
        self.save()

    def __str__(self):
        return self.first_name