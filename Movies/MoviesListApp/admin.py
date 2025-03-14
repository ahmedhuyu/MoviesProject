from django.contrib import admin

# Register your models here.
from .models import Movies_Info, Publisher, Contributors, MovieContributor, Review


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'email')

class MovieAdmin(admin.ModelAdmin):
    list_filter = ('publisher',)

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Movies_Info, MovieAdmin)
admin.site.register(Contributors)
admin.site.register(MovieContributor)
admin.site.register(Review)
