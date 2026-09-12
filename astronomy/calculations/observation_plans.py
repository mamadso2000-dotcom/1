from datetime import timedelta
from ..models import ObservationPlan, Event
from .orbital import calculate_planets_angular_separation, calculate_planet_position

def min_angular_separation(event, earth):
    best_date = event.start_date
    best_separation = None
    current_date = event.start_date
    while current_date <= event.end_date:
        planet_A_position = calculate_planet_position(planet=event.planet_A, target_date=current_date)
        planet_B_position = calculate_planet_position(planet=event.planet_B, target_date=current_date)
        earth_position = calculate_planet_position(planet=earth, target_date=current_date)
        separation = calculate_planets_angular_separation(planet_A_position=planet_A_position, planet_B_position=planet_B_position, earth_position=earth_position)
        if best_separation is None or separation < best_separation:
            best_separation = separation
            best_date = current_date
        current_date += timedelta(days=1)
    return best_date, best_separation

def add_observation_plan_to_db(event, best_date, best_separation):
    observation_plan, created = ObservationPlan.objects.update_or_create(event=event, defaults={'observation_date' : best_date, 'angular_separation' : best_separation})
    return observation_plan

def create_observation_plans(earth):
    events = Event.objects.all()
    for event in events:
        best_date, best_separation = min_angular_separation(event, earth)
        add_observation_plan_to_db(event, best_date, best_separation)