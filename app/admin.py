from django.contrib import admin
from .models import (
    Testimonials,
    Team,
    CountriesVisited,
    Destination
)
# Register your models here.

admin.site.register(Testimonials)
admin.site.register(Team)
admin.site.register(CountriesVisited)
admin.site.register(Destination)











