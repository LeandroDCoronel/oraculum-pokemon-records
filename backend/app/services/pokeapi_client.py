import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_data(pokemon_id: int):
    url = f"{BASE_URL}/pokemon/{pokemon_id}"

    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            return None
        
        data = response.json()

        return {
            "id": data["id"],
            "name": data["name"],
            "types": [t["type"]["name"] for t in data["types"]],
            "base_stats": {
                stat["stat"]["name"]: stat["base_stat"]
                for stat in data["stats"]
            }
        }

    except Exception as e:
        print("Error fetching from PokeAPI:", e)
        return None