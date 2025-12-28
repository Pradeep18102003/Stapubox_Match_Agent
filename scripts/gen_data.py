import json
import random
from faker import Faker
from pathlib import Path

fake = Faker('en_IN')

# Real Delhi-NCR Pincode Map for realism
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

SPORTS = ['Badminton', 'Cricket', 'Football', 'Tennis', 'Table Tennis']
SKILL_LEVELS = ['Beginner', 'Intermediate', 'Advanced']

def generate_stapubox_data(num_players=50):
    players = []
    locations = list(LOCATION_PIN_MAP.keys())
    
    for i in range(num_players):
        loc = random.choice(locations)
        player = {
            "id": f"STAPU_{1000 + i}",
            "name": fake.name(),
            "sport": random.choice(SPORTS),
            "skill_level": random.choice(SKILL_LEVELS),
            "location": loc,
            "pincode": LOCATION_PIN_MAP[loc],  # Added Pincode
            "availability": random.choice(["Weekends", "Evenings"]),
            "bio": f"Looking for {random.choice(SPORTS).lower()} partners near {loc}."
        }
        players.append(player)

    Path("data").mkdir(exist_ok=True)
    with open("data/players.json", "w") as f:
        json.dump(players, f, indent=4)
    print(f"✅ Generated {num_players} players with pincodes in data/players.json")

if __name__ == "__main__":
    generate_stapubox_data()