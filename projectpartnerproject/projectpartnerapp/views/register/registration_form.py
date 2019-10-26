from django.shortcuts import render

# This view takes you to the registration form.
# The registration/registration.html is the template containing the form.


def register_form(request):
    template = 'registration/registration.html'
    # Nothing needs to be sent to the template--so an empty dictionary is being sent.
    context = {}

    return render(request, template, context)