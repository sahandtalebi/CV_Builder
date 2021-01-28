from django.shortcuts import render
from .forms import ContactUs
from .models import Contact, Information


def contact_page(request, *args, **kwargs):
    information = Information.objects.first()
    contact_us = ContactUs(request.POST or None)

    if contact_us.is_valid():
        full_name = contact_us.cleaned_data.get('full_name')
        email = contact_us.cleaned_data.get('email')
        massage = contact_us.cleaned_data.get('massage')
        Contact.objects.create(full_name=full_name, email=email, massage=massage)

        contact_us = ContactUs
    context = {
        "information": information,
        "contact": contact_us,
    }
    return render(request, 'contact_us.html', context)
