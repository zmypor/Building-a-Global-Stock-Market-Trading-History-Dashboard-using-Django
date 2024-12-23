import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import SPGlobalIndex, IndexConstituent


def fetch_data(request):
    url = "https://eodhd.com/api/mp/unicornbay/spglobal/list?api_token=<YOUR_API_KEY>"
    response = requests.get(url)
    data = response.json()

    for item in data:
        SPGlobalIndex.objects.update_or_create(
            index_id=item.get("ID"),
            defaults={
                "code": item.get("Code"),
                "name": item.get("Name"),
                "constituents": item.get("Constituents"),
                "value": item.get("Value"),
                "market_cap": item.get("MarketCap"),
                "divisor": item.get("Divisor"),
                "daily_return": item.get("DailyReturn"),
                "dividend": item.get("Dividend"),
                "adjusted_market_cap": item.get("AdjustedMarketCap"),
                "adjusted_divisor": item.get("AdjustedDivisor"),
                "adjusted_constituents": item.get("AdjustedConstituents"),
                "currency_code": item.get("CurrencyCode"),
                "currency_name": item.get("CurrencyName"),
                "currency_symbol": item.get("CurrencySymbol"),
                "last_update": item.get("LastUpdate"),
            },
        )

    indices = SPGlobalIndex.objects.all()
    return render(request, "spglobal/index.html", {"indices": indices})


def fetch_index_constituents(request, index_code):
    url = f'https://eodhd.com/api/mp/unicornbay/spglobal/comp/{index_code}?fmt=json&api_token=<YOUR_API_KEY>'
    response = requests.get(url)
    data = response.json()

    # Extract constituents and general information
    constituents = data['Components'].values()
    general_info = data['General']

    return render(request, 'spglobal/constituents.html', {
        'constituents': constituents,
        'general_info': general_info
    })

