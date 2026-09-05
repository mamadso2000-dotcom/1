from datetime import timedelta
from .orbital import calculate_planet_position, calculate_planets_angular_separation

# conjunction
def is_close_conjunction(separation):
    if separation <= 3:
        return True
    else:
        return False

def calculate_event_window_end(start_date):
    end_date = start_date + timedelta(days=30)
    return end_date

def calculate_next_day(current_date):
    next_day = current_date + timedelta(days=1)
    return next_day

def check_event_window(planet_A, planet_B, earth, start_date):
    current_date = start_date
    end_date = calculate_event_window_end(start_date)
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
