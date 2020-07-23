from django.contrib import admin
from .models import Experience, ExperienceResponsibility, ExperienceAccomplishment, Education, Certification, Skill

# Register your models here.
admin.site.register(Experience)
admin.site.register(ExperienceResponsibility)
admin.site.register(ExperienceAccomplishment)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Skill)