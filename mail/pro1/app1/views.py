from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.mail import send_mail



def mail_view(request):
    template_name = 'demo.html'
    if request.method == 'POST':
        my_mail = request.POST['my_mail']
        print(my_mail)
        my_name = request.POST['my_name']
        subject = 'welcome to website'
        message = f'Hi {my_name}, thank you for registering in our website.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [my_mail]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse('Mail sent check once')
    return render(request, template_name)


