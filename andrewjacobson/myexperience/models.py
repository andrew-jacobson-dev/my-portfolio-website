from django.db import models

# Create your models here.
class Experience(models.Model):
    t_position = models.CharField(max_length=50)
    t_company = models.CharField(max_length=50)
    t_company_url = models.CharField(max_length=100)
    t_city = models.CharField(max_length=20)
    c_state = models.CharField(max_length=2)
    t_country = models.CharField(max_length=20)
    d_start = models.DateField()
    d_end = models.DateField(default='9999-12-31', null=True)
    t_overview = models.TextField()

    def __str__(self):
        return self.t_position + " at " + self.t_company


class ExperienceResponsibility(models.Model):
    n_experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
    t_title = models.CharField(max_length=100)
    t_responsibility = models.TextField(default='', blank=True)
    n_page_order = models.SmallIntegerField()

    def __str__(self):
        return self.t_title


class ExperienceAccomplishment(models.Model):
    n_experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
    t_accomplishment = models.TextField(default='', blank=True)
    n_page_order = models.SmallIntegerField()

    def __str__(self):
        return self.t_accomplishment


class Education(models.Model):
    t_degree = models.CharField(max_length=75)
    t_university = models.CharField(max_length=50)
    t_city = models.CharField(max_length=20)
    c_state = models.CharField(max_length=2)
    t_country = models.CharField(max_length=20)
    d_start = models.DateField()
    d_end = models.DateField(null=True)

    def __str__(self):
        return self.t_degree


class Certification(models.Model):
    t_certification = models.CharField(max_length=100)
    t_certification_path = models.ImageField(upload_to="images/", blank=True)
    n_page_order = models.SmallIntegerField()

    def __str__(self):
        return self.t_certification


class Skill(models.Model):
    c_type = models.CharField(max_length=1)
    t_skill = models.CharField(max_length=100)
    c_proficiency = models.CharField(max_length=1)

    def __str__(self):
        return self.t_skill
