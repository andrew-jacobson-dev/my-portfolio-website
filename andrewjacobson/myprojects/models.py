from django.db import models
from tinymce.models import HTMLField


# Create your models here.

# class Game(models.Model):
#     s_played = models.DateTimeField('timestamp of game played')
#     i_doubles = models.CharField(max_length=1, null=True)
#     n_winner_1 = models.CharField(max_length=25)
#     n_winner_2 = models.CharField(max_length=25, null=True)
#     n_loser_1 = models.CharField(max_length=25)
#     n_loser_2 = models.CharField(max_length=25, null=True)
#     a_winning_score = models.SmallIntegerField()
#     a_losing_score = models.SmallIntegerField()

class Project(models.Model):
    t_title = models.CharField(max_length=100)
    t_blurb = models.CharField(max_length=200)
    t_objective = models.TextField()
    t_code_url = models.CharField(max_length=100, default='', blank=True)
    t_details = HTMLField()
    t_technology_used = models.CharField(max_length=75)
    t_image_path = models.ImageField(upload_to="images/")
    n_page_order = models.SmallIntegerField(null=True)
    c_type = models.CharField(max_length=1)

    def __str__(self):
        return self.t_title + " - " + str(self.n_page_order)


class ProjectComment(models.Model):
    n_project = models.ForeignKey('Project', on_delete=models.CASCADE)
    t_author = models.CharField(max_length=60)
    t_comment = models.TextField()
    s_written = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.t_comment