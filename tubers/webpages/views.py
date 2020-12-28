from django.shortcuts import render
from .models import *
# Create your views here.
from youtubers.models import Ytuber
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    sliders = Slider.objects.all()
    team_members = TeamMember.objects.all()
    featured_ytubers = Ytuber.objects.order_by(
        '-created_at').filter(is_featured=True)
    ytubers = Ytuber.objects.order_by('-created_at')
    context = {'sliders': sliders,
               'team_members': team_members, 'ytubers': ytubers, 'featured_ytubers': featured_ytubers}
    return render(request, 'webpages/home.html', context)


def services(request):
    return render(request, 'webpages/services.html')


def about(request):
    about_event = AboutModel.objects.all()
    team_members = TeamMember.objects.all()
    data = {'team_members': team_members, 'about_event': about_event}
    return render(request, 'webpages/about.html', data)


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        country = request.POST['country']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            'YTubers Services',
            f'''Hi, {full_name} !
            We have received Your message regarding {subject}, Our representative will call you Asap.
            Have a nice day !
            ''',
            '8921test@gmail.com',
            [email],
            fail_silently=False,
        )
        new_contact_message = ContactModel(
            full_name=full_name, email=email, country=country, company=company, subject=subject, message=message)
        new_contact_message.save()
        messages.success(request, 'Thanks for Your Message!')
        redirect('home')
    return render(request, 'webpages/contact.html')
