from django.db import models


class SearchResult(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Settings(models.Model):
    class Meta:
        # So the admin interface doesn't say "Settingss"
        verbose_name_plural = "Settings"

    search_interval_minutes = models.IntegerField()
    search_site = models.CharField(max_length=30, default="sfbay")
    search_zip_code = models.CharField(max_length=5)
    search_radius = models.IntegerField()
    search_terms = models.CharField(max_length=5000, default="Band saw")

    def publish(self):
        self.save()

    def __str__(self):
        return "Search site {} every {} minutes, in a radius of {} miles around zip code {}, for search terms {}".format(
            self.search_site, self.search_interval_minutes, self.search_radius, self.search_zip_code, self.search_terms)
