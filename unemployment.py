# Application prints 3 countries with the lowest and 3 countries with the
# highest unemployment rate (based on specified year sorted by value of
# unemployment rate - i.e. first country in output has the highest/the lowest
# unemployment rate).

import json


def load_json():
    """ Loads json file called 'input.json'. File must be in
    the same directory as app. """
    json_file = open('input.json', "r")
    json_loaded = json.loads(json_file.read())
    json_file.close()
    return json_loaded


def rates_from_year(json_loaded, year):
    """ Returns an array of unemployment rates from specified year sorted
    by same order as in json file. If year is not in input json file, then
    it is undefined behaviour."""
    size = 1
    for i in json_loaded["size"]:
        size *= i
    years_count = json_loaded["size"][2]
    year_index = json_loaded["dimension"]["year"]["category"]["index"][str(year)]
    result = []
    for i in range(year_index, size, years_count):
        result.append(json_loaded["value"][i])
    return result


def lowest_countries(json_loaded, rates_in_year, countries_count):
    indexes = []
    mins = []
    """ Extract 'countries_count' of lowest values from rates"""
    for _ in range(countries_count):
        current_min = 101
        for i in rates_in_year:
            if i < current_min and i not in mins:
                current_min = i
        indexes.append(rates_in_year.index(current_min))
        mins.append(current_min)
    print(str(countries_count) + " countries with lowest unemployment rates:")
    print_countries(json_loaded, indexes)


def print_countries(json_loaded, indexes):
    countries = []
    country_codes = list(
        (json_loaded["dimension"]["area"]["category"]["index"]).keys())
    for i in indexes:
        countries.append(country_codes[i])
    for code in countries:
        print(json_loaded["dimension"]["area"]["category"]["label"][code])


def highest_countries(json_loaded, rates_in_year, countries_count):
    indexes = []
    maxes = []
    """ Extract 'countries_count' of highest values from rates"""
    for _ in range(countries_count):
        current_max = -1
        for i in rates_in_year:
            if i > current_max and i not in maxes:
                current_max = i
        indexes.append(rates_in_year.index(current_max))
        maxes.append(current_max)
    print(str(countries_count) + " countries with highest unemployment rates:")
    print_countries(json_loaded, indexes)
