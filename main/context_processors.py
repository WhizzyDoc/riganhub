from .models import *


def footer_content(request):
    services = Service.objects.all()[:8]
    developers = Developer.objects.all()[:8]
    site = Site.objects.first()
    context = {
        'our_services': services,
        'our_experts': developers,
        'mysite': site
    }
    return context
