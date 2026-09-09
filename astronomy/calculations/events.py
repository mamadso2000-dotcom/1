from datetime import timedelta
from itertools import combinations
from ..models import Event
from .orbital import calculate_planet_position, calculate_planets_angular_separation

# conjunction
def is_close_conjunction(separation):
    if separation <= 3:
        return True
    else:
        return False

def calculate_next_day(current_date):
    next_day = current_date + timedelta(days=1)
    return next_day

def check_event_window(planet_A, planet_B, earth, start_date, end_date):
    current_date = start_date
    event_active = False
    events = []

    while current_date <= end_date:
        earth_position = calculate_planet_position(earth, current_date)
        planet_A_position = calculate_planet_position(planet_A, current_date)
        planet_B_position = calculate_planet_position(planet_B, current_date)
        separation = calculate_planets_angular_separation(
            planet_A_position,
            planet_B_position,
            earth_position
        )

        conjunction = is_close_conjunction(separation)

        if conjunction:

            if not event_active:
                event_start = current_date

            event_active = True

        elif event_active:
            event_active = False
            event_end = current_date - timedelta(days=1)
            events.append((event_start, event_end))

        current_date = calculate_next_day(current_date)

    if event_active:
        event_end = end_date
        events.append((event_start, event_end))

    return events

def combinations_planets(planet_list):
    list_planet = list(planet_list)
    for planet in planet_list:
        if planet.name == 'Earth':
            list_planet.remove(planet)
    planet_groups = combinations(list_planet, 2)
    return planet_groups

def find_conjunctions(planet_list, earth, start_date, end_date):
    planet_groups = combinations_planets(planet_list)
    conjunction_list = {}
    for planet_pair in planet_groups:
        conjunction = check_event_window(planet_pair[0], planet_pair[1], earth, start_date, end_date)
        if conjunction:
            conjunction_list[planet_pair] = conjunction
    return conjunction_list

def create_event_data(conjunctions):
    conjunctions_list = []
    for planet_pair, events in conjunctions.items():
        event_type = "conjunction"

        planet_A = planet_pair[0]
        planet_B = planet_pair[1]

        for event in events:
            start_date = event[0]
            end_date = event[1]

            event_data = {
                'event_type' : event_type,
                'planet_A' : planet_A,
                'planet_B' : planet_B,
                'start_date' : start_date,
                'end_date' : end_date
            }

            conjunctions_list.append(event_data)

    return conjunctions_list

def save_event_data(event_data):
    for event in event_data:
        event_type = event['event_type']
        planet_A = event['planet_A']
        planet_B = event['planet_B']
        start_date = event['start_date']
        end_date = event['end_date']
        if Event.objects.filter(planet_A=planet_A, planet_B=planet_B, start_date=start_date, end_date=end_date):
            continue

        Event.objects.create(event_type=event_type, planet_A=planet_A, planet_B=planet_B, start_date=start_date, end_date=end_date)