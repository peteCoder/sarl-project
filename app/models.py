from django.db import models

# Create your models here.



class Destination(models.Model):
    destination = models.CharField(max_length=30, blank=False, null=False)
    description =  models.CharField(max_length=100, blank=False, null=False)
    trip_duration = models.CharField(max_length=100, blank=True, null=False)
    travel_fee = models.CharField(max_length=100, blank=True, null=False)
    image = models.ImageField(upload_to="media", blank=False, null=False)
    other_details =  models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"

    def __str__(self) -> str:
        return self.destination


class Team(models.Model):
    staff_name = models.CharField(max_length=100, blank=False, null=False)
    position = models.CharField(max_length=100, blank=False, null=False)
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    twitter_url = models.URLField()

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self) -> str:
        return self.staff_name


class CountriesVisited(models.Model):
    country_name = models.CharField(max_length=100, blank=False, null=False)
    short_description = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=False, null=False)

    class Meta:
        verbose_name = "Country Visited"
        verbose_name_plural = "Countries Visited"

    def __str__(self) -> str:
        return self.country_name
    
class Testimonials(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    position = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="media", blank=False, null=False)
    review = models.TextField()

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self) -> str:
        return self.name

