from django.shortcuts import render
from about.models import Bio, CurrentProject, Testimonial
# Create your views here.


def about_index(request):

    # Fetch About page content
    # Bio section
    bio = Bio.objects.get()
    # Testimonials
    testimonials = Testimonial.objects.order_by('n_page_order')
    # Current projects
    current_projects = CurrentProject.objects.order_by('n_page_order')

    # Create context
    context = {
        'bio': bio,
        'testimonials': testimonials,
        'current_projects': current_projects,
    }

    return render(request, 'about_index.html', context)