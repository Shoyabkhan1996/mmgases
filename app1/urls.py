from django.contrib import admin
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('',views.index, name='app1'),
    path('mmg',views.mmg,name='M>M>GASES'),
    path('about',views.about,name='about'),
    path('services',views.services,name="servieses"),
    path('contact',views.contact,name='contact'),
    path("oxcygen",views.oxcygen,name="oxcygen"),
    path("nitrogen",views.nitrogen,name="nitrogen"),
    path("indstrial",views.indstrial,name="indstrial")
]