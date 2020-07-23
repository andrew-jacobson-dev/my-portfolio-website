import urllib
import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from contact.models import ContactPoint, ContactMessage
from contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages

# Create your views here.
def contact_index(request):

    # Create objects for context

    # Retrieve contact points (social media, github, etc.)
    contact_points = ContactPoint.objects.order_by('n_page_order')
    # Create empty form
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Get value of input from spam check field
            spam_check = contact_form.cleaned_data['spam_check']

            # Check spam check input
            if not spam_check:
                # Create email contents
                # Get the person's name
                name = contact_form.cleaned_data['name']
                # Create the email subject using their name
                subject = 'New message from ' + name
                # Get the person's message
                message = contact_form.cleaned_data['message']

                # Before emailing, write message to DB so that it is not lost if the email fails
                contact_message = ContactMessage(
                    t_name=name,
                    t_message=message
                )
                # Save the message to the DB
                contact_message.save()
                # Try sending the email
                try:
                    # Send email using send_mail function
                    send_mail(subject, message, settings.EMAIL_HOST_USER, ['andrew@andrewjacobson.dev'], fail_silently=False,)
                    # Add code here for success message
                    messages.success(request, 'Message sent!')
                    return HttpResponseRedirect('/contact/')
                except BadHeaderError:
                    # Add code here for failure message
                    messages.failure(request, 'Uhh, what are you doing?')
                    return HttpResponseRedirect('/contact/')
                except:
                    message.sucess(request, 'Your message was sent!')
                    return HttpResponseRedirect('/contact/')
            else:
                messages.success(request, 'Message sent! ;)')
                return HttpResponseRedirect('/contact/')
        else:
            return HttpResponseRedirect('/contact/')
    # Anything but a POST request
    else:
        # Create context
        context = {
            'contact_points': contact_points,
            'contact_form': contact_form,
        }

    # Return request with context
    return render(request, 'contact_index.html', context)