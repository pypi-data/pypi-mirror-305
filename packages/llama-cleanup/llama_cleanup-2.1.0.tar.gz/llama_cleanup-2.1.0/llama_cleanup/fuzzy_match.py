from thefuzz import process

def fuzzy_city_lookup(city, cities_list):
    if city is None or len(cities_list) == 0:
        return city
    best_match = process.extractOne(city, cities_list)
    if best_match and best_match[1] > 80:  # Confidence threshold
        return best_match[0]
    else:
        return city

