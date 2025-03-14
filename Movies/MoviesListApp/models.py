from django.db import models
from django.contrib import auth

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the publisher")
    website = models.URLField(help_text="The Publisher website")
    email = models.EmailField(help_text="Publisher's email address")

    def __str__(self): #دالة __str__ تستخدم دائما داخل class
        return self.name

class Movies_Info(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the movie")
    date = models.DateField(verbose_name="Date of release.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) #foreignKey :for many to one type of data relationship
    contributors = models.ManyToManyField('Contributors', through="MovieContributor")

    def __str__(self): #دالة __str__ تستخدم دائما داخل class
        return self.name


class Contributors(models.Model): #مساهمين مثل الممثلين و المخرجين ووو
    first_name = models.CharField(max_length=50, help_text="contributer's first name")
    last_name = models.CharField(max_length=50, help_text="contributer's last name")
    email = models.EmailField(help_text="contributer's email address")

    def __str__(self): #دالة __str__ تستخدم دائما داخل class ، تعطينا الـ object as string
        return self.first_name

class MovieContributor(models.Model):
    class ContributionRole(models.TextChoices):
        ACTOR = "ACTOR", "Actor"
        DIRECTOR = "DIRECTOR", "Director"
    movie = models.ForeignKey(Movies_Info, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributors, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the movie. ", choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField(help_text="Review text")
    rating = models.IntegerField(help_text="Rating of the reviewer")
    date_creating = models.DateTimeField(auto_now_add=True, help_text="date and time created")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE) #foreignKey :for many to one type of data relationship
    movie = models.ForeignKey(Movies_Info, on_delete=models.CASCADE, help_text="The movie that this review is for") #foreignKey :for many to one type of data relationship