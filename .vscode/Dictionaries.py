travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

cities_visited = {}

for country in travel_log:
    cities_visited[country] = {
        "Cities Visited": travel_log[country],
        "Total Visits": len(travel_log[country])
        
    }

print(cities_visited)

travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    {
    "country":"Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
    }
]
