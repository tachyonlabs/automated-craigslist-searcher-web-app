from django import forms


class EditSearchSettingsForm(forms.Form):
    interval = forms.IntegerField(label="Search interval in minutes: ", min_value=1, max_value=1440)
    site = forms.CharField(label="Search Craigslist site: ", max_length=30)
    zip_code = forms.CharField(label="Center search on zip code: ", max_length=5)
    radius = forms.IntegerField(label="Search radius in miles: ", min_value=1, max_value=1000)
    search_terms = forms.CharField(label="Search terms (enter each search term on a line by itself): ",
                                   widget=forms.Textarea, max_length=5000)
