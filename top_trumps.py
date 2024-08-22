import requests
import random

def pokemon_generator():
    pokemon_id = random.randint(1, 151)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        pokemon_info = response.json()
        pokemon_name = pokemon_info['name']
        pokemon_id = pokemon_info['id']
        pokemon_height = pokemon_info['height']
        pokemon_weight = pokemon_info['weight']
        return {"name": pokemon_name, "id": pokemon_id, "height": pokemon_height, "weight": pokemon_weight}
    else:
        print("Response", response)
        print("Pokemon not found")
        return None

def compare_stats_pokemon(pokemon_player_one, pokemon_player_two, stat):
    pokemon_one_stat = pokemon_player_one[stat]
    pokemon_two_stat = pokemon_player_two[stat]

    print(f"Player 1 {stat}: {pokemon_one_stat}")
    print(f"Player 2 {stat}: {pokemon_two_stat}")

    if pokemon_one_stat > pokemon_two_stat:
        print("Player 1 wins!")
    elif pokemon_one_stat < pokemon_two_stat:
        print("Player 2 wins!")
    else:
        print("It's a draw!")

def main_pokemon():
    player_one = pokemon_generator()
    player_two = pokemon_generator()

    print(f"Player 1 Pokemon: {player_one['name']}")
    print(f"Player 2 Pokemon: {player_two['name']}")

    stat_selection = input("Select a stat to compare (id, height, weight): ").lower().strip()

    while stat_selection not in ['id', 'height', 'weight']:
        stat_selection = input("Stat not found. Try again (id, height, weight): ").lower().strip()

    compare_stats_pokemon(player_one, player_two, stat_selection)

def planets_generator():
    planets = []
    planets.append(["Mercury", 57.9, 4879, 88, 0])
    planets.append(["Venus", 108.2, 12104, 224.7, 0])
    planets.append(["Earth", 149.6, 12756, 365.2, 1])
    planets.append(["Mars", 227.9, 6792, 687, 2])
    planets.append(["Jupiter", 778.6, 142984, 4331, 67])
    planets.append(["Saturn", 1433.5, 120536, 10747, 62])
    planets.append(["Uranus", 2872.5, 51118, 30589, 27])
    planets.append(["Neptune", 4495.1, 49528, 59800, 14])
    planets.append(["Pluto", 5906.4, 2370, 90560, 5])
    return random.choice(planets)

def compare_stats_planet(planets_player_one, planets_player_two, stat):
    planets_one_stat = planets_player_one[stat]
    planets_two_stat = planets_player_two[stat]

    print(f"Player 1 {stat}: {planets_one_stat}")
    print(f"Player 2 {stat}: {planets_two_stat}")

    if planets_one_stat > planets_two_stat:
        print("Player 1 wins!")
    elif planets_one_stat < planets_two_stat:
        print("Player 2 wins!")
    else:
        print("It's a draw!")

def main_planet():
    player_one = planets_generator()
    player_two = planets_generator()

    print(f"Player 1 Planet: {player_one[0]}")
    print(f"Player 2 Planet: {player_two[0]}")

    stat_selection = input("Which stat would you like to compare (distance from sun, size, orbital period, number of moons): ").lower().strip()

    while stat_selection not in ['distance from sun', 'size', 'orbital period', 'number of moons']:
        stat_selection = input("Stat not found. Please try again (distance from sun, size, orbital period, number of moons): ").lower().strip()

    stat_index_map = {
        'distance from sun': 1,
        'size': 2,
        'orbital period': 3,
        'number of moons': 4
    }

    compare_stats_planet(player_one, player_two, stat_index_map[stat_selection])

if __name__ == "__main__":
    pack_selection = input("Choose your Top Trumps Pack (Pokemon or Planets): ").lower().strip()

    while pack_selection not in ['pokemon', 'planets']:
        pack_selection = input("Pack not found. Try again (Pokemon, Planets): ").lower().strip()

    if pack_selection == 'pokemon':
        main_pokemon()
    elif pack_selection == 'planets':
        main_planet()