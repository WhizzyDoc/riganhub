from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('services/', views.ServiceListView.as_view(), name="services"),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(),
         name="service_details"),
    path('team-members/', views.DoctorListView.as_view(), name="team_members"),
    path('team-members/<int:pk>/', views.DoctorDetailView.as_view(),
         name="member_details"),
    path('faqs/', views.FaqListView.as_view(), name="faqs"),
    path('products/', views.GalleryListView.as_view(), name="gallery"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('products/<int:pk>/', views.GalleryDetailView.as_view(),
         name="gallery_details"),
]
