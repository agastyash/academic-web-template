from django.urls import path

from . import views

app_name = "homepage"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about", views.AboutView.as_view(), name="about"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("courses", views.CoursesView.as_view(), name="courses"),
    path("results", views.ResultsView.as_view(), name="results"),
]