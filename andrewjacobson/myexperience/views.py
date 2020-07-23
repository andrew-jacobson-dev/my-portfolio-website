from django.shortcuts import render
from myexperience.models import Experience, ExperienceResponsibility, ExperienceAccomplishment, Education, Certification, Skill


# Create your views here.
def myexperience_index(request):

    # Jobs section queries
    experiences = Experience.objects.order_by('-d_start')
    responsibilities = ExperienceResponsibility.objects.order_by('n_experience', 'n_page_order')
    accomplishments = ExperienceAccomplishment.objects.order_by('n_experience', 'n_page_order')

    # Education section queries
    education = Education.objects.order_by('-d_start')

    # Certifications section queries
    certifications = Certification.objects.order_by('n_page_order')

    # Professional skills section queries
    professionalSkillsDatabases = Skill.objects.filter(c_proficiency='1', c_type='D').order_by('t_skill')
    professionalSkillsLanguages = Skill.objects.filter(c_proficiency='1', c_type='L').order_by('t_skill')
    professionalSkillsFrameworks = Skill.objects.filter(c_proficiency='1', c_type='F').order_by('t_skill')
    professionalSkillsSoftwares = Skill.objects.filter(c_proficiency='1', c_type='S').order_by('t_skill')
    professionalSkillsPlatforms = Skill.objects.filter(c_proficiency='1', c_type='P').order_by('t_skill')

    # Personal skills section queries
    personalSkillsDatabases = Skill.objects.filter(c_proficiency='2', c_type='D').order_by('t_skill')
    personalSkillsLanguages = Skill.objects.filter(c_proficiency='2', c_type='L').order_by('t_skill')
    personalSkillsFrameworks = Skill.objects.filter(c_proficiency='2', c_type='F').order_by('t_skill')
    personalSkillsSoftwares = Skill.objects.filter(c_proficiency='2', c_type='S').order_by('t_skill')
    personalSkillsPlatforms = Skill.objects.filter(c_proficiency='2', c_type='P').order_by('t_skill')

    # Creating the context object with QuerySets created above
    context = {
        'experiences': experiences,
        'responsibilities': responsibilities,
        'accomplishments': accomplishments,
        'education': education,
        'certifications': certifications,
        'professionalSkillsDatabases': professionalSkillsDatabases,
        'professionalSkillsLanguages': professionalSkillsLanguages,
        'professionalSkillsFrameworks': professionalSkillsFrameworks,
        'professionalSkillsSoftwares': professionalSkillsSoftwares,
        'professionalSkillsPlatforms': professionalSkillsPlatforms,
        'personalSkillsDatabases': personalSkillsDatabases,
        'personalSkillsLanguages': personalSkillsLanguages,
        'personalSkillsFrameworks': personalSkillsFrameworks,
        'personalSkillsSoftwares': personalSkillsSoftwares,
        'personalSkillsPlatforms': personalSkillsPlatforms,
    }

    return render(request, 'myexperience_index.html', context)