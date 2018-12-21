from django.db import models
from .directionOfFile import images_upload
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User1(models.Model):
    user=models.CharField(max_length=256,primary_key=True,default='',blank=True)
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    def __str__(self):
        return self.user


class User2(models.Model):
    user=models.OneToOneField(User1,on_delete=models.CASCADE,default='',blank=True,unique=True)
    email= models.EmailField(max_length=70)
    university=models.CharField(max_length=256,blank=True)
    speciality=models.CharField(max_length=256,blank=True)
    checking=models.BooleanField(default=False)
    score=models.IntegerField(blank=True,default="-",null=True)
    def __str__(self):
        return self.email

class Test(models.Model):
    number=models.IntegerField();
    SECTION_TYPE = (
        (1, 'English'),
        (2, 'Russion'),
    );
    sections = models.PositiveSmallIntegerField(choices=SECTION_TYPE);
    question=models.TextField(default='')
    img=models.ImageField(upload_to=images_upload,default='',blank=True)
    second_part=models.TextField(default='',blank=True)
    A=models.CharField(max_length=256)
    B=models.CharField(max_length=256)
    C=models.CharField(max_length=256)
    answer=models.CharField(max_length=256)
    def __str__(self):
        return self.answer

