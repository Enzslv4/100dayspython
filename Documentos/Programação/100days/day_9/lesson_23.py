country = input('The country you visited: ') # Add country name
visits = int(input('The number of visits: ')) # Number of visits
list_of_cities = eval(input('A list of cities you visited: ')) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

travel_log.append({
    "country": country,
    "visits": visits,
    "cities": list_of_cities
})

# print(travel_log)

# add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")