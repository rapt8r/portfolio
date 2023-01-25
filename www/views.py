
from django.http import FileResponse
from django.views.generic import TemplateView
from .models import Skill, Project, Visitor
# Create your views here.

class TrackVisitorsMixin:
    def track(self, request, *args, **kwargs):
        #Check if visitor is registered in DB
        try:
            existing_visitor = Visitor.objects.get(ip=request.META['REMOTE_ADDR'])
            existing_visitor.info = request.headers
            existing_visitor.last_page = request.path
            existing_visitor.views += 1
            existing_visitor.save()
        except Visitor.DoesNotExist:
            new_visitor = Visitor(ip=request.META['REMOTE_ADDR'], info=request.headers, last_page=request.path, source=request.GET.get('source', ''))
            new_visitor.clean()
            new_visitor.save()

class IndexPage(TrackVisitorsMixin, TemplateView):
    template_name = 'www/index.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['skills'] = Skill.objects.all().filter(visible=True)
        context['projects'] = Project.objects.all()
        self.track(request)
        return self.render_to_response(context)
class AboutMePage(TemplateView):
    template_name = 'www/about-me.html'
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
    return FileResponse(open('C:/Users/domin/Desktop/vps/static/www/img/test.jpg', 'rb'))


