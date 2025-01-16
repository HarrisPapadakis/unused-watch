def describe_city(city, country="Iceland"):
    """Display a city that is located in which country."""  # Explains the purpose of the function to display the city's location in dockstring.
    print(f"{city} is in {country}.")  # Prints the city and the country where it is located.

describe_city("Reykjavik")  # Calls the function with the city "Reykjavik" and uses the default country "Iceland".
describe_city("Akureyri")  # Calls the function with the city "Akureyri" and uses the default country "Iceland".
describe_city(city="Athens", country="Greece")  # Calls the function with the city "Athens" and overrides the default country with "Greece".
