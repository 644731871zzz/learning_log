def city_and_country(city,country,population=''):
    if population=='':
        city_country=f"{city}, {country}"
    else:
        city_country=f"{city}, {country} - population {population}"
    return city_country.title()