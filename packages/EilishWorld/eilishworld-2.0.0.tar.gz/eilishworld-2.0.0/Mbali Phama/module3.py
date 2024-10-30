LIGHT_SPEED = 299792458  # Speed of light in meters per second
EARTH_RADIUS = 6371  # Radius of Earth in kilometers

# Functions
def time_to_travel_distance(distance):
    return distance / LIGHT_SPEED

def earth_circumference():
    return 2 * 3.14159 * EARTH_RADIUS