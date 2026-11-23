from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
    ('planning', 'Planning'),
    ('design', 'Design'),
    ('development', 'Development'),
    ('completed', 'Completed'),
    ('paused', 'Paused'),
]
    name = models.CharField(max_length=150)
    details = models.TextField()
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/images')

    def __str__(self):
        return self.project.name