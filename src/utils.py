import pgeocode

def calculate_distance(pincode1, pincode2):
    dist = pgeocode.GeoDistance('IN')
    # Returns distance in km
    distance_km = dist.query_postal_code(pincode1, pincode2)
    return round(distance_km, 2)

# Usage in your Match Agent:
# if calculate_distance(user_pincode, player_pincode) < 5.0:
#     recommend_player()

