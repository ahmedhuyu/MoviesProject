from django.contrib import admin

# Register your models here.
from .models import Movies_Info, Publisher, Contributors, MovieContributor, Review

admin.site.register(Publisher)
admin.site.register(Movies_Info)
admin.site.register(Contributors)
admin.site.register(MovieContributor)
admin.site.register(Review)