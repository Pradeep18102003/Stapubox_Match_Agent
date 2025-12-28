import json
import random
from faker import Faker
from pathlib import Path

fake = Faker('en_IN')

LOCATION_PIN_MAP = {
    "Noida Sector 62": "201309",
    "Noida Sector 15": "201301",
    "Gurgaon Ph 3": "122010",
    "DLF Phase II": "122008",
    "Indirapuram": "201014",
    "Hauz Khas": "110016",
    "Connaught Place": "110001",
    "Rohini": "110085"
}


SPORTS = ['Badminton', 'Cricket', 'Football', 'Tennis', 'Table Tennis', 'Gym']
SKILL_LEVELS = ['Beginner', 'Intermediate', 'Advanced']


TIMINGS = ["Early Mornings", "Weekends", "Weekday Evenings", "Afternoons"]

def generate_stapubox_data(num_players=2000):

    project_root = Path(__file__).parent.parent
    data_folder = project_root / "data"
    output_file = data_folder / "players.json"

    data_folder.mkdir(exist_ok=True)
    players = []
    locations = list(LOCATION_PIN_MAP.keys())
    
    for i in range(num_players):
        loc = random.choice(locations)
        sport = random.choice(SPORTS)
        
        player = {
            "id": f"STAPU_{1000 + i}",
            "name": fake.name(),
            "sport": sport,
            "skill_level": random.choice(SKILL_LEVELS),
            "location": loc,
            "pincode": LOCATION_PIN_MAP[loc],
            "availability": random.choice(TIMINGS),
            "bio": f"I'm a {sport.lower()} enthusiast looking for partners near {loc}."
        }
        players.append(player)

    with open(output_file, "w") as f:
        json.dump(players, f, indent=4)
        
    print(f"✅ Successfully saved {num_players} players to: {output_file}")

if __name__ == "__main__":
    generate_stapubox_data()