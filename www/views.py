from django.shortcuts import render
from django.http import FileResponse
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
class AboutMePage(TemplateView):
    template_name = 'www/about-me.html'
class ContactPage(TemplateView):
    template_name = 'www/contact.html'

class DownloadCVPage(TemplateView):
    template_name = 'www/download-cv.html'

def OpenGraphPage(request):
    return FileResponse(open('C:/Users/domin/Desktop/vps/static/www/img/test.jpg', 'rb'))