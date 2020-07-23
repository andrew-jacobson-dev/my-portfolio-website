from django.db import models

# Create your models here.
class ContactPoint(models.Model):
    t_site = models.CharField(max_length=50)
    t_site_url = models.CharField(max_length=100)
    t_site_logo = models.ImageField(upload_to="images/")
    t_blurb = models.TextField(default='', blank=True)
    n_page_order = models.SmallIntegerField()

    def __str__(self):
        return self.t_site + " - " + str(self.n_page_order)


class ContactMessage(models.Model):
    s_received = models.DateTimeField(auto_now_add=True)
    t_name = models.CharField(max_length=60)
    t_message = models.TextField()

    def __str__(self):
        return "Message from " + self.t_name + " at " + str(self.s_received)