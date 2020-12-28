from django.shortcuts import render, redirect
from django.contrib import messages
from youtubers.models import Ytuber
from django.core.mail import send_mail
from contact_tuber.models import ContactInfo

# Create your views here.


def contactTuber(request, id):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        youtuber_contacted = Ytuber.objects.get(id=id)
        user_id = request.POST['user_id']

        # Send mail
        send_mail(
            'YTubers Services',
            f'''Hi, {first_name} !
            Your message regarding {subject} has been sent to {youtuber_contacted.name} and he/she will respond Asap.
            Have a nice day !
            ''',
            '8921test@gmail.com',
            [email, youtuber_contacted.email],
            fail_silently=False,
        )

        # saving messages
        new_msg = ContactInfo(first_name=first_name,
                              last_name=last_name, email=email, city=city, state=state, phone=phone, subject=subject, message=message, ytuber_contacted=youtuber_contacted)
        new_msg.save()
        messages.success(
            request, f'{first_name} Your Message Sent! {youtuber_contacted.name} will respond Asap!')
        return redirect('youtuber_detail', id=id)
    return redirect('youtuber_detail', id=id)
