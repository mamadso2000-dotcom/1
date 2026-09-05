import math

#----------------------------------------------------------------is_conjuction----------------------------------------------------------------

# CALCULATE PLANET PLACE AT ORBITAL
# Calculate circle anomaly today
# period
def calculate_orbital_period(semi_major_axis):
    period = semi_major_axis ** (3 / 2)
    return period

# daily speed
def calculate_mean_motion(period):
    speed = 360 / (period * 365)
    return speed

# time different from epoch
def calculate_days_since_epoch(epoch, target_date):
    difference = target_date - epoch
    return difference.days

# anomaly different from epoch
def calculate_new_anomaly(mean_anomaly, speed, days):
    new_anomaly = mean_anomaly + speed * days
    Remainder = new_anomaly % 360
    if Remainder:
        new_anomaly = Remainder
    return new_anomaly

# Eccentric Anomaly
# solve_kepler
def solve_kepler(mean_anomaly, eccentricity):
    tolerance = 0.000001
    eccentric_anomaly = mean_anomaly
    kepler = eccentric_anomaly - eccentricity * math.sin(math.radians(eccentric_anomaly))

    if abs(kepler - mean_anomaly) < tolerance:
        return eccentric_anomaly
    
    elif kepler > mean_anomaly:
        while True:
            Operations = eccentric_anomaly - eccentricity * math.sin(math.radians(eccentric_anomaly))
            if abs(Operations-mean_anomaly) <= tolerance:
                break
            eccentric_anomaly -= 0.000001

        return eccentric_anomaly
    
    elif kepler < mean_anomaly:
        while True:
            Operations = eccentric_anomaly - eccentricity * math.sin(math.radians(eccentric_anomaly))
            if abs(Operations-mean_anomaly) <= tolerance:
                break
            eccentric_anomaly += 0.000001

        return eccentric_anomaly
    

# Complex Eccentric Anomaly & Circle Anomaly
# true anomaly
def calculate_true_anomaly(eccentric_anomaly, eccentricity):
    func = math.sqrt((1 + eccentricity) / (1 - eccentricity)) * math.tan(math.radians(eccentric_anomaly) / 2)
    true_anomaly = math.degrees(2 * math.atan(func))
    return true_anomaly

# distance from sun
def calculate_distance_from_sun(semi_major_axis, eccentricity, true_anomaly):
    numerator = semi_major_axis * (1 - (eccentricity ** 2))
    denominator = 1 + (eccentricity * math.cos(math.radians(true_anomaly)))
    distance_from_sun = numerator / denominator
    return distance_from_sun

# 3D Location
# normal x , y
def calculate_orbital_plane_position(distance, true_anomaly):
    x = distance * math.cos(math.radians(true_anomaly))
    y = distance * math.sin(math.radians(true_anomaly))
    return x, y

# argument_of_periapsis , inclination , longitude_of_ascending_node in x , y , z
def calculate_heliocentric_position(distance, true_anomaly, argument_of_periapsis, inclination, longitude_of_ascending_node):
    argument_angle = argument_of_periapsis + true_anomaly
    x = distance * (
        math.cos(math.radians(longitude_of_ascending_node))
        * math.cos(math.radians(argument_angle))
        - math.sin(math.radians(longitude_of_ascending_node))
        * math.sin(math.radians(argument_angle))
        * math.cos(math.radians(inclination))
    )
    y = distance * (
        math.sin(math.radians(longitude_of_ascending_node))
        * math.cos(math.radians(argument_angle))
        + math.cos(math.radians(longitude_of_ascending_node))
        * math.sin(math.radians(argument_angle))
        * math.cos(math.radians(inclination))
    )
    z = distance * (
        math.sin(math.radians(argument_angle))
        * math.sin(math.radians(inclination))
    )
    return x, y, z


# Carrect Planet Place At Space
def calculate_planet_position(planet, target_date):
    period = calculate_orbital_period(planet.semi_major_axis)
    speed = calculate_mean_motion(period)
    days = calculate_days_since_epoch(planet.epoch, target_date)
    new_anomaly = calculate_new_anomaly(planet.mean_anomaly, speed, days)
    eccentric_anomaly = solve_kepler(new_anomaly, planet.eccentricity)
    true_anomaly = calculate_true_anomaly(eccentric_anomaly, planet.eccentricity)
    distance = calculate_distance_from_sun(planet.semi_major_axis, planet.eccentricity, true_anomaly)
    x, y, z = calculate_heliocentric_position(distance, true_anomaly, planet.argument_of_periapsis, planet.inclination, planet.longitude_of_ascending_node)

    return x, y, z


# CONJUCTION CALCULATE
# Geocentric Planet Place
# geocentric position
def calculate_geocentric_position(planet_position, earth_position):
    planet_x, planet_y, planet_z = planet_position
    earth_x, earth_y, earth_z = earth_position

    x = planet_x - earth_x
    y = planet_y - earth_y
    z = planet_z - earth_z

    return x, y, z

# geocentric longitude
def calculate_geocentric_longitude(geocentric_position):
    x, y, z = geocentric_position
    z.str()
    geocentric_longitude = math.degrees(math.atan2(y, x))
    return geocentric_longitude

# Planets Againts Each Other
# θ angle
def calculate_angular_separation(position1, position2):
    x1, y1, z1 = position1
    x2, y2, z2 = position2

    dot_product = (x1 * x2) + (y1 * y2) + (z1 * z2)
    vector_length_a = math.sqrt((x1 ** 2) + (y1 ** 2) + (z1 ** 2))
    vector_length_b = math.sqrt((x2 ** 2) + (y2 ** 2) + (z2 ** 2))
    theta_cos = dot_product / (vector_length_a * vector_length_b)

    theta = math.degrees(math.acos(theta_cos))
    return theta

# calculation the angle
def calculate_planets_angular_separation(planet_A_position, planet_B_position, earth_position):
    a_against_earth = calculate_geocentric_position(planet_A_position, earth_position)
    b_against_earth = calculate_geocentric_position(planet_B_position, earth_position)
    separation = calculate_angular_separation(a_against_earth, b_against_earth)
    
    return separation

#---------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------extra--------------------------------------------------------------------

def calculate_angular_difference(angle1, angle2):
    difference = abs(angle1 - angle2)

    if difference > 180:
        special_difference = 360 - difference
        return special_difference
    
    return difference
