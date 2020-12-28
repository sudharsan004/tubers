from django.template import Context
from .models import ContactInfo


def contact(request):
    details = ContactInfo.objects.get(id=1)
    return {'contact_info': details}
