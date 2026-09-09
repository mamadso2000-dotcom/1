from django.db import models

# Create your models here.
class Planet(models.Model):
    # Basic Elements
    name = models.CharField(max_length=100, unique=True)
    diameter = models.FloatField(help_text="km")
    composition = models.TextField()
    moons = models.IntegerField()
    image = models.ImageField(upload_to="planets/")

    # Orbital Elements
    semi_major_axis = models.FloatField(help_text="AU")
    eccentricity = models.FloatField(help_text="Dimensionless")
    inclination = models.FloatField(help_text="Degrees")
    longitude_of_ascending_node = models.FloatField(help_text="Degrees")
    argument_of_periapsis = models.FloatField(help_text="Degrees")
    mean_anomaly = models.FloatField(help_text="Degrees")
    epoch = models.DateTimeField()

    def __str__(self):
        return self.name
    
class Event(models.Model):
    event_type = models.CharField(max_length=50)

    planet_A = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name="events_as_planet_A")
    planet_B = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name="events_as_planet_B")

    start_date = models.DateField()
    end_date = models.DateField()