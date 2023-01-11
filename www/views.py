from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.base import ContextMixin
from .models import Skill, Project
# Create your views here.


class IndexPage(TemplateView):
    template_name = 'www/index.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['skills'] = Skill.objects.all().filter(visible=True)
        context['projects'] = Project.objects.all()
        return self.render_to_response(context)


class ProjectPage(TemplateView):
    template_name = 'www/project.html'

class DownloadCVPage(TemplateView):
    template_name = 'www/download-cv.html'
