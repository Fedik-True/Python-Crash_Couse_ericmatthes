def get_culture(city, country, population=""):
    """Returns a 'from' information."""
    if population:
        formatted_culture = f"{city}, {country}\npopulation: {population}"
    else:
        formatted_culture = f"{city}, {country}"
    return formatted_culture.title()
