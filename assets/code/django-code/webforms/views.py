from .forms import Webformform
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
import requests
from django.core.mail import send_mail


def new_feedback_submission(request):
    if request.method == "POST":
        form = Webformform(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

            result = r.json()

            if result['success']:

                form.save()
                # build message body form form
                email_body = "Hi, \n You are being emailed because a new comment was made on the EPSS feedback site. \n the contents are below: \n" + "Name:" + \
                             form.cleaned_data['name'] + '\n' + "Phone:" + form.cleaned_data[
                                 'phone_number'] + '\n' + "Email:" + form.cleaned_data[
                                 'email'] + '\n' + "Affiliation:" + form.cleaned_data[
                                 'affiliation'] + '\n' + "Request body:" + form.cleaned_data['request_body'] + '\n'
                subject = 'New Feedback Submission from http://epss.ucla.edu'
                sender = 'epss@g.ucla.edu'
                recipients = ['roconnor@epss.ucla.edu', 'chair@epss.ucla.edu', 'cbrown@epss.ucla.edu']
                # send message
                send_mail(subject, email_body, sender, recipients, fail_silently=False)

                messages.success(request,
                                 '<p> Thank you for your feedback! </p> <p> If you provided contact information, someone will follow up with you as soon as possible.</p>')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('/feedback')

    else:
        form = Webformform()

    return render(request, 'webforms/feedback.html', {'form': form})
