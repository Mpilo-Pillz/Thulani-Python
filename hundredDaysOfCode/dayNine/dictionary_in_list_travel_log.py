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
#🚨 Do NOT change the code above
def add_new_country(country, visits, cities):
  travel_log.append({
    country: country,
    visits: visits,
    cities: cities
  })
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
add_new_country("Mozambique", 3, ["Maputo", "Phemba"])

print(travel_log)

