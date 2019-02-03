from django.shortcuts import render
from craigslist import CraigslistForSale
from .models import SearchResult


def search_results(request):
    all_results = []
    # Later the search terms, zip code, and radius will be editable and stored in the database rather than hard-coded
    for query in ["Table saw", "Band saw", "Oculus Rift", "HTC Vive", "VR Headset"]:
        part = {}
        part["query"] = query
        part_results = []
        cl_searcher = CraigslistForSale(site="sfbay",
                                        filters={"query": query, "posted_today": True, "zip_code": "95060",
                                                 "search_distance": 80, "search_titles": True})

        for result in cl_searcher.get_results(sort_by='newest', geotagged=True):
            search_result = SearchResult()
            search_result.name = result["name"].title() if result["name"] else ""
            search_result.price = result["price"] if result["price"] else ""
            search_result.where = result["where"].title() if result["where"] else ""
            search_result.url = result["url"]
            part_results.append(search_result)

        if part_results:
            part["results"] = part_results
            all_results.append(part)

    return render(request, 'search/search_results.html', {'all_results': all_results})
