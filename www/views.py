import os

from django.http import FileResponse
from django.views.generic import TemplateView
from .models import Skill, Project, Visitor, Entry
# Create your views here.

class TrackVisitorsMixin:
    def track(self, request, *args, **kwargs):
        #Check if visitor is registered in DB
        new_entry = Entry()
        try:
            #Visitor already exists
            existing_visitor = Visitor.objects.get(ip=request.META['REMOTE_ADDR'])
            new_entry.set_info(request, existing_visitor)
            new_entry.save()
        except Visitor.DoesNotExist:
            #Visitor doesn't exist
            new_visitor = Visitor(ip=request.META['REMOTE_ADDR'], source=request.GET.get('source', ''))
            new_visitor.clean()
            new_visitor.save()
            new_entry.set_info(request, new_visitor)
            new_entry.save()

class IndexPage(TrackVisitorsMixin, TemplateView):
    template_name = 'www/index.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['skills'] = Skill.objects.all().filter(visible=True)
        context['projects'] = Project.objects.all()
        self.track(request)
        return self.render_to_response(context)
class Error404Page(TrackVisitorsMixin, TemplateView):
    template_name = 'www/404.html'
    def get(self, request, *args, **kwargs):
        self.track(request)
        return super().get(self, request, *args, **kwargs)
class DownloadCVPage(TrackVisitorsMixin, TemplateView):
    template_name = 'www/download-cv.html'
    def get(self, request, *args, **kwargs):
        self.track(request)
        return super().get(self, request, *args, **kwargs)
def OpenGraphPage(request):
    return FileResponse(open(os.getenv('OPEN_GRAPH_PATH'), 'rb'))


