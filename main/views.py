from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import View
from .utils import *

class HomeView(ListView):
    template_name = 'main/index.html'
    queryset = Service.objects.all()
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = Slider.objects.all()
        context['experts'] = Developer.objects.all()
        context['features'] = Feature.objects.all()
        context['reviews'] = Review.objects.all()
        context['faqs'] = Faq.objects.all()
        return context


class ServiceListView(ListView):
    queryset = Service.objects.all()
    template_name = "main/services.html"


class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = "main/service_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context


class DoctorListView(ListView):
    template_name = 'main/team.html'
    queryset = Developer.objects.all()
    paginate_by = 8


class DoctorDetailView(DetailView):
    template_name = 'main/team-details.html'
    queryset = Developer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["developers"] = Developer.objects.all()
        return context

class ContactView(TemplateView):
    template_name = "main/contact.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = "Rigan Tech Message Alert"

        if name and message and email and phone:
            Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
            send_contact_message(
                email,
                name,
                subject,
                message
            )
            messages.success(request, " Email has been sent successfully...")

        return redirect('contact')


class FaqListView(ListView):
    template_name = 'main/faqs.html'
    queryset = Faq.objects.all()


class GalleryListView(ListView):
    template_name = 'main/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 9

class GalleryDetailView(DetailView):
    queryset = Gallery.objects.all()
    template_name = "main/gallery_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["galleries"] = Gallery.objects.all()
        return context



"""

class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'doctors': Doctor.objects.all()
        }
        return render(request, "appointment/index.html", context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')
        if doctor_id:
            doctor = get_object_or_404(Doctor, id=doctor_id)

        if(name and phone and email and doctor and date and time):
            Appointment.objects.create(
                name=name, phone=phone, email=email, doctor=doctor, date=date, time=time, note=note)
            messages.success(request,'Appointment done successfully')
        return redirect('appointment')

"""