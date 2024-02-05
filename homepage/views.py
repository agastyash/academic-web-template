from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from .models import Testimonial, Course, Result, Teacher

# Create your views here.
class IndexView(TemplateView):
    template_name = "homepage/index.html"

    def get_context_data(self):
        context = {"testimonial_list": Testimonial.objects.all(), "active_link": "home"}
        return context
    
class AboutView(TemplateView):
    template_name = "homepage/about.html"

    def get_context_data(self):
        return {"teacher_list": Teacher.objects.all(), "active_link": "about"}
    
class ContactView(TemplateView):
    template_name = "homepage/contact.html"

    def get_context_data(self):
        return {"active_link": "contact"}
    
class CoursesView(TemplateView):
    template_name = "homepage/courses.html"

    def get_context_data(self):
        context = {"course_list": Course.objects.all(), "active_link": "courses"}
        return context
    
class ResultsView(TemplateView):
    template_name = "homepage/results.html"

    def get_context_data(self):
        return {"result_list": Result.objects.all(), "active_link": "results"}