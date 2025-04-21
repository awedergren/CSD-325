# Amanda Wedergren
# April 16, 2025
# Module 7.2 Assignment

# Generate a formatted city and country.
def format_location(city, country, population = None, language = None):
    city_country = f"{city.capitalize()}, {country.capitalize()} - population {population}, {language}"

    return city_country

print(format_location('Beijing', 'China'))

print(format_location('Amsterdam', 'Netherlands', '930000'))

print(format_location('Madrid', 'Spain', '3200000', 'Spanish'))


