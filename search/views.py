from django.shortcuts import render, redirect
from craigslist import CraigslistForSale
from .models import SearchResult, Settings
from .forms import EditSearchSettingsForm
import datetime


def search_results(request):
    all_results = []
    settings = Settings.objects.first()
    search_interval_in_minutes = settings.search_interval_minutes

    for query in settings.search_terms.split(", "):
        part = {}
        part["query"] = query
        part_results = []
        cl_searcher = CraigslistForSale(site=settings.search_site,
                                        filters={"query": query, "posted_today": True,
                                                 "zip_code": settings.search_zip_code,
                                                 "search_distance": settings.search_radius,
                                                 "search_titles": True})

        for result in cl_searcher.get_results(sort_by='newest', geotagged=True):
            search_result = SearchResult()
            search_result.name = result["name"].title() if result["name"] else ""
            search_result.price = result["price"] if result["price"] else ""
            search_result.location = result["where"].title() if result["where"] else ""
            search_result.url = result["url"]
            part_results.append(search_result)

        if part_results:
            part["results"] = part_results
            all_results.append(part)

    extra_title_text = " - last checked {}".format(datetime.datetime.now().strftime("%I:%M:%S %p")).replace(" 0", " ")

    return render(request, 'search/search_results.html',
                  {'all_results': all_results, 'search_interval_in_minutes': search_interval_in_minutes,
                   'extra_title_text': extra_title_text})


def edit_search_settings(request):
    search_settings = Settings.objects.first()
    search_interval = search_settings.search_interval_minutes
    search_site = search_settings.search_site
    search_zip_code = search_settings.search_zip_code
    search_radius = search_settings.search_radius
    search_terms = "\n".join(search_settings.search_terms.split(", "))

    if request.method == "POST":
        if ("Cancel", "Cancel") in request.POST.items():
            # if the user clicked Cancel
            return redirect('search_results')

        form = EditSearchSettingsForm(request.POST)

        if form.is_valid():
            search_settings.search_interval_minutes = form.cleaned_data['interval']
            search_settings.search_site = form.cleaned_data['site'].strip()
            search_settings.search_zip_code = form.cleaned_data['zip_code']
            search_settings.search_radius = form.cleaned_data['radius']

            # Convert the \r\n-delimited textarea to ", "-delimited string, getting rid of any blank lines
            # or leading or trailing whitespace.
            terms_from_form = [term.strip() for term in form.cleaned_data["search_terms"].strip().split("\r\n")]
            search_settings.search_terms = ", ".join(term for term in terms_from_form if term)

            search_settings.save()

            return redirect('search_results')

    else:
        form = EditSearchSettingsForm()

    return render(request, 'search/edit_search_settings.html',
                  {'form': form, 'search_interval': search_interval, 'search_site': search_site,
                   'search_zip_code': search_zip_code, 'search_radius': search_radius,
                   'search_terms': search_terms})
