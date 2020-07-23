from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Bio(models.Model):
    t_image_path = models.ImageField(upload_to="images/")
    t_details = HTMLField()

class CurrentProject(models.Model):
    t_current_project = models.CharField(max_length=100)
    n_page_order = models.SmallIntegerField(null=True)

class Testimonial(models.Model):
    t_testimonial = models.CharField(max_length=100)
    t_reviewer = models.CharField(max_length=25)
    a_star_rating = models.SmallIntegerField()
    n_page_order = models.SmallIntegerField(null=True)