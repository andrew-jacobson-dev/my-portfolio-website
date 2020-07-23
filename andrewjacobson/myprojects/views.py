from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from myprojects.forms import CommentForm
from myprojects.models import Project, ProjectComment


# Create your views here.
def myprojects_index(request):
    myprojects = Project.objects.order_by('n_page_order')
    context = {
        'projects': myprojects
    }
    return render(request, 'myprojects_index.html', context)


def myprojects_detail(request, project_id):

    # Create objects for context

    # Retrieve the project details
    myproject = Project.objects.get(pk=project_id)
    # Create empty comment form
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Get value of input from spam check field
            spam_check = form.cleaned_data['spam_check']
            # Check spam check input
            if not spam_check:
                # Create database object
                comment = ProjectComment(
                    t_author=form.cleaned_data["author"],
                    t_comment=form.cleaned_data["body"],
                    n_project_id=project_id
                )
                # Save the comment to the DB
                comment.save()
                # Clear the form after saving it
                form = CommentForm()
                return HttpResponseRedirect('/projects/' + str(project_id) + '/')
            else:
                return HttpResponseRedirect('/projects/' + str(project_id) + '/')
    # Anything but a POST request
    else:
        # Retrieve the comments for the project
        comments = ProjectComment.objects.filter(n_project=project_id).order_by('-s_written')
        # Create context
        context = {
            'project': myproject,
            'comments': comments,
            'form': form,
        }

    # Return request with context
    return render(request, 'myprojects_detail.html', context)